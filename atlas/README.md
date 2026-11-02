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
