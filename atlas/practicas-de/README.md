# Prácticas de Ingeniería de Datos · Atlas / Ingeniería Analítica

Ruta: `../ingenieria-datos.html`. Edición: 16 noviembre 2026.
Datos sintéticos. Entorno local: Python 3.10+, SQLite incluido; sin pip.

## Inicio local

```bash
cd practicas-de
python pipeline.py
python -m unittest -v
python pipeline.py --db practica.db
```

Resultado Gold: `2026-01-01: 2 eventos, 15000 centavos` y
`2026-01-02: 1 evento, 7000 centavos`; total 22000.
Reejecutar con la misma base no debe cambiar el resultado.

## Qué debes aprender y modificar

1. Lee el contrato de `validate`, las claves y los supuestos de `ingest`.
2. Implementa `ejercicios/reconstruir.py` sin copiar `ingest`; su
   NotImplementedError inicial es intencional. Se ejecuta por separado.
3. Añade SCD2 de segmentos con intervalos [inicio, fin) y pruebas de no solapamiento.
4. Simula API paginada, fallo antes de confirmar cursor y página repetida.
5. Añade checks de frescura con un reloj inyectado y logs por lote.
6. Explica por qué los tombstones evitan resucitar registros borrados.
7. Compara reconstrucción e incremental por clave/versión, no solo por total.

Las 14 pruebas incluidas comprueban duplicados, reintentos, conflictos, borrados,
rollback, secuencia de lotes, contratos y reconstrucción independiente. No
implementan SCD2, paginación real, streaming distribuido ni permisos cloud.

El contrato exige lotes contiguos por fuente, versiones crecientes por entidad,
UTC exacto y valores monetarios enteros. DELETE conserva el resto de campos en
este ejemplo; un CDC que entregue solo clave necesita otra normalización.
Los conflictos de clave/versión abortan el lote completo; errores de formato van
a cuarentena. Las escrituras y el checkpoint están en una transacción local.
No generalices esta atomicidad a varias tablas Delta o servicios externos.

## Databricks: no ejecutado en cloud desde Atlas

Archivos `databricks/pipeline_demo.py` y `databricks/databricks.yml`.
Necesitas CLI autenticada, catálogo de práctica y permisos para crear schema,
tablas y Jobs; el bundle presupone serverless para tareas notebook disponible.
Si no se admite, adapta cómputo con las opciones de tu workspace.

```bash
cd databricks
databricks bundle validate -t dev --var catalog=TU_CATALOGO
# Revisa recursos, permisos y costo antes de ejecutar:
databricks bundle deploy -t dev --var catalog=TU_CATALOGO
databricks bundle run -t dev credit_demo --var catalog=TU_CATALOGO
```

O importa el notebook y configura widgets catalog/schema/stage. La preparación
reemplaza `bronze_demo` del schema elegido: usa uno exclusivo de práctica.
El ejemplo cloud tiene total 19000 (A=12000, C=7000); no contiene D de la
práctica local. `silver_demo` conserva B borrado. Prueba dos ejecuciones,
fallo controlado y reparación; guarda historial y comparación. El código no
implementa una ingesta real de Auto Loader ni SCD2: son ampliaciones guiadas.
No asumas validación completa del bundle hasta ejecutar CLI contra tu entorno.

## dbt: plantilla PostgreSQL, no ejecutada contra una base desde Atlas

Crea un entorno virtual y una base PostgreSQL de práctica con un rol propio.
Instala versiones compatibles de dbt-core y dbt-postgres. Registra versiones
exactas con `python -m pip freeze > requirements-lock.txt` tras comprobarlas.
Copia `profiles.example.yml` como `profiles.yml` en una carpeta FUERA del repo.
Configura DBT_HOST, DBT_USER, DBT_PASSWORD y DBT_DATABASE mediante tu gestor de
entorno; nunca los incluyas en commits ni capturas públicas.

```bash
cd dbt
dbt debug --profiles-dir RUTA_PERFILES
dbt seed --profiles-dir RUTA_PERFILES
dbt build --profiles-dir RUTA_PERFILES
dbt docs generate --profiles-dir RUTA_PERFILES
```

La sintaxis `data_tests` requiere una versión compatible de dbt. Los modelos
son vistas para facilitar un baseline; no se presentan como incrementales.
El total esperado del seed es 19000. Las pruebas impiden conflictos de versión,
claves repetidas, valores inválidos y un total distinto al fixture.
La ampliación consiste en implementar incremental con `unique_key`, estrategia
compatible y correcciones tardías, y comparar contra este baseline.

## CI

`workflow.example.yml` es una plantilla: cópiala a `.github/workflows/` en tu
repo de práctica y adapta la ruta. No se instala automáticamente en tu portfolio.
Ejecuta solo las pruebas locales; autenticar y desplegar cloud es otra etapa.

## Evidencias sugeridas

`evidencias/DE-Rxx/`: README del caso, comandos, entrada, resultado esperado,
resultado observado, prueba de fallo, commit y límites. Para cada práctica,
explica qué implementaste tú y qué proviene de la solución de referencia.
El ZIP no contiene perfiles personales, credenciales ni datos del usuario.
