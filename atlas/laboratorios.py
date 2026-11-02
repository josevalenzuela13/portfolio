"""Atlas: cuatro laboratorios sintéticos. Python 3, solo biblioteca estándar.
Ejecutar: python laboratorios.py
No utiliza datos reales ni servicios externos. No es una implementación de producción.
"""
import math
import random
import sqlite3


def datos():
    """AE: demostrar un fan-out y preservar granularidad al agregar."""
    db = sqlite3.connect(":memory:")
    db.executescript("""
    CREATE TABLE lineas(factura INTEGER, importe REAL);
    CREATE TABLE pagos(factura INTEGER, importe REAL);
    INSERT INTO lineas VALUES (1, 10), (1, 20), (2, 40);
    INSERT INTO pagos VALUES (1, 15), (1, 15), (2, 40);
    """)
    incorrecto = db.execute("""
        SELECT l.factura, SUM(l.importe), SUM(p.importe)
        FROM lineas l JOIN pagos p USING (factura)
        GROUP BY l.factura
    """).fetchall()
    correcto = db.execute("""
        WITH l AS (
          SELECT factura, SUM(importe) facturado FROM lineas GROUP BY factura
        ), p AS (
          SELECT factura, SUM(importe) pagado FROM pagos GROUP BY factura
        )
        SELECT l.factura, l.facturado, COALESCE(p.pagado,0)
        FROM l LEFT JOIN p USING (factura) ORDER BY l.factura
    """).fetchall()
    print("\nAE | Join directo:", incorrecto)
    print("AE | Agregados a la misma granularidad:", correcto)
    print("En factura 1, cada suma incorrecta es 60; la correcta es 30.")
    db.close()
    # Extensión: añadir facturas sin pago y pagos sin factura.
    # ¿Qué población representa el LEFT JOIN? ¿Qué cambiaría con FULL JOIN?


def decisiones():
    """DE: enumerar una asignación entera y evaluar su sensibilidad."""
    def resolver(capacidad):
        factibles = [
            (3*x + 2*y, x, y)
            for x in range(3)
            for y in range(capacidad + 1)
            if x + y <= capacidad
        ]
        return max(factibles)

    print("\nDE | Objetivo 3x+2y; x<=2; x+y<=capacidad; enteros >=0")
    for capacidad in (3, 4, 5):
        valor, x, y = resolver(capacidad)
        print(f"Capacidad {capacidad}: x={x}, y={y}, valor={valor}")
    # Extensión: introducir incertidumbre de demanda y costo de faltantes.
    # Comparar políticas en escenarios de evaluación distintos del diseño.


def ciencias_vida():
    """LS: procedimiento BH; no equivale a un análisis ómico completo."""
    p = [0.001, 0.01, 0.04, 0.20]
    q = 0.05
    ordenados = sorted(enumerate(p), key=lambda par: par[1])
    m = len(p)
    k = max((r for r, (_, valor) in enumerate(ordenados, 1)
             if valor <= r*q/m), default=0)
    rechazados = [indice for indice, _ in ordenados[:k]]
    print("\nLS | BH con q=0.05; p=", p)
    print("Índices originales declarados (base 0):", rechazados)
    print("No interpretar q como probabilidad individual de error de cada gen.")
    # Extensión: simular muchas familias de hipótesis para estudiar FDR.
    # Mantener independencia o especificar la dependencia y sus implicaciones.


def inteligencia_artificial():
    """AI: logística básica, partición temporal y Brier fuera de muestra."""
    rng = random.Random(2026)

    def sigmoid(z):
        # Forma estable para evitar exp de magnitudes positivas muy grandes.
        if z >= 0:
            return 1 / (1 + math.exp(-z))
        ez = math.exp(z)
        return ez / (1 + ez)

    registros = []
    for t in range(1000):
        x = rng.gauss(0, 1)
        probabilidad = sigmoid(-0.5 + 1.2*x)
        y = int(rng.random() < probabilidad)
        registros.append((t, x, y))
    train, test = registros[:800], registros[800:]
    b, w = 0.0, 0.0
    for _ in range(1000):
        grad_b = grad_w = 0.0
        for _, x, y in train:
            error = sigmoid(b + w*x) - y
            grad_b += error
            grad_w += error*x
        b -= 0.1 * grad_b / len(train)
        w -= 0.1 * grad_w / len(train)
    prevalencia_train = sum(y for _, _, y in train) / len(train)
    brier_modelo = sum((sigmoid(b+w*x)-y)**2 for _, x, y in test) / len(test)
    brier_base = sum((prevalencia_train-y)**2 for _, _, y in test) / len(test)
    print(f"\nAI | Intercepto {b:.3f}; pendiente {w:.3f}")
    print(f"Brier test: modelo={brier_modelo:.4f}; baseline={brier_base:.4f}")
    print("No se ha usado test para ajustar ni seleccionar hiperparámetros.")
    # Extensión: cambiar la relación generadora en el último periodo.
    # Añadir intervalos por simulación y una gráfica de calibración.


if __name__ == "__main__":
    datos()
    decisiones()
    ciencias_vida()
    inteligencia_artificial()
