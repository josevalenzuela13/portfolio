"""Plan fechado de Atlas. Fuente de semanas, sesiones, calendario y web."""
from pathlib import Path
from datetime import date,timedelta,datetime,timezone
from zoneinfo import ZoneInfo
import json,html
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'dist' if (ROOT/'dist').is_dir() else ROOT
START=date(2026,11,16);END=date(2027,12,31)
ZONE='America/Guatemala';BASE='https://josevalenzuela13.github.io/portfolio/atlas/'
E=html.escape
academic=json.loads((ROOT/'content/curriculum.json').read_text())
data=json.loads((ROOT/'content/data-engineering.json').read_text())
languages=json.loads((ROOT/'content/languages.json').read_text())
modules={m['id']:dict(m,url=('ingenieria-datos.html#' if m['id'].startswith('DE-R') else 'maestria.html#')+m['id']) for m in academic['modules']+data['modules']}
langmap={u['id']:dict(u,url='idiomas.html#'+u['id']) for u in languages['units']}
modules.update(langmap)
phases=[dict(id='base',title='Base técnica y pipelines',start=1,end=16,goal='SQL, Python, modelo temporal, ingesta, Delta, PySpark y dbt con pruebas.'),dict(id='operate',title='Operar y recuperar',start=17,end=26,goal='Jobs, CI/CD, contratos, permisos y observabilidad.'),dict(id='portfolio',title='Proyecto de crédito y defensa',start=27,end=30,goal='Una solución reproducible, un fallo reparado y una explicación en inglés.'),dict(id='depth',title='Streaming y cloud',start=31,end=34,goal='Profundización con límites y costos explícitos; opcional para la primera postulación.'),dict(id='decision',title='Ingeniería de decisiones',start=35,end=42,goal='Conectar datos con utilidad, optimización, causalidad y políticas ejecutables.'),dict(id='ai',title='Inteligencia artificial',start=43,end=50,goal='Baselines, evaluación honesta y una exploración guiada por unidad.'),dict(id='life',title='Ciencias de la vida',start=51,end=58,goal='Reutilizar la base en datos científicos y clínicos sintéticos.'),dict(id='close',title='Cierre y selección del siguiente paso',start=59,end=59,goal='Revisión de evidencias, repositorio y prioridades de 2028.')]
foundation={1:['F07'],3:['F08'],5:['F01'],7:['F02'],9:['F03'],11:['F04'],13:['F05'],15:['F06']}
bridges={1:['AE08'],2:['AE01'],3:['AE01'],4:['AE02','AE06'],5:['AE03'],6:['AE04'],7:['AE07'],8:['AE05'],9:['AE08'],10:['AE08'],11:['AE05'],12:['AE08'],13:['AE07']}
slots={0:[('tech',60,30,'19:30'),('de',15,10,'20:35')],1:[('en',20,15,'19:30'),('de',15,10,'19:55')],2:[('tech',60,30,'19:30'),('de',15,0,'20:35')],3:[('tech',60,30,'19:30'),('en',20,0,'20:35'),('de',15,10,'21:00')],4:[('de',15,10,'19:30')],5:[('tech',120,60,'09:00'),('de',15,0,'11:10')],6:[('tech',60,30,'16:00'),('en',20,15,'17:05'),('review',30,20,'17:30')]}
day_names=['Lunes','Martes','Miércoles','Jueves','Viernes','Sábado','Domingo']
weeks=[];tasks=[]
for n in range(1,60):
 a=START+timedelta(weeks=n-1);b=min(a+timedelta(days=6),END)
 phase=next(p for p in phases if p['start']<=n<=p['end'])
 if n<=26:
  idx=(n+1)//2;primary=f'DE-R{idx:02}';stage='Comprender e implementar' if n%2 else 'Probar y demostrar';title=modules[primary]['title'];related=bridges[idx]+foundation.get(n,[]);goal=modules[primary]['goals'] if 'goals' in modules[primary] else modules[primary]['goal'];accept=modules[primary]['accept']
 elif n<=30:
  primary='DE-R16';i=n-27;stage=['Diseñar el producto','Construir el recorrido completo','Provocar fallos y reparar','Revisar y defender'][i];title='Proyecto de crédito · '+stage;related=['AE02','AE03','AE05','AE08'];goal=['Define fuentes sintéticas, grano, contrato y baseline.','Implementa ingesta, transformación y Gold; conserva evidencia.','Agrega pruebas adversas, CI, reintento y reconciliación independiente.','Ejecuta desde cero, documenta límites y defiende en inglés.'][i];accept=['Diagrama, diccionario, datos sintéticos y criterios comprobables.','Producto ejecutable con métricas al grano correcto.','Fallo recuperado sin duplicación y pruebas que detectan un defecto.','README reproducible, tres decisiones justificadas y revisión externa.'][i]
 elif n<=34:
  idx=14 if n<=32 else 15;primary=f'DE-R{idx:02}';stage='Exploración' if n%2 else 'Contraste y límites';title=modules[primary]['title'];related=['AE04','AE07'] if idx==14 else ['AE08'];goal=modules[primary]['goal'];accept=modules[primary]['accept']
 elif n<=58:
  prefix,offset=('DE',34) if n<=42 else ('AI',42) if n<=50 else ('LS',50);primary=f'{prefix}{n-offset:02}';stage='Exploración guiada';title=modules[primary]['title'];related=['F03','F06'] if prefix=='DE' else ['F01','F04'] if prefix=='AI' else ['F04','F08'];goal=modules[primary]['goals'];accept='Ejercicio resuelto, ejemplo mínimo reproducible y una página que explique supuestos, resultado y limitación. La lectura extensa queda como ampliación.'
 else:
  primary='DE-R16';stage='Cierre parcial de cinco días';title='Revisión anual y siguiente especialización';related=['AI08','LS08','DE08'];goal='Selecciona evidencias que puedas explicar, cierra pendientes importantes y elige una prioridad de 2028.';accept='Índice del portafolio, balance de progreso y tres decisiones para continuar; no es necesario completar toda lectura optativa.'
 english=f'EN{min(8,(n+1)//2) if n<=16 else 1+((n-17)//4)%8:02}'
 german=f'DEU{min(12,(n+1)//2) if n<=24 else 1+(n-25)%12:02}'
 language_stage='Primer recorrido' if n<=24 else 'Consolidación A1 y escucha externa; no avanzar de nivel solo por fecha'
 light=n in (6,7,58,59)
 week=dict(number=n,id=f'W{n:02}',start=a.isoformat(),end=b.isoformat(),phase=phase['id'],title=title,primary=primary,stage=stage,goal=goal,accept=accept,related=related,english=english,german=german,language_stage=language_stage,default_mode='minimum' if light else 'normal',task_ids=[])
 tech_index=0
 for day in range((b-a).days+1):
  d=a+timedelta(days=day)
  for kind,normal,minimum,time in slots[day]:
   if kind=='tech':
    unit=primary
    if n<=26 or 31<=n<=34:
     odd=(n%2==1);prompts=(['Explica el objetivo y dibuja el flujo con sus supuestos.','Resuelve el ejercicio sin mirar; compara después la solución.','Implementa el primer paso de la práctica y agrega un caso límite.','Construye el siguiente paso y conserva entrada y salida.','Documenta decisiones; repasa el puente académico sin intentar agotar el texto.'] if odd else ['Reconstruye lo esencial sin copiar y corrige lo que no puedas explicar.','Introduce un fallo o dato adverso y comprueba su detección.','Compara el resultado con un baseline independiente.','Completa la práctica y demuestra su criterio de aceptación.','Redacta evidencia, límites y siguiente mejora; revisa lo aprendido.'])
    elif 27<=n<=30:prompts=['Revisa el objetivo del hito y define una comprobación.','Implementa una parte pequeña del hito actual.','Prueba una entrada adversa o una modificación de requisitos.','Integra, ejecuta y conserva evidencia del hito.','Documenta el resultado y prepara una explicación breve en inglés.']
    else:prompts=['Lee las notas y escribe tres conceptos y un supuesto.','Resuelve el ejercicio antes de abrir la respuesta.','Construye un ejemplo mínimo o simulación del laboratorio.','Contrasta el ejemplo con un baseline y registra resultados.','Escribe una página de lectura crítica y conecta con tu experiencia.']
    text=prompts[min(tech_index,4)];tech_index+=1
    if day==6 and related:text+=' Puente: '+', '.join(related)+'.'
    label='Técnica · '+modules[primary]['title']
   elif kind=='en':
    unit=english;label='Inglés · '+modules[english]['title'];text={1:'Escucha un recurso de la unidad, toma notas y resume sin transcripción.',3:'Practica las frases y explica en voz alta el tema técnico de esta semana.',6:'Escribe o graba un segundo intento; compara, corrige y guarda una evidencia.'}[day]
   elif kind=='de':
    unit=german;label='Alemán · '+modules[german]['title'];text={0:'Escucha un modelo humano y repite tres frases de la unidad.',1:'Recupera cinco frases o palabras sin mirar y cambia un dato.',2:'Lee la explicación y completa una comprobación con revisión.',3:'Escribe cinco frases propias con el patrón estudiado.',4:'Escucha de nuevo sin texto; identifica lo que ahora reconoces.',5:'Haz un diálogo breve o pide feedback; repasa los errores.'}[day]
   else:
    unit=primary;label='Revisión semanal';text='Registra minutos reales, evidencia y una dificultad. Elige un pendiente prioritario y adapta la siguiente semana; evita acumular deuda de estudio.'
   task=dict(id=f'AT-{d.isoformat()}-{kind}',date=d.isoformat(),week=n,kind=kind,unit=unit,label=label,instruction=text,url=modules[unit]['url'],normal_minutes=normal,minimum_minutes=minimum,time=time)
   tasks.append(task);week['task_ids'].append(task['id'])
 # End date is Friday: place the closing review within the actual plan range.
 if n==59:
  t=dict(id='AT-2027-12-31-review',date='2027-12-31',week=n,kind='review',unit=primary,label='Cierre de 2027',instruction=accept,url=modules[primary]['url'],normal_minutes=30,minimum_minutes=20,time='20:00');tasks.append(t);week['task_ids'].append(t['id'])
 week['normal_minutes']=sum(t['normal_minutes'] for t in tasks if t['week']==n)
 week['minimum_minutes']=sum(t['minimum_minutes'] for t in tasks if t['week']==n)
 weeks.append(week)
# Actividad física de 2027: sin asignar horas ni modificar el presupuesto académico.
activity=json.loads((ROOT/'content/activity.json').read_text())
for w in weeks:
 w['activity_normal_minutes']=0;w['activity_minimum_minutes']=0
 for day in range((date.fromisoformat(w['end'])-date.fromisoformat(w['start'])).days+1):
  d=date.fromisoformat(w['start'])+timedelta(days=day)
  if d.isoformat()<activity['start']:continue
  for item in activity['schedule']:
   if d.weekday() not in item['days']:continue
   t=dict(id=f'AT-{d.isoformat()}-{item["key"]}',date=d.isoformat(),week=w['number'],kind='activity',unit=None,label=item['label'],instruction=item['instruction'],url='rutina.html#actividad',normal_minutes=item['minutes'],minimum_minutes=item['minutes'],time=None)
   tasks.append(t);w['task_ids'].append(t['id'])
   w['activity_normal_minutes']+=item['minutes'];w['activity_minimum_minutes']+=item['minutes']
plan=dict(id='atlas-2026-2027-v1',version=1,start=START.isoformat(),end=END.isoformat(),timezone=ZONE,repository='josevalenzuela13/portfolio',site_url=BASE,phases=phases,weeks=weeks,tasks=tasks,modules={k:dict(id=k,title=m['title'],url=m['url']) for k,m in modules.items()})
(OUT/'plan-aprendizaje.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
# Seed files are never overwritten once user tracking/configuration exists.
(OUT/'tracking').mkdir(exist_ok=True)
for filename,content in [('progress.json',dict(program=plan['id'],version=1,entries={})),('reminders.json',dict(enabled=True,timezone=ZONE,notify_user='josevalenzuela13',mode='week_default',end=END.isoformat()))]:
 p=OUT/'tracking'/filename
 if not p.exists():p.write_text(json.dumps(content,ensure_ascii=False,indent=2)+'\n')

def escape_ics(s):return s.replace('\\','\\\\').replace('\n','\\n').replace(',','\\,').replace(';','\\;')
def fold(line):
 out=[];cur='';size=0
 for ch in line:
  n=len(ch.encode())
  if size+n>73:out.append(cur);cur=' '+ch;size=1+n
  else:cur+=ch;size+=n
 out.append(cur);return '\r\n'.join(out)
def calendar(mode='normal'):
 lines=['BEGIN:VCALENDAR','VERSION:2.0','PRODID:-//Atlas//Plan 2026-2027//ES','CALSCALE:GREGORIAN','X-WR-CALNAME:Atlas aprendizaje 2026-2027','X-WR-TIMEZONE:'+ZONE]
 for t in tasks:
  w=weeks[t['week']-1];use='minimum' if w['default_mode']=='minimum' else mode
  minutes=t[use+'_minutes']
  if not minutes:continue
  if t['kind']=='activity':
   d=date.fromisoformat(t['date'])
   lines.extend(['BEGIN:VEVENT','UID:'+t['id']+'@atlas-josevalenzuela13','DTSTAMP:20261116T120000Z','DTSTART;VALUE=DATE:'+d.strftime('%Y%m%d'),'DTEND;VALUE=DATE:'+(d+timedelta(days=1)).strftime('%Y%m%d'),'SUMMARY:'+escape_ics(t['label']),'DESCRIPTION:'+escape_ics(t['instruction']+'\nSin hora fija; duración prevista: '+str(minutes)+' min.\n'+BASE+t['url']),'END:VEVENT'])
   continue
  start=datetime.fromisoformat(t['date']+'T'+t['time']).replace(tzinfo=ZoneInfo(ZONE)).astimezone(timezone.utc)
  end=start+timedelta(minutes=minutes)
  lines.extend(['BEGIN:VEVENT','UID:'+t['id']+'@atlas-josevalenzuela13','DTSTAMP:20261116T120000Z','DTSTART:'+start.strftime('%Y%m%dT%H%M%SZ'),'DTEND:'+end.strftime('%Y%m%dT%H%M%SZ'),'SUMMARY:'+escape_ics(t['label']),'DESCRIPTION:'+escape_ics(t['instruction']+'\n'+BASE+'rutina.html#week='+str(t['week'])+'\nRecurso: '+BASE+t['url']),'BEGIN:VALARM','TRIGGER:-PT10M','ACTION:DISPLAY','DESCRIPTION:Atlas · sesión de aprendizaje','END:VALARM','END:VEVENT'])
 lines+=['END:VCALENDAR'];return '\r\n'.join(fold(x) for x in lines)+'\r\n'
(OUT/'rutina-2026-2027.ics').write_bytes(calendar().encode())
(OUT/'rutina-minima-2026-2027.ics').write_bytes(calendar('minimum').encode())
# An accessible text copy is versioned with the website.
md=['# Atlas · Rutina del 16 noviembre 2026 al 31 diciembre 2027\n','59 semanas. Semana normal: 6 h técnicas + 1 h inglés + 1 h 30 alemán + 30 min revisión = 9 h. Semana mínima: 3 h técnicas + 30 min inglés + 40 min alemán + 20 min revisión = 4 h 30. Semanas 6, 7, 58 y 59 ligeras. La última termina el viernes.\n','La primera prioridad es construir evidencia técnica antes de julio 2027. Las unidades F/AE son puentes de repaso; las semanas de decisiones, IA y ciencias de la vida son exploraciones guiadas, no dominio de toda su literatura. No se garantiza nivel de idioma por fecha.\n']
for w in weeks:
 md.extend([f'## Semana {w["number"]}: {w["start"]} — {w["end"]}\n',f'**{w["title"]} · {w["stage"]}**\n',w['goal']+'\n',f'Principal: [{w["primary"]}]({BASE+modules[w["primary"]]["url"]}). Inglés: {w["english"]}. Alemán: {w["german"]}. Puentes: {", ".join(w["related"])}.\n','Evidencia: '+w['accept']+'\n'])
 for t in [t for t in tasks if t['week']==w['number']]:md.append(f'- [ ] `{t["id"]}` {t["date"]} {t["time"] or "Sin hora fija"} · {t["normal_minutes"]} min / mínimo {t["minimum_minutes"]} · {t["label"]}. {t["instruction"]}\n')
(OUT/'rutina-2026-2027.md').write_text('\n'.join(md))
print(json.dumps(dict(weeks=len(weeks),tasks=len(tasks),start=plan['start'],end=plan['end'],normal_minutes=sum(w['normal_minutes'] for w in weeks))))
# Static shell + separately testable pure logic; data loaded from same origin.
style=(OUT/'maestria.html').read_text().split('<style>',1)[1].split('</style>',1)[0]
(OUT/'rutina.html').write_text((ROOT/'content/routine_template.html').read_text().replace('__STYLE__',style))
for filename in ['index.html','maestria.html','ingenieria-datos.html','idiomas.html']:
 p=OUT/filename;s=p.read_text()
 if 'data-routine-nav' not in s:s=s.replace('</nav>','<a data-routine-nav href="rutina.html">Mi rutina · hasta diciembre 2027</a></nav>',1)
 if filename=='index.html' and 'id="routine-entry"' not in s:
  entry='''<section id="routine-entry"><div class="section-no">09 / APRENDER CON CONSTANCIA</div><h2>Tu rutina hasta diciembre de 2027</h2><p>59 semanas con sesiones fechadas, materiales del Atlas, inglés, alemán, evidencias y seguimiento. Modalidad normal o mínima, calendario descargable y recordatorios con GitHub.</p><div class="actions"><a class="button" href="rutina.html">Abrir mi rutina →</a><a class="button alt" href="rutina.html#tracking">Guardar mi avance</a></div></section>'''
  s=s.replace('</main>',entry+'</main>',1)
 p.write_text(s)
