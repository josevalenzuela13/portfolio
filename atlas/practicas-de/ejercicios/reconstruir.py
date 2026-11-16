"""Ejercicio DE-R05/DE-R06. Implementa sin copiar pipeline.ingest.

Entrada: lista de lotes con eventos del contrato de pipeline.py.
Salida: lista de tuplas (event_id, version, amount_cents) de eventos activos,
ordenada por event_id. Conserva tombstones al elegir la versión más reciente.
Rechaza conflictos de payload para una misma clave y versión con ValueError.
No omitas validaciones; puedes reutilizar pipeline.validate.

Evaluación manual: A=12000, C=7000, D=3000; B no debe aparecer.
Añade casos para claves compartidas por varias fuentes antes de generalizar.
"""


def reconstruct(batches):
    raise NotImplementedError("Implementa deduplicación, validación, versionado y tombstones")


if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
    from pipeline import batches
    assert reconstruct(batches()) == [("A", 2, 12000), ("C", 1, 7000), ("D", 1, 3000)]
    print("Caso base correcto; completa ahora los casos adversos indicados.")
