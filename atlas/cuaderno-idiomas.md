# Atlas · Inglés profesional y alemán desde cero

20 unidades, 80 frases y 40 comprobaciones breves. Programa de práctica, no certificación de nivel.

## Rutina
Cuatro sesiones semanales por idioma: tres de 20 minutos y una de 30. Ajusta duración y calendario. Registra un intento, una corrección y una frase nueva.

## EN01 · Contar tu trayectoria con claridad

Organiza tu presentación en presente, experiencia relevante y siguiente paso. Una lista de herramientas no explica tu aporte: conecta SQL, modelos y reglas con el problema que ayudaste a resolver. Distingue tu responsabilidad de la del equipo; “supported”, “coordinated” y “implemented” no son intercambiables.

Usa pasado simple para un proyecto terminado y presente perfecto para experiencia sin fecha cerrada. Elige dos hechos verificables de tu CV. Practica con palabras clave y cambia la formulación entre intentos para evitar memorizar un monólogo rígido.

### Modelos

- I work at the intersection of data, business rules and credit decisions. — Trabajo en la intersección de datos, reglas de negocio y decisiones crediticias.

- I have worked across banking, fintech and healthcare. — He trabajado en banca, fintech y salud.

- I helped standardize more than 40 business KPIs. — Ayudé a estandarizar más de 40 indicadores de negocio.

- I am now strengthening my data engineering skills. — Ahora estoy fortaleciendo mis habilidades de ingeniería de datos.


### Mi tarea
Graba fuera del sitio dos presentaciones de 90 segundos. En la segunda, elimina detalles que no expliquen el puesto que buscas.

### Evidencia
Incluye función actual, dos evidencias de tu CV y siguiente paso. Pide a alguien que pueda resumir tu perfil sin aclaraciones.

### Ejercicio
Corrige: I have worked in healthcare in 2022.

Respuesta orientativa: I worked in healthcare in 2022. Una fecha pasada cerrada pide pasado simple en este caso.

### Comprobaciones

- Completa: I ___ worked across several industries.
  Respuesta: have. I have worked…: experiencia acumulada sin fecha cerrada.

- Completa: Last year, I ___ a reporting project.
  Respuesta: supported. I supported…: periodo terminado y contribución específica.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN02 · Entrevistas con evidencia y honestidad

Estructura situación, tarea, acción y resultado, pero dedica más espacio a la acción que al contexto. Explica qué hiciste tú, qué decisión tomaste y cómo verificaste el resultado. Un resultado puede ser una regla documentada o una inconsistencia detectada; no necesitas inventar un porcentaje de mejora.

Prepara preguntas de seguimiento y reconoce límites. Si tu experiencia es de formación, dilo. Puedes describir lo que harías en producción sin presentarlo como algo ya desplegado. Hablar con precisión sobre tus límites resulta más informativo que repetir que sabes todas las herramientas.

### Modelos

- My responsibility was to clarify the business rules. — Mi responsabilidad era aclarar las reglas de negocio.

- I checked the output against the agreed definitions. — Comprobé el resultado contra las definiciones acordadas.

- The team delivered the solution; I focused on the data requirements. — El equipo entregó la solución; yo me enfoqué en los requisitos de datos.

- I have practised this in a project, but not yet in production. — He practicado esto en un proyecto, pero aún no en producción.


### Mi tarea
Prepara tres historias reales: ambigüedad en un KPI, colaboración difícil y un error del que aprendiste. Responde dos preguntas de seguimiento por historia.

### Evidencia
Cada historia distingue tu acción y la del equipo; todos los resultados son verificables y puedes explicar cómo se comprobaron.

### Ejercicio
¿Cómo respondes si te preguntan por una tecnología que no has operado en producción?

Respuesta orientativa: I have used it in a learning project, but I have not operated it in production yet. I can explain the design and the tests I ran.

### Comprobaciones

- Completa: My responsibility ___ to clarify the requirements.
  Respuesta: was. Responsabilidad en una situación pasada.

- Completa: I have not used it in production ___.
  Respuesta: yet. Yet encaja con algo que todavía no ha ocurrido.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN03 · Explicar pipelines y decisiones técnicas

Para explicar arquitectura, empieza por el consumidor y la necesidad. Describe fuente, transformación y salida; después introduce la decisión técnica y su alternativa. Usa conectores que hagan visible el razonamiento: “because”, “therefore”, “whereas” y “however”. No los uses como adorno: cada uno expresa una relación distinta.

Distingue precisión de jerga. Define idempotencia con una consecuencia observable: repetir el mismo lote no añade duplicados. Explica qué comprueba una prueba y qué deja fuera. Practica la misma explicación para un ingeniero y para alguien de negocio.

### Modelos

- The pipeline reads new files and validates the incoming records. — El pipeline lee archivos nuevos y valida los registros entrantes.

- We keep the deletion marker so that an older event cannot restore the record. — Conservamos el marcador de borrado para impedir que un evento anterior restaure el registro.

- I chose a batch approach because the report is updated daily. — Elegí procesamiento por lotes porque el informe se actualiza diariamente.

- The trade-off is lower complexity at the cost of higher latency. — La contrapartida es menor complejidad a costa de mayor latencia.


### Mi tarea
Explica durante dos minutos el pipeline de la ruta de Ingeniería de Datos. Haz otra versión de 45 segundos para un stakeholder no técnico.

### Evidencia
Defines una decisión, una alternativa, un supuesto y un límite. Otra persona entiende qué ocurre si llega un duplicado.

### Ejercicio
Explica idempotencia sin utilizar la palabra “idempotent”.

Respuesta orientativa: If we process the same batch again, the final data stays the same and no duplicate records are added.

### Comprobaciones

- Completa: We validate the data ___ publishing it.
  Respuesta: before. Before indica la secuencia de validación y publicación.

- Completa: I chose batch processing ___ the report is updated daily.
  Respuesta: because. Because introduce la razón.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN04 · Participar en reuniones sin quedarte callado

Participar no exige responder rápido a todo. Puedes comprobar una definición, pedir un ejemplo o resumir una decisión. Practica frases de entrada cortas para no esperar a tener una explicación perfecta. Si no entendiste, señala exactamente qué parte necesita aclaración.

Al discrepar, identifica la preocupación y propone una comprobación. En vez de una oposición vaga, plantea qué dato cambiaría tu opinión. Termina con responsable y siguiente paso. Esto conecta con tu experiencia de traducir requisitos: la claridad de una pregunta puede evitar una implementación equivocada.

### Modelos

- Could you clarify what counts as an approved application? — ¿Podrías aclarar qué cuenta como solicitud aprobada?

- If I understand correctly, the metric excludes cancelled applications. — Si entiendo bien, la métrica excluye solicitudes canceladas.

- My concern is that this join could duplicate the amounts. — Me preocupa que este join pueda duplicar los importes.

- Let us confirm the definition before changing the model. — Confirmemos la definición antes de cambiar el modelo.


### Mi tarea
Simula una reunión de cinco minutos sobre una métrica ambigua. Haz dos preguntas, presenta una objeción y cierra con el acuerdo.

### Evidencia
El cierre especifica definición, responsable y siguiente paso. Puedes pedir aclaración sin abandonar la conversación.

### Ejercicio
Convierte “I do not understand” en una pregunta específica sobre fecha de la métrica.

Respuesta orientativa: Could you clarify whether the metric uses the application date or the approval date?

### Comprobaciones

- Completa: Could you ___ the definition?
  Respuesta: clarify. Clarify = aclarar.

- Completa: My concern ___ that the totals may be duplicated.
  Respuesta: is. My concern is that… introduce una preocupación concreta.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN05 · Escribir correos y actualizaciones útiles

Un mensaje profesional suele necesitar objetivo, contexto mínimo y acción. Empieza por el resultado o bloqueo; añade evidencia y di qué necesitas del destinatario. Distingue una fecha comprometida de una estimación. Evita expresiones largas que oculten la petición.

Escribe primero una versión breve y revisa si contiene actor, acción y plazo. Después comprueba tiempos verbales y tono. Un texto formal no necesita sonar distante. No envíes automáticamente los borradores de esta práctica: trabaja con nombres y datos ficticios.

### Modelos

- The validation is complete, and the results match the source totals. — La validación terminó y los resultados coinciden con los totales de origen.

- We are waiting for confirmation of the business definition. — Esperamos confirmación de la definición de negocio.

- Could you review the proposed definition by Friday? — ¿Podrías revisar la definición propuesta antes del viernes?

- I will send an update once the checks are complete. — Enviaré una actualización cuando terminen las comprobaciones.


### Mi tarea
Escribe un correo de 100 palabras: un informe está bloqueado por una definición pendiente. Luego redúcelo a 60 sin perder la petición.

### Evidencia
El lector puede identificar qué está listo, qué falta, quién debe actuar y cuándo. Revisa claridad antes de revisar estilo.

### Ejercicio
Reescribe: I am writing this email in order to ask you if you could possibly check the definition.

Respuesta orientativa: Could you review the definition? Añade objeto y plazo cuando sean relevantes.

### Comprobaciones

- Completa: The results are consistent ___ the source data.
  Respuesta: with. Consistent with es la combinación habitual.

- Completa: Could you review this ___ Friday?
  Respuesta: by. By Friday establece un plazo límite.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN06 · Escuchar, tomar notas y responder

La comprensión útil consiste en extraer idea, evidencia, postura y acción, no en reconocer cada palabra. Escucha una vez para captar propósito y otra para localizar detalles. Usa la transcripción después de producir tus notas; así podrás distinguir un problema de vocabulario de uno de segmentación del habla.

Selecciona un fragmento de 30–60 segundos y practica shadowing tras entenderlo. No persigas un acento idéntico: busca ritmo inteligible, agrupación de ideas y énfasis. Para evaluar tu resumen, compara contenido y relaciones lógicas con el original.

### Modelos

- The speaker argues that the main issue is data quality. — La persona sostiene que el problema principal es la calidad del dato.

- The example supports the argument, but it does not prove causation. — El ejemplo apoya el argumento, pero no demuestra causalidad.

- I missed the last point. Could you repeat it? — No capté el último punto. ¿Podrías repetirlo?

- The next step is to agree on a shared definition. — El siguiente paso es acordar una definición compartida.


### Mi tarea
Elige una escucha C1 de la fuente enlazada. Anota idea, dos detalles y acción; consulta transcripción y corrige el resumen.

### Evidencia
Conservas primer intento y revisión. Identificas tres expresiones que no reconociste al escucharlas, aunque sí conocías por escrito.

### Ejercicio
¿Qué diferencia hay entre no conocer una palabra y no reconocerla al escucharla?

Respuesta orientativa: El primer caso pide aprender significado y uso; el segundo requiere trabajar sonido, enlace y contexto con un modelo audible.

### Comprobaciones

- Completa: Could you ___ the last point?
  Respuesta: repeat. Repeat solicita que se repita una parte.

- Completa: The speaker provides two ___ to support the claim.
  Respuesta: examples. Examples = ejemplos; respalda sin afirmar prueba causal.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN07 · Precisión gramatical y lenguaje natural

Lleva un registro breve de errores que realmente cometes. Clasifica tiempo verbal, preposición, elección de palabra y orden; corrige un patrón por semana. Una regla es útil cuando puedes reutilizarla en tres situaciones nuevas, no solo reconocer la respuesta de un ejercicio.

Después de “can” se usa la forma base: “I cannot believe it”. “Experience”, “information” y “advice” suelen ser incontables en estos usos: “some advice”, no “an advice”. Aprende colocaciones completas como “responsible for”, “experience with” y “apply for a role”. La revisión debe preservar tu voz y no convertir todo en frases genéricas.

### Modelos

- I still cannot believe it. — Todavía no puedo creerlo.

- I am responsible for coordinating the reporting work. — Soy responsable de coordinar el trabajo de reporting.

- I have experience with Databricks. — Tengo experiencia con Databricks.

- I would like some advice on my next step. — Me gustaría recibir orientación sobre mi siguiente paso.


### Mi tarea
Reúne diez frases tuyas de práctica, corrígelas y escribe una frase nueva por cada patrón. Vuelve a producirlas al día siguiente sin mirar.

### Evidencia
Puedes justificar cinco correcciones y reutilizarlas en mensajes nuevos. No dependes únicamente de una corrección automática.

### Ejercicio
Corrige: I can not believed it. / I need an advice.

Respuesta orientativa: I cannot believe it. / I need some advice. Después de can va la forma base; advice es incontable en este uso.

### Comprobaciones

- Completa: I still cannot ___ it.
  Respuesta: believe. Después de cannot se usa believe, no believed.

- Completa: I am responsible ___ data quality checks.
  Respuesta: for. Responsible for + sustantivo o forma -ing.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## EN08 · Defensa técnica y conversación espontánea

Combina presentación, explicación técnica, escucha y preguntas inesperadas. Hablar bien sobre una respuesta preparada no demuestra que puedas sostener una conversación. Pide a un compañero que cambie un requisito, cuestione una decisión o solicite una explicación más simple.

Mide progreso con muestras comparables: misma tarea al inicio y al final, tiempo disponible parecido y una rúbrica de claridad, precisión, interacción e inteligibilidad. La rapidez por sí sola no representa fluidez. Una revisión externa ayuda a detectar errores que ya no notas. El sitio organiza práctica; no asigna nivel CEFR ni sustituye evaluación de un docente.

### Modelos

- That is a fair question. Let me explain the assumption first. — Es una pregunta válida. Primero explicaré el supuesto.

- I would need to check that before giving a reliable answer. — Necesitaría comprobarlo antes de dar una respuesta fiable.

- If the latency requirement changed, I would reconsider the design. — Si cambiara el requisito de latencia, reconsideraría el diseño.

- What would success look like in the first three months? — ¿Cómo se definiría el éxito durante los primeros tres meses?


### Mi tarea
Realiza una entrevista simulada de 15 minutos: presentación, proyecto, incidente y preguntas propias. Pide tres observaciones concretas.

### Evidencia
Repites el diagnóstico de EN01, mejoras dos aspectos identificados y conservas una lista breve de próximos objetivos.

### Ejercicio
¿Qué respondes si necesitas comprobar un detalle técnico?

Respuesta orientativa: I would need to check the runtime documentation before confirming that behaviour. Reconoce el límite y especifica qué comprobarías.

### Comprobaciones

- Completa: If the requirements changed, I ___ reconsider the design.
  Respuesta: would. Hipótesis: if + pasado, would + forma base.

- Completa: Let me ___ the assumption first.
  Respuesta: explain. Let me + forma base.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU01 · Sonidos, alfabeto y primeras frases

Escucha el alfabeto alemán y practica tu nombre letra por letra. Las combinaciones no se leen como en español: “ei” suele sonar parecido a “ai”, “ie” representa una i larga y “eu/äu” se aproximan a “oi”. Son ayudas iniciales, no transcripciones exactas. Escucha ejemplos nativos para ä, ö, ü y las variantes de ch; no reemplaces sistemáticamente esos sonidos por vocales españolas.

Los sustantivos se escriben con mayúscula. Aprende una palabra con su artículo y plural cuando corresponda. Empieza por frases útiles para pedir repetición: te permiten participar incluso cuando tu vocabulario es pequeño.

### Modelos

- Hallo! Guten Tag! — ¡Hola! ¡Buen día!

- Wie schreibt man das? — ¿Cómo se escribe eso?

- Können Sie das bitte wiederholen? — ¿Puede repetirlo, por favor?

- Ich lerne Deutsch. — Estoy aprendiendo alemán.


### Mi tarea
Escucha un modelo de alfabeto en Goethe. Deletrea Andrés y cinco palabras; repite tres frases sin mirar el texto.

### Evidencia
Puedes deletrear tu nombre y pedir repetición. Compara tu voz con un modelo nativo; las aproximaciones españolas no bastan para evaluar pronunciación.

### Ejercicio
Traduce: Estoy aprendiendo alemán.

Respuesta orientativa: Ich lerne Deutsch.

### Comprobaciones

- Completa: Ich lerne ___.
  Respuesta: Deutsch. Deutsch designa el idioma y se escribe con mayúscula.

- Completa: Guten ___! (buen día)
  Respuesta: Tag. Guten Tag es un saludo cortés.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU02 · Presentarte y decir de dónde eres

En una oración declarativa principal sencilla el verbo conjugado ocupa la segunda posición. “Ich komme aus Guatemala” empieza con sujeto; “Heute lerne ich Deutsch” empieza con un complemento y coloca el sujeto después del verbo. Segunda posición no significa segunda palabra.

Aprende los pares ich bin / du bist / Sie sind, ich heiße / du heißt / Sie heißen. Sie con mayúscula es trato formal. Para procedencia usa “aus”; Guatemala puede aparecer sin artículo en estas frases. Practica pregunta y respuesta juntas para no quedarte solo con afirmaciones memorizadas.

### Modelos

- Ich heiße Andrés. — Me llamo Andrés.

- Ich komme aus Guatemala. — Soy de Guatemala.

- Ich bin Ingenieur. — Soy ingeniero.

- Wie heißen Sie? Woher kommen Sie? — ¿Cómo se llama? ¿De dónde es?


### Mi tarea
Presenta nombre, procedencia, profesión e idiomas en 30 segundos. Responde también en trato formal.

### Evidencia
Produces cuatro frases comprensibles y reconoces las preguntas equivalentes sin traducir palabra por palabra.

### Ejercicio
Ordena: aus Guatemala / komme / ich.

Respuesta orientativa: Ich komme aus Guatemala.

### Comprobaciones

- Completa: Ich ___ Andrés. (me llamo)
  Respuesta: heiße. Heiße; heisse se acepta como alternativa de teclado.

- Completa: Ich komme ___ Guatemala.
  Respuesta: aus. Aus expresa procedencia en este caso.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU03 · Preguntas, verbos regulares y trato formal

Muchos verbos regulares parten del infinitivo menos -en y usan terminaciones: ich lerne, du lernst, wir lernen, Sie lernen. Algunos verbos presentan cambios o ajustes; no conviertas el patrón en una regla sin excepciones. Aprende cada verbo con una frase.

En preguntas con palabra interrogativa, esta va primero y el verbo conjugado después: “Wo wohnen Sie?”. En preguntas sí/no, el verbo va al inicio: “Sprechen Sie Englisch?”. Distingue wo (dónde) y woher (de dónde). Practica siempre cambiar también la conjugación cuando cambies el pronombre.

### Modelos

- Wo wohnen Sie? — ¿Dónde vive?

- Ich wohne in Guatemala-Stadt. — Vivo en Ciudad de Guatemala.

- Sprechen Sie Englisch? — ¿Habla inglés?

- Ja, ich spreche Spanisch und Englisch. — Sí, hablo español e inglés.


### Mi tarea
Construye un diálogo de ocho turnos con nombre, residencia e idiomas. Alterna du y Sie sin mezclar conjugaciones.

### Evidencia
Puedes hacer cuatro preguntas y responderlas. Identificas por qué “Sprechen Sie…?” comienza con verbo.

### Ejercicio
Ordena: Sie / Englisch / sprechen / ?.

Respuesta orientativa: Sprechen Sie Englisch?

### Comprobaciones

- Completa: Wo ___ Sie? (vivir)
  Respuesta: wohnen. Sie formal usa wohnen.

- Completa: Ich ___ Deutsch. (aprender)
  Respuesta: lerne. Ich + lerne.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU04 · Artículos, plurales y objetos cotidianos

El género gramatical no se deduce de forma fiable del significado. Aprende der Termin, die Wohnung y das Zimmer como unidades, junto con sus plurales: Termine, Wohnungen y Zimmer. El artículo definido plural es die. Los patrones ayudan, pero no reemplazan aprender el sustantivo completo.

En nominativo usa ein para masculino y neutro y eine para femenino. “Das ist…” presenta algo; “Ich habe…” introduce una estructura que requiere acusativo y cambia el masculino a einen. Primero reconoce las diferencias en frases cortas antes de memorizar tablas extensas.

### Modelos

- Das ist ein Termin. — Eso es una cita.

- Das ist eine Wohnung. — Eso es una vivienda.

- Das ist ein Zimmer. — Eso es una habitación.

- Die Termine sind am Montag. — Las citas son el lunes.


### Mi tarea
Aprende diez objetos o lugares con artículo y plural. Describe cinco con “Das ist…” y comprueba el artículo.

### Evidencia
Recuerdas al menos ocho de los diez con artículo; corriges los restantes y los vuelves a recuperar otro día.

### Ejercicio
Completa el artículo de Wohnung y su plural.

Respuesta orientativa: die Wohnung; die Wohnungen.

### Comprobaciones

- Completa: Das ist ___ Wohnung.
  Respuesta: eine. Wohnung es femenino: eine.

- Completa: ___ Zimmer (la habitación).
  Respuesta: das. Das Zimmer es neutro.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU05 · Números, precios, fechas y horas

Practica primero 0–20 y las decenas. En 21–99 normalmente se dice unidad + und + decena: einundzwanzig. No inviertas automáticamente el orden al escribir cifras. Para precios escucha euros y centavos; repite para confirmar antes de actuar.

Para empezar usa hora formal: “um neun Uhr” y “um vierzehn Uhr dreißig”. Las expresiones coloquiales, como halb zehn, requieren atención: significan las nueve y media. Aprende am Montag y um neun Uhr como combinaciones. Usa números ficticios para practicar datos personales.

### Modelos

- Der Termin ist am Montag um neun Uhr. — La cita es el lunes a las nueve.

- Das kostet zwölf Euro. — Eso cuesta doce euros.

- einundzwanzig — veintiuno

- Können Sie die Nummer bitte wiederholen? — ¿Puede repetir el número, por favor?


### Mi tarea
Escucha y escribe diez números. Simula tres citas y confirma día y hora en voz alta.

### Evidencia
Aciertas ocho números y confirmas las tres citas; repasa lo que confundiste. Usa hora formal antes de añadir expresiones coloquiales.

### Ejercicio
¿Qué hora expresa halb zehn?

Respuesta orientativa: Las nueve y media: media hora antes de las diez.

### Comprobaciones

- Completa: Der Termin ist ___ Montag.
  Respuesta: am. Am + día de la semana.

- Completa: Der Termin ist ___ neun Uhr.
  Respuesta: um. Um + hora.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU06 · Pedir algo y expresar necesidades

“Ich möchte…” permite pedir de forma cortés. Si hay otro verbo, el infinitivo suele ir al final: “Ich möchte einen Termin vereinbaren”. Aprende también “Ich brauche…” y “Ich habe…”. En estas frases los objetos directos se construyen en acusativo.

El cambio más visible al empezar es masculino: ein Termin pasa a einen Termin. Femenino y neutro mantienen aquí eine Wohnung y ein Zimmer. Practica con objetos concretos. Para profesiones con sein, como “Ich bin Ingenieur”, esta no es la misma estructura de objeto directo.

### Modelos

- Ich möchte einen Kaffee, bitte. — Quisiera un café, por favor.

- Ich brauche einen Termin. — Necesito una cita.

- Ich habe eine Frage. — Tengo una pregunta.

- Ich möchte Deutsch lernen. — Quisiera aprender alemán.


### Mi tarea
Simula cafetería y recepción: dos peticiones por contexto y una pregunta de aclaración.

### Evidencia
Usas möchten con cortesía y distingues ein/einen en dos ejemplos masculinos.

### Ejercicio
Completa: Ich brauche ___ Termin.

Respuesta orientativa: Ich brauche einen Termin.

### Comprobaciones

- Completa: Ich ___ eine Frage.
  Respuesta: habe. Ich habe = tengo.

- Completa: Ich möchte einen Kaffee, ___.
  Respuesta: bitte. Bitte = por favor.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU07 · Negación y preferencias

Kein niega un sustantivo que en la afirmación tendría artículo indefinido o ninguno: “Ich habe kein Auto”. Cambia según género y caso: “keine Zeit”, “keinen Termin”. Nicht niega otras partes de la oración; su posición depende del foco. Empieza con modelos completos y cambia un elemento cada vez.

Gern expresa que disfrutas hacer algo: “Ich lese gern”. Mögen expresa gusto por algo; en esta etapa no necesitas dominar todas sus conjugaciones para comunicar una preferencia. Negar una frase no debe destruir su orden básico ni la conjugación.

### Modelos

- Ich habe kein Auto. — No tengo coche.

- Ich habe heute keine Zeit. — Hoy no tengo tiempo.

- Ich spreche noch nicht gut Deutsch. — Todavía no hablo bien alemán.

- Ich lese gern. — Me gusta leer.


### Mi tarea
Escribe cuatro frases afirmativas y sus negativas. Añade dos gustos y una actividad que no disfrutas.

### Evidencia
Explicas por qué usaste kein en un ejemplo y nicht en otro; revisa el orden con un modelo.

### Ejercicio
Niega: Ich habe ein Auto.

Respuesta orientativa: Ich habe kein Auto.

### Comprobaciones

- Completa: Ich habe ___ Zeit.
  Respuesta: keine. Die Zeit: keine Zeit.

- Completa: Ich lese ___. (me gusta leer)
  Respuesta: gern. Gern/gerne expresa gusto por la actividad.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU08 · Rutina y verbos separables

Describe hábitos con verbos frecuentes: arbeiten, lernen, lesen y beginnen. Algunos son irregulares; aprende una forma útil y amplía después. Si empiezas con un complemento de tiempo, el verbo principal sigue en segunda posición: “Am Abend lerne ich Deutsch”.

Los verbos separables como aufstehen separan el prefijo en estas oraciones: “Ich stehe um sieben Uhr auf”. Con un modal, el infinitivo queda junto al final: “Ich muss früh aufstehen”. Practica escuchar el final de la frase para no perder la información del prefijo.

### Modelos

- Ich arbeite mit Daten. — Trabajo con datos.

- Am Abend lerne ich Deutsch. — Por la noche estudio alemán.

- Ich stehe um sieben Uhr auf. — Me levanto a las siete.

- Am Wochenende lese ich gern. — El fin de semana me gusta leer.


### Mi tarea
Describe un día en seis frases y cambia dos de ellas para empezar por la hora o el momento del día.

### Evidencia
Mantienes el verbo conjugado en segunda posición y colocas el prefijo separable al final en el ejemplo practicado.

### Ejercicio
Ordena: am Abend / Deutsch / ich / lerne.

Respuesta orientativa: Am Abend lerne ich Deutsch.

### Comprobaciones

- Completa: Ich stehe um sieben Uhr ___.
  Respuesta: auf. Aufstehen separa auf en esta oración.

- Completa: Am Abend ___ ich Deutsch.
  Respuesta: lerne. El verbo va antes del sujeto cuando inicia Am Abend.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU09 · Moverte, preguntar y orientarte

Prioriza frases que permiten localizar un lugar y confirmar una indicación. Wo pregunta por ubicación y wohin por destino. No traduzcas cada preposición desde español: aprende secuencias como “zum Bahnhof” y revisa su estructura al avanzar.

En el nivel inicial puedes usar instrucciones y respuestas breves: links, rechts, geradeaus. Cuando no entiendas, pide que hablen más despacio. Reconocer esas palabras en un mapa es distinto de entenderlas al oído: combina ambas prácticas.

### Modelos

- Entschuldigung, wo ist der Bahnhof? — Disculpe, ¿dónde está la estación?

- Gehen Sie geradeaus und dann nach links. — Siga recto y después a la izquierda.

- Ich möchte zum Bahnhof. — Quiero ir a la estación.

- Bitte sprechen Sie langsamer. — Por favor, hable más despacio.


### Mi tarea
Dibuja un mapa pequeño y pide instrucciones para dos destinos. Escucha una respuesta sin mirar el mapa y verifica la ruta.

### Evidencia
Distingues izquierda/derecha/recto y puedes pedir repetición si te pierdes.

### Ejercicio
Traduce: Disculpe, ¿dónde está la estación?

Respuesta orientativa: Entschuldigung, wo ist der Bahnhof?

### Comprobaciones

- Completa: Wo ist der ___? (estación)
  Respuesta: Bahnhof. Der Bahnhof.

- Completa: Bitte sprechen Sie ___. (más despacio)
  Respuesta: langsamer. Langsamer = más despacio.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU10 · Vivienda, citas y comunicación cortés

Un mensaje inicial necesita saludo, motivo, datos relevantes y petición. Usa oraciones cortas y revisa verbo, artículo y mayúsculas. Para buscar vivienda puedes empezar con “Ich suche ein Zimmer” y preguntar por precio o visita; no necesitas una carta compleja.

Aprende expresiones como “Ich habe einen Termin” y “Ich kann am Montag kommen”. La cortesía también depende de contexto, tono y tratamiento. En estas prácticas usa información ficticia: el objetivo es construir un mensaje comprensible, no completar un trámite real.

### Modelos

- Ich suche ein Zimmer. — Busco una habitación.

- Wie hoch ist die Miete? — ¿De cuánto es el alquiler?

- Ist das Zimmer noch frei? — ¿Sigue disponible la habitación?

- Kann ich am Montag kommen? — ¿Puedo venir el lunes?


### Mi tarea
Escribe un mensaje de cinco frases para preguntar por una habitación y una posible visita. Revisa con los modelos.

### Evidencia
El mensaje indica interés, pregunta por disponibilidad y propone un momento; mantiene trato cortés y orden básico.

### Ejercicio
Escribe una pregunta para saber si una habitación sigue disponible.

Respuesta orientativa: Ist das Zimmer noch frei?

### Comprobaciones

- Completa: Ich suche ___ Zimmer.
  Respuesta: ein. Zimmer es neutro; aquí ein.

- Completa: Ist das Zimmer noch ___?
  Respuesta: frei. Frei = libre/disponible en este contexto.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU11 · Hablar de trabajo, estudio y capacidades

Los modales como können y müssen se conjugan y suelen colocar el otro verbo en infinitivo al final: “Ich kann Englisch sprechen”. Aprende ich kann / Sie können y ich muss / Sie müssen con ejemplos cortos. La negación de müssen no equivale a prohibición: “nicht müssen” expresa no tener obligación.

Para tu perfil basta empezar diciendo profesión, área e interés de estudio. No intentes traducir un CV técnico entero en A1. La meta es una presentación breve que puedas sostener y comprender cuando alguien te haga preguntas sencillas.

### Modelos

- Ich bin Ingenieur und arbeite mit Daten. — Soy ingeniero y trabajo con datos.

- Ich möchte in Deutschland studieren. — Quisiera estudiar en Alemania.

- Ich kann Englisch sprechen. — Puedo hablar inglés.

- Ich muss heute arbeiten. — Tengo que trabajar hoy.


### Mi tarea
Presenta tu trabajo en cinco frases sencillas. Añade una capacidad y algo que necesitas aprender.

### Evidencia
Conjugas el modal y dejas el infinitivo al final en tres ejemplos. Puedes explicar que se trata de una presentación inicial.

### Ejercicio
Ordena: Englisch / kann / sprechen / ich.

Respuesta orientativa: Ich kann Englisch sprechen.

### Comprobaciones

- Completa: Ich ___ Englisch sprechen. (puedo)
  Respuesta: kann. Ich kann + infinitivo al final.

- Completa: Ich muss heute ___. (trabajar)
  Respuesta: arbeiten. El verbo principal queda en infinitivo al final.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## DEU12 · Integración y siguiente paso hacia A1

Integra lo aprendido en situaciones breves: presentarte, preguntar una hora, pedir algo y escribir un mensaje. No confundas reconocer una frase con poder producirla y entender una respuesta nueva. Alterna cambios pequeños de persona, fecha, cantidad y lugar para comprobar transferencia.

A1 incluye más contenidos y práctica de lo que cabe en estas doce unidades. Usa el curso externo para ampliar temas y los materiales oficiales para detectar brechas. La autoevaluación del sitio no asigna nivel. Una revisión con docente o interlocutor competente ayuda especialmente con pronunciación e interacción.

### Modelos

- Ich heiße Andrés und komme aus Guatemala. — Me llamo Andrés y soy de Guatemala.

- Ich arbeite mit Daten und lerne Deutsch. — Trabajo con datos y estudio alemán.

- Können Sie mir bitte helfen? — ¿Puede ayudarme, por favor?

- Vielen Dank für Ihre Hilfe. — Muchas gracias por su ayuda.


### Mi tarea
Haz una conversación de tres minutos y escribe un mensaje de 40–60 palabras. Luego prueba una sección de escucha A1 oficial y registra dificultades.

### Evidencia
Puedes iniciar, pedir aclaración y cerrar una conversación breve. Conserva correcciones y selecciona los siguientes temas con un curso completo.

### Ejercicio
¿Qué falta para afirmar que completaste un nivel A1?

Respuesta orientativa: Una evaluación más amplia de comprensión, producción e interacción. Marcar doce unidades aquí no demuestra por sí solo ese nivel.

### Comprobaciones

- Completa: Vielen ___ für Ihre Hilfe.
  Respuesta: Dank. Vielen Dank = muchas gracias.

- Completa: Können Sie mir bitte ___? (ayudar)
  Respuesta: helfen. Können + infinitivo helfen.


### Mi intento y corrección

Escribe aquí: primer intento / corrección / frase nueva.

## Fuentes

- [British Council · C1 Listening](https://learnenglish.britishcouncil.org/free-resources/listening/c1) — Escucha entrevistas, reuniones y charlas; responde primero sin transcripción y compara después.

- [British Council · C1 Writing](https://learnenglish.britishcouncil.org/free-resources/writing/c1) — Estudia la estructura de un texto modelo y escribe después una versión con tu propio caso.

- [British Council · Podcasts for professionals](https://learnenglish.britishcouncil.org/free-resources/business/podcasts-professionals) — Refuerzo B2 de escucha profesional con transcripciones y ejercicios; sirve como puente si una actividad C1 resulta muy difícil.

- [Goethe-Institut · Practicar alemán](https://www.goethe.de/en/spr/ueb.html) — Busca alfabeto, presentación personal y ejercicios de nivel inicial; escucha el modelo antes de imitarlo.

- [Goethe-Institut · Material de práctica A1](https://www.goethe.de/en/spr/prf/ueb/pa1.html) — Más adelante, contrasta comprensión, lectura, escritura y conversación con los modelos oficiales. Completar Atlas no equivale a aprobar el examen.

- [vhs-Lernportal · A1](https://a1.vhs-lernportal.de/) — Curso externo para ampliar y practicar de forma sistemática. La información del proveedor indica uso gratuito; algunas funciones requieren registro propio.

- [Deutsche Welle · Nicos Weg, episodio inicial](https://www.youtube.com/watch?v=dC6ZGLzdaTs) — Vídeo oficial para comenzar con saludos. Mira un fragmento corto, anota lo que reconoces y repite después con el modelo.
