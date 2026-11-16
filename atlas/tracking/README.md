# Atlas · seguimiento y recordatorios (2026–2027)

## Qué existe y qué requiere activación

La web tiene 59 semanas y 881 sesiones fechadas entre el 16/11/2026 y el
31/12/2027 (Guatemala). Un registro de sesión no certifica dominio de la unidad.
El programa normal suma 9 h por semana completa. El mínimo suma 4 h 30 y reduce
alcance. Semanas 6, 7, 58 y 59 son ligeras; la última termina el viernes.

El cron solo funciona cuando `.github/workflows/atlas-learning.yml` está en la
rama predeterminada y Actions está habilitado. Un PR abierto no lo activa.
Los horarios iniciales son lunes–viernes 19:30, sábado 09:00, domingo 16:00,
Guatemala. El calendario ICS puede ajustarse en la web, independientemente del
cron. Para cambiar los avisos hay que editar los cron UTC del workflow y revisar
el cálculo de fechas. Guatemala es UTC-6, sin horario de verano.

## Progreso local y copia en Git

1. Marca sesiones, minutos reales, evidencia y nota en `rutina.html`.
2. Exporta `progress.json` al terminar la semana.
3. En GitHub abre `atlas/tracking/progress.json`, pulsa Edit y reemplaza el
   contenido por el JSON exportado; guarda el cambio. Es un paso manual.
4. Desde otro navegador, “Cargar copia del repositorio” lee la versión publicada
   después del despliegue de Pages. También puedes importar el archivo local.

No se guarda un token en la web. Las notas y minutos no se envían automáticamente.
El repositorio es público: evita información de clientes, empresa o datos
personales que no quieras publicar. Exporta antes de borrar datos del navegador.
La importación combina sesiones y conserva la más reciente según updatedAt;
las reseñas presentes en el archivo reemplazan sus versiones locales.

## Checklists persistentes sin guardar archivos manualmente

El workflow crea un issue por semana con etiqueta `atlas-learning` y casillas
con IDs estables de las sesiones. Marca allí las tareas desde cualquier equipo.
La web las lee con “Cargar tracking de Issues”, sin autenticación para este
repositorio público. Por defecto conserva los registros ya editados localmente;
puedes elegir usar estados de GitHub más recientes. Notas y minutos locales se
conservan. La API pública tiene límites; no se consulta continuamente.

Cerrar el issue detiene sus avisos pero NO significa que todas sus sesiones estén
hechas. El bot no reescribe ni borra tu checklist, no reabre un issue cerrado y
no agrega el mismo aviso de fecha dos veces. Usa las casillas para el tracking.
Los minutos detallados y las notas se conservan en Git solo mediante el JSON.

## Activar notificaciones

1. Fusiona el PR que incorpora el workflow.
2. Abre Actions → “Atlas · recordatorios de aprendizaje” → Run workflow.
3. Usa `preview` para revisar sin enviar; `send` crea la checklist o el aviso del
   día actual. No es posible enviar para una fecha ficticia.
4. Revisa tus ajustes de notificaciones para participación, asignaciones y
   menciones. Selecciona email/On GitHub y configura el móvil si lo deseas.
5. Comprueba primero la creación del issue y luego la entrega real a tu canal.

El workflow usa GITHUB_TOKEN efímero, con contents:read e issues:write, y solo
notifica a `josevalenzuela13`. No necesita un secreto SMTP ni token personal.
El script no modifica main ni otros archivos y no usa servicios de pago.

## Pausar, retomar y cerrar

- Para pausar todos los avisos: `enabled: false` en reminders.json o deshabilita
  el workflow en Actions. Para retomar: vuelve a true o habilítalo.
- `mode: week_default` aplica la modalidad sugerida por semana. Puedes elegir
  `minimum` o `normal` para los recordatorios. El selector de la web es local y
  no cambia este archivo ni el cron.
- El script no envía después del 31/12/2027; el cron puede seguir ejecutando
  comprobaciones sin avisar hasta deshabilitarlo.
- GitHub puede retrasar o descartar cron y deshabilitarlo tras 60 días sin
  actividad en un repo público. Revisa Actions periódicamente.
- Standard runners en repos públicos son gratuitos según la documentación
  consultada el 16/11/2026. Si cambias visibilidad, revisa facturación y cuotas.

## Calendario

Importa ICS en un calendario separado y revisa zona horaria, alarmas y primeras
fechas. Cada evento incluye alarma 10 min antes y enlace al material. La app de
calendario decide si respeta las alarmas; el sitio no puede verificarlo.
El archivo no se actualiza automáticamente. Para sustituirlo, elimina/reemplaza
el calendario importado y evita duplicados. Los UID de las sesiones son estables.
Puedes exportar solo una semana o un tipo de sesión desde la web.

## Probar el código desde GitHub

```bash
python -m unittest discover -s tests -p test_learning_reminders.py -v
node --test tests/plan-core.test.cjs
python scripts/learning_reminders.py --mode preview --date 2026-11-16
```

Las pruebas de recordatorios usan un cliente falso y no envían notificaciones.
La validación local no demuestra entrega real del correo: compruébala al activar.

## Fuentes

- https://docs.github.com/en/actions/concepts/billing-and-usage
- https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows
- https://docs.github.com/en/subscriptions-and-notifications/get-started/configuring-notifications
- https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api

## Actividad física integrada · 2027

Desde el 01/01/2027, `content/activity.json` agrega natación lunes–jueves (30 min), fuerza lunes y viernes (40 min, clase o kettlebell) y caminata sábado (60 min). El sábado puede sustituir al viernes; no se agrega como tercera sesión obligatoria. Las horas de entrenamiento no se han acordado: no se inventan ni se desplazan con el horario de estudio. Los ICS usan eventos de día completo sin alarma para ejercicio.

Ejecuta `python atlas/content/build_routine.py` desde la raíz del repositorio para regenerar el plan y sus archivos. Los presupuestos de estudio se conservan; `activity_normal_minutes` y `activity_minimum_minutes` registran el ejercicio por separado. La modalidad mínima reduce el estudio, no prescribe una reducción automática del ejercicio.

El mismo workflow y los mismos horarios de aviso incluyen las sesiones físicas pendientes. Las casillas de IDs swim/strength/walk se reconocen en el bot y en la lectura de Issues del sitio. Esto no convierte la web en un editor de Issues ni automatiza las notas o minutos. No se necesita una tarea nueva en ChatGPT. Las semanas anteriores a enero quedan sin cambios de actividad.
