"""Pruebas de comportamiento: fallos, reintentos, cambios tardíos y reconciliación."""
import unittest
from copy import deepcopy
from pipeline import connect, ingest, batches, gold, snapshot, validate


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.db = connect()

    def tearDown(self):
        self.db.close()

    def load(self):
        for i, batch in enumerate(batches(), 1):
            ingest(self.db, "credit", i, batch)

    def test_duplicate_does_not_inflate_total(self):
        ingest(self.db, "credit", 1, batches()[0])
        self.assertEqual(gold(self.db), [("2026-01-01", 2, 15000)])

    def test_invalid_amount_goes_to_quarantine(self):
        r = ingest(self.db, "credit", 1, batches()[0])
        self.assertEqual(r["rejected"], 1)
        self.assertEqual(self.db.execute("SELECT reason FROM quarantine").fetchall(), [("invalid_amount",)])

    def test_retry_is_idempotent(self):
        self.load()
        before = snapshot(self.db)
        for i, b in enumerate(batches(), 1):
            self.assertTrue(ingest(self.db, "credit", i, b)["replayed"])
        self.assertEqual(snapshot(self.db), before)
        self.assertEqual(self.db.execute("SELECT count(*) FROM audit").fetchone()[0], 3)

    def test_stale_update_cannot_overwrite_newer(self):
        self.load()
        self.assertEqual(self.db.execute("SELECT version,amount_cents FROM silver WHERE event_id='A'").fetchone(), (2, 12000))

    def test_deleted_row_does_not_resurrect(self):
        self.load()
        self.assertEqual(self.db.execute("SELECT version,deleted FROM silver WHERE event_id='B'").fetchone(), (2, 1))

    def test_reconciled_gold(self):
        self.load()
        self.assertEqual(gold(self.db), [("2026-01-01", 2, 15000), ("2026-01-02", 1, 7000)])

    def test_failure_rolls_back_data_checkpoint_and_audit(self):
        with self.assertRaises(RuntimeError):
            ingest(self.db, "credit", 1, batches()[0], fail_after=2)
        for table in ("bronze", "silver", "checkpoints", "audit", "quarantine"):
            self.assertEqual(self.db.execute(f"SELECT count(*) FROM {table}").fetchone()[0], 0)
        ingest(self.db, "credit", 1, batches()[0])
        self.assertEqual(gold(self.db), [("2026-01-01", 2, 15000)])

    def test_changed_retry_rejected(self):
        ingest(self.db, "credit", 1, batches()[0])
        changed = deepcopy(batches()[0]); changed[0]["amount_cents"] = 999
        with self.assertRaises(ValueError):
            ingest(self.db, "credit", 1, changed)

    def test_same_version_conflict_rolls_back_whole_batch(self):
        b = deepcopy(batches()[0][:2]); b.append(dict(b[0], amount_cents=999))
        with self.assertRaises(ValueError):
            ingest(self.db, "credit", 1, b)
        self.assertEqual(snapshot(self.db), [])

    def test_missing_batch_is_not_skipped(self):
        with self.assertRaises(ValueError):
            ingest(self.db, "credit", 2, batches()[1])

    def test_sources_are_isolated(self):
        ingest(self.db, "credit", 1, batches()[0][:1])
        ingest(self.db, "hospital", 1, [dict(batches()[0][0], amount_cents=2500)])
        self.assertEqual(len(snapshot(self.db)), 2)

    def test_invalid_types_and_dates(self):
        base = batches()[0][0]
        for row in (None, [], {}, dict(base, amount_cents=True),
                    dict(base, event_time="2026-02-30T12:00:00Z"), dict(base, version=0)):
            self.assertIsNotNone(validate(row))

    def test_empty_batch_advances_checkpoint(self):
        ingest(self.db, "credit", 1, [])
        self.assertEqual(self.db.execute("SELECT sequence FROM checkpoints").fetchone()[0], 1)

    def test_rebuild_matches_incremental_state(self):
        self.load()
        latest = {}
        for b in batches():
            for row in b:
                if validate(row) is None and row["version"] > latest.get(row["event_id"], {}).get("version", 0):
                    latest[row["event_id"]] = row
        expected = sorted(("credit", r["event_id"], r["version"], r["customer_id"], r["event_time"],
                           r["amount_cents"], int(r["op"] == "DELETE")) for r in latest.values())
        self.assertEqual(snapshot(self.db), expected)


if __name__ == "__main__":
    unittest.main(verbosity=2)
