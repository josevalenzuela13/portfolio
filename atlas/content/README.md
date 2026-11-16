# Atlas: programa avanzado de autoestudio

40 unidades desarrolladas, 41 referencias, 40 ejercicios con solución y prácticas,
cinco calculadoras, cuatro laboratorios Python y proyectos por área e integrador.

## Archivos

- `index.html`: atlas introductorio y acceso al programa.
- `maestria.html`: contenido académico y herramientas locales.
- `laboratorios.py`: prácticas sintéticas con Python 3 y biblioteca estándar.
- `content/curriculum.json`: contenido estructurado para revisión y mantenimiento.
- `content/build_curriculum.py`: fuente generadora del programa y enlaces de entrada.

En Sites, los archivos web están en `dist/`; en GitHub Pages, en la carpeta `atlas/`.
El generador detecta ambos diseños. Desde la raíz del atlas:

```bash
python content/build_curriculum.py
python dist/laboratorios.py  # Sites
python laboratorios.py       # GitHub Pages
```

El generador conserva el atlas original y agrega enlaces al programa si faltan.
Las notas son originales y educativas. Los enlaces externos conservan derechos y
condiciones de sus titulares. No es una maestría acreditada ni otorga créditos.
Los ejemplos y datasets son sintéticos. El progreso se guarda en localStorage
del navegador, separado del seguimiento de lecturas del atlas inicial.

Edición: 2 de noviembre de 2026.

## Ruta de Ingeniería de Datos dentro de Ingeniería Analítica

Edición adicional: 16 noviembre 2026. Conserva las 40 unidades originales y
agrega 16 unidades DE-R, 168 horas orientativas, 19 fuentes dirigidas, 16 prácticas
con criterio de aceptación y dos proyectos integradores de crédito y salud.
Etiquetas: Base compartida AE+DE, Ingeniería de Datos y Profundización.
Los códigos DE-R evitan confundir esta ruta con Decision Engineering DE01–08.

- `ingenieria-datos.html`: ruta, búsqueda, filtros y progreso con evidencia local.
- `practicas-de/`: pipeline Python/SQLite, 14 pruebas, ejercicio, notebook/bundle
  Databricks, plantilla dbt y plantilla de CI.
- `practicas-ingenieria-datos.zip`: paquete de prácticas descargable.
- `content/data-engineering.json`: unidades y fuentes estructuradas.
- `content/build_data_engineering.py`: fuente editorial y generador idempotente.

```bash
python content/build_data_engineering.py
python -m unittest discover -s dist/practicas-de -v  # Sites
python -m unittest discover -s practicas-de -v       # GitHub Pages
```

El generador base vuelve a incorporar esta extensión al reconstruir el programa.
El progreso se guarda por navegador/dominio; exportación e importación permiten
trasladarlo. No se envía a GitHub ni implica acreditación de competencias.
Las pruebas locales fueron ejecutadas; Databricks/dbt requieren ejecución y
validación adicionales en entornos configurados por el estudiante.

## Idiomas: inglés profesional y alemán desde cero

- `idiomas.html`: 8 unidades de consolidación de inglés y 12 introductorias de
  alemán, 80 tarjetas, 40 comprobaciones cortas, temporizador y cuaderno local.
- `cuaderno-idiomas.md`: material descargable con tareas y modelos originales.
- `content/build_languages.py` y `content/languages.json`: fuente y datos.

```bash
python content/build_languages.py
```

El generador se reaplica tras reconstruir el programa y la ruta DE. Las voces
son síntesis opcional del navegador: requieren una voz compatible y no evalúan
pronunciación. Las notas y borradores se conservan por dominio/navegador y pueden
exportarse/importarse; no se envían a GitHub. El sitio no graba ni pide micrófono.
Las actividades son práctica de autoestudio y no acreditan un nivel CEFR.

## Rutina hasta diciembre 2027

- `rutina.html`, `routine.js`, `plan-core.js`: dashboard estático y lógica pura.
- `plan-aprendizaje.json`: 59 semanas y 881 sesiones, 16/11/2026 a 31/12/2027.
- `rutina-2026-2027.md`: plan completo legible sin JavaScript.
- `rutina-2026-2027.ics` y `rutina-minima-2026-2027.ics`: calendarios con alarmas.
- `tracking/`: configuración de avisos, semilla de progreso e instrucciones.
- `content/build_routine.py` y `content/routine_template.html`: generador y plantilla.

En el checkout de Sites, `github/` conserva archivos que se publican en la raíz
del repositorio GitHub: `.github/workflows/atlas-learning.yml`, `scripts/` y
`tests/`. No son parte de la carpeta estática dist. La rutina se reaplica al
regenerar las rutas previas. El generador no sobreescribe progreso/configuración
si esos archivos ya existen.

El cron requiere main y Actions permitido. Los recordatorios escriben Issues,
no commits a main. No utilizan SMTP, servicios pagos ni secretos personales.
No se promete entrega exacta a correo: depende de GitHub y sus notificaciones.
