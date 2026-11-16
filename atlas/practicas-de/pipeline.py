"""Pipeline didáctico local, Python 3.10+ y SQLite. Solo datos sintéticos.

Una transacción por lote protege datos y checkpoint. Esto NO simula la
concurrencia, el escalado ni todas las garantías de Delta/Spark.
"""
import argparse
import hashlib
import json
import sqlite3
from pathlib import Path

DDL = """
CREATE TABLE IF NOT EXISTS bronze(
 source TEXT NOT NULL, event_id TEXT NOT NULL, version INTEGER NOT NULL,
 payload TEXT NOT NULL, PRIMARY KEY(source,event_id,version));
CREATE TABLE IF NOT EXISTS silver(
 source TEXT NOT NULL, event_id TEXT NOT NULL, version INTEGER NOT NULL,
 customer_id TEXT NOT NULL, event_time TEXT NOT NULL, amount_cents INTEGER NOT NULL,
 deleted INTEGER NOT NULL CHECK(deleted IN (0,1)), PRIMARY KEY(source,event_id));
CREATE TABLE IF NOT EXISTS quarantine(
 source TEXT NOT NULL, fingerprint TEXT NOT NULL, reason TEXT NOT NULL,
 payload TEXT NOT NULL, PRIMARY KEY(source,fingerprint));
CREATE TABLE IF NOT EXISTS checkpoints(
 source TEXT PRIMARY KEY, sequence INTEGER NOT NULL);
CREATE TABLE IF NOT EXISTS audit(
 source TEXT NOT NULL, sequence INTEGER NOT NULL, checksum TEXT NOT NULL,
 received INTEGER NOT NULL, rejected INTEGER NOT NULL,
 PRIMARY KEY(source,sequence));
"""


def connect(path=":memory:"):
    conn = sqlite3.connect(path)
    conn.executescript(DDL)
    return conn


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def validate(row):
    from datetime import datetime
    if not isinstance(row, dict):
        return "record_not_object"
    required = {"event_id", "version", "customer_id", "event_time", "amount_cents", "op"}
    if not required <= row.keys():
        return "missing_fields"
    if not all(isinstance(row[k], str) and row[k].strip() for k in ("event_id", "customer_id")):
        return "invalid_key"
    if type(row["version"]) is not int or row["version"] < 1:
        return "invalid_version"
    if type(row["amount_cents"]) is not int or row["amount_cents"] < 0:
        return "invalid_amount"
    if row["op"] not in ("UPSERT", "DELETE"):
        return "invalid_operation"
    try:
        # Contrato del ejercicio: UTC, exactamente YYYY-MM-DDTHH:MM:SSZ.
        datetime.strptime(row["event_time"], "%Y-%m-%dT%H:%M:%SZ")
        if len(row["event_time"]) != 20:
            return "invalid_time"
    except (ValueError, TypeError):
        return "invalid_time"
    return None


def ingest(conn, source, sequence, rows, fail_after=None):
    """Lotes contiguos por fuente; reintentos requieren idéntico contenido.

    version ordena cambios de una entidad; sequence ordena lotes. Un DELETE
    conserva un tombstone para que un evento viejo no resucite la entidad.
    """
    if not source or type(sequence) is not int or sequence < 1:
        raise ValueError("Fuente y secuencia positiva requeridas")
    checksum = hashlib.sha256(canonical(rows).encode()).hexdigest()
    previous = conn.execute(
        "SELECT checksum FROM audit WHERE source=? AND sequence=?", (source, sequence)
    ).fetchone()
    if previous:
        if previous[0] != checksum:
            raise ValueError("El lote ya confirmado cambió de contenido")
        return {"replayed": True, "rejected": 0}
    checkpoint = conn.execute("SELECT sequence FROM checkpoints WHERE source=?", (source,)).fetchone()
    if sequence != (checkpoint[0] if checkpoint else 0) + 1:
        raise ValueError("Secuencia no contigua; falta un lote anterior")
    rejected = 0
    with conn:
        for i, row in enumerate(rows, 1):
            payload = canonical(row)
            reason = validate(row)
            if reason:
                rejected += 1
                digest = hashlib.sha256(payload.encode()).hexdigest()
                conn.execute("INSERT OR IGNORE INTO quarantine VALUES(?,?,?,?)",
                             (source, digest, reason, payload))
            else:
                existing = conn.execute(
                    "SELECT payload FROM bronze WHERE source=? AND event_id=? AND version=?",
                    (source, row["event_id"], row["version"])).fetchone()
                if existing and existing[0] != payload:
                    raise ValueError("Dos payloads para la misma clave y versión")
                conn.execute("INSERT OR IGNORE INTO bronze VALUES(?,?,?,?)",
                             (source, row["event_id"], row["version"], payload))
                conn.execute("""INSERT INTO silver VALUES(?,?,?,?,?,?,?)
                    ON CONFLICT(source,event_id) DO UPDATE SET
                    version=excluded.version, customer_id=excluded.customer_id,
                    event_time=excluded.event_time, amount_cents=excluded.amount_cents,
                    deleted=excluded.deleted
                    WHERE excluded.version > silver.version""",
                    (source, row["event_id"], row["version"], row["customer_id"],
                     row["event_time"], row["amount_cents"], int(row["op"] == "DELETE")))
            if fail_after is not None and i == fail_after:
                raise RuntimeError("Fallo inyectado: verificar rollback antes de reintentar")
        conn.execute("INSERT INTO audit VALUES(?,?,?,?,?)", (source, sequence, checksum, len(rows), rejected))
        conn.execute("INSERT INTO checkpoints VALUES(?,?) ON CONFLICT(source) DO UPDATE SET sequence=excluded.sequence",
                     (source, sequence))
    return {"replayed": False, "rejected": rejected}


def gold(conn):
    return conn.execute("""SELECT substr(event_time,1,10) AS day,
        COUNT(*) AS events, SUM(amount_cents) AS total_cents
        FROM silver WHERE deleted=0 GROUP BY day ORDER BY day""").fetchall()


def snapshot(conn):
    return conn.execute("SELECT * FROM silver ORDER BY source,event_id").fetchall()


def batches():
    def e(key, version, cents, op="UPSERT", day="01"):
        return dict(event_id=key, version=version, customer_id="C001",
                    event_time=f"2026-01-{day}T12:00:00Z", amount_cents=cents, op=op)
    return [
        [e("A", 1, 10000), e("B", 1, 5000), e("A", 1, 10000), e("BAD", 1, -50)],
        [e("A", 2, 12000), e("C", 1, 7000, day="02"), e("B", 2, 0, "DELETE")],
        [e("A", 1, 10000), e("B", 1, 5000), e("D", 1, 3000)],
    ]


def demo(path):
    conn = connect(path)
    try:
        for seq, rows in enumerate(batches(), 1):
            print("batch", seq, ingest(conn, "credit", seq, rows))
        print("gold", gold(conn))
        print("checkpoint", conn.execute("SELECT * FROM checkpoints").fetchall())
        print("quarantine", conn.execute("SELECT reason,count(*) FROM quarantine GROUP BY reason").fetchall())
    finally:
        conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", default=":memory:", help="Ruta SQLite; por defecto no escribe archivos")
    demo(parser.parse_args().db)
