"""Recordatorios de Atlas mediante GitHub Issues. Solo biblioteca estándar.

No modifica archivos ni main, no utiliza SMTP y no necesita secretos personales.
GITHUB_TOKEN lo aporta Actions con permiso issues:write. Preview no usa red.
"""
import argparse
from datetime import date, datetime
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.parse
import urllib.request
from zoneinfo import ZoneInfo

LABEL = 'atlas-learning'
ROOT = Path(__file__).resolve().parents[1]
if (ROOT / 'atlas' / 'plan-aprendizaje.json').exists():
    PLAN_ROOT = ROOT / 'atlas'
else:  # Checkout de Sites: scripts se conservan bajo github/.
    PLAN_ROOT = ROOT.parent / 'dist'


def load_plan():
    return json.loads((PLAN_ROOT / 'plan-aprendizaje.json').read_text())


def load_config():
    return json.loads((PLAN_ROOT / 'tracking/reminders.json').read_text())


def choose_week(plan, today):
    value = today.isoformat()
    return next((w for w in plan['weeks'] if w['start'] <= value <= w['end']), None)


def marker(plan, week):
    return f'<!-- atlas-plan:{plan["id"]} week:{week["number"]} -->'


def mode_for(config, week):
    mode = config.get('mode', 'week_default')
    if mode not in ('normal', 'minimum', 'week_default'):
        raise ValueError('Modo de recordatorios no válido')
    return week['default_mode'] if mode == 'week_default' else mode


def week_tasks(plan, week, config):
    mode = mode_for(config, week)
    return [t for t in plan['tasks'] if t['week'] == week['number'] and t[mode + '_minutes'] > 0]


def checked_ids(body):
    return set(re.findall(r'^- \[[xX]\] `(AT-\d{4}-\d{2}-\d{2}-(?:tech|en|de|review|swim|strength|walk))`', body or '', re.M))


def body_for(plan, week, config):
    mode = mode_for(config, week)
    lines = [marker(plan, week), f'## Semana {week["number"]} · {week["title"]}',
             f'{week["start"]} — {week["end"]} · {plan["timezone"]} · modalidad {mode}',
             '', week['goal'], '', '**Evidencia de la semana:** ' + week['accept'], '',
             '[Abrir mi semana](' + plan['site_url'] + 'rutina.html#week=' + str(week['number']) + ')',
             '', 'Marca las casillas al terminar. El dashboard puede leerlas con “Cargar tracking de Issues”.',
             'Las notas aquí son públicas. No incluyas datos personales ni información de tu empresa.', '']
    for task in week_tasks(plan, week, config):
        minutes = task[mode + '_minutes']
        lines.append(f'- [ ] `{task["id"]}` {task["date"]} · {minutes} min · [{task["label"]}]({plan["site_url"] + task["url"]})')
    lines += ['', 'Cerrar este issue detiene sus recordatorios pendientes. Desmarca o anota una reprogramación cuando sea necesario; no marques todo como hecho por cerrarlo.']
    return '\n'.join(lines)


class GitHub:
    def __init__(self, repository, token):
        if not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository):
            raise ValueError('Repositorio inválido')
        if not token:
            raise ValueError('Falta GITHUB_TOKEN para modo send')
        self.base = 'https://api.github.com/repos/' + repository
        self.token = token

    def request(self, method, path, payload=None):
        data = json.dumps(payload).encode() if payload is not None else None
        req = urllib.request.Request(self.base + path, data=data, method=method,
                                    headers={'Authorization': 'Bearer ' + self.token,
                                             'Accept': 'application/vnd.github+json',
                                             'X-GitHub-Api-Version': '2022-11-28',
                                             'User-Agent': 'Atlas-learning-reminders',
                                             'Content-Type': 'application/json'})
        with urllib.request.urlopen(req, timeout=30) as response:
            return json.load(response)

    def pages(self, path):
        rows = []
        sep = '&' if '?' in path else '?'
        for page in range(1, 11):
            batch = self.request('GET', f'{path}{sep}per_page=100&page={page}')
            rows.extend(batch)
            if len(batch) < 100:
                return rows
        raise RuntimeError('Demasiadas páginas; revisar antes de enviar')

    def ensure_label(self):
        try:
            self.request('GET', '/labels/' + LABEL)
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise
            self.request('POST', '/labels', {'name': LABEL, 'color': '708A45',
                                            'description': 'Rutina de aprendizaje Atlas 2026-2027'})


def deliver(client, plan, config, today):
    """Máximo un aviso por fecha; conserva checklists editadas y no reabre issues."""
    week = choose_week(plan, today)
    if not config.get('enabled') or not week or today.isoformat() > config.get('end', plan['end']):
        return 'Sin envío: fuera de fechas o recordatorios desactivados.'
    user = config.get('notify_user', '')
    # La única cuenta destinataria configurada en esta edición es el propietario.
    if user != 'josevalenzuela13':
        raise ValueError('Destinatario distinto: revisar y autorizar antes de cambiarlo')
    client.ensure_label()
    tag = marker(plan, week)
    matches = [i for i in client.pages('/issues?state=all&labels=' + LABEL)
               if not i.get('pull_request') and tag in (i.get('body') or '')]
    daily = '<!-- atlas-reminder:' + today.isoformat() + ' -->'
    if not matches:
        issue_body = body_for(plan, week, config) + '\n\n' + daily + '\n@' + user + ' Tu checklist de esta semana está lista.'
        result = client.request('POST', '/issues', {
            'title': f'Atlas · Semana {week["number"]:02} · {week["title"]}',
            'body': issue_body, 'labels': [LABEL], 'assignees': [user]})
        return 'Checklist creada: ' + result['html_url']
    issue = min(matches, key=lambda x: x['number'])
    if issue['state'] == 'closed':
        return 'Sin envío: checklist cerrada por el usuario.'
    completed = checked_ids(issue.get('body'))
    pending = [t for t in week_tasks(plan, week, config)
               if t['date'] == today.isoformat() and t['id'] not in completed]
    if not pending:
        return 'Sin envío: no quedan sesiones pendientes hoy.'
    if daily in (issue.get('body') or ''):
        return 'Sin envío: esta fecha ya fue notificada.'
    if any(daily in (c.get('body') or '') for c in client.pages(f'/issues/{issue["number"]}/comments')):
        return 'Sin envío: esta fecha ya fue notificada.'
    mode = mode_for(config, week)
    lines = [daily, '@' + user + ' · Tu plan de hoy (' + today.isoformat() + ')', '']
    for t in pending:
        lines.append(f'- {t[mode + "_minutes"]} min · [{t["label"]}]({plan["site_url"] + t["url"]})')
    lines += ['', '[Abrir rutina](' + plan['site_url'] + 'rutina.html#week=' + str(week['number']) + ')',
              'Si hoy no cabe, usa la modalidad mínima y retoma sin duplicar la carga mañana.']
    client.request('POST', f'/issues/{issue["number"]}/comments', {'body': '\n'.join(lines)})
    return 'Recordatorio publicado en issue ' + str(issue['number'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--mode', choices=['preview', 'send'], default='preview')
    parser.add_argument('--date', help='Solo preview: YYYY-MM-DD para revisar un ejemplo')
    args = parser.parse_args()
    if args.date and args.mode != 'preview':
        parser.error('--date solo está permitido con --mode preview')
    plan, config = load_plan(), load_config()
    today = date.fromisoformat(args.date) if args.date else datetime.now(ZoneInfo(config['timezone'])).date()
    week = choose_week(plan, today)
    if args.mode == 'preview':
        print(body_for(plan, week, config) if week else 'Fecha fuera del plan: sin recordatorio.')
        return
    # Comprobar el límite ANTES de pedir credenciales o hacer llamadas.
    if not config.get('enabled') or not week or today.isoformat() > config.get('end', plan['end']):
        print('Sin envío: fuera del plan o desactivado.'); return
    client = GitHub(os.environ.get('GITHUB_REPOSITORY', plan['repository']), os.environ.get('GITHUB_TOKEN', ''))
    print(deliver(client, plan, config, today))


if __name__ == '__main__':
    main()
