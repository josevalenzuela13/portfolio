from datetime import date,datetime,timedelta
import importlib.util
import json
from pathlib import Path
import unittest
from zoneinfo import ZoneInfo

BASE=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('reminders',BASE/'scripts/learning_reminders.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)


class Fake:
    def __init__(self, issues=None, comments=None):
        self.issues=issues or [];self.comments=comments or [];self.posts=[]
    def ensure_label(self): pass
    def pages(self,path):return self.comments if '/comments' in path else self.issues
    def request(self,method,path,payload=None):
        self.posts.append((method,path,payload))
        return {'html_url':'https://github.com/example/issue/1'}


class ReminderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):cls.plan=r.load_plan();cls.config=r.load_config()
    def issue(self,body='',state='open'):
        return dict(number=1,state=state,body=r.marker(self.plan,self.plan['weeks'][0])+'\n'+body)
    def test_plan_dates_and_unique_tasks(self):
        p=self.plan;self.assertEqual(len(p['weeks']),59)
        ids=[t['id'] for t in p['tasks']];self.assertEqual(len(ids),len(set(ids)))
        self.assertTrue(all(p['start']<=t['date']<=p['end'] for t in p['tasks']))
        self.assertEqual(min(t['date'] for t in p['tasks']),'2026-11-16')
        self.assertEqual(max(t['date'] for t in p['tasks']),'2027-12-31')
    def test_all_original_and_new_modules_referenced(self):
        p=self.plan;seen=set()
        for w in p['weeks']:seen.update([w['primary'],w['english'],w['german']]+w['related'])
        self.assertTrue(set(p['modules'])<=seen)
    def test_week_boundary_in_guatemala(self):
        self.assertEqual(r.choose_week(self.plan,date(2026,11,22))['number'],1)
        self.assertEqual(r.choose_week(self.plan,date(2026,11,23))['number'],2)
        # Martes 01:30 UTC es lunes 19:30 en Guatemala.
        d=datetime.fromisoformat('2026-11-17T01:30:00+00:00').astimezone(ZoneInfo('America/Guatemala'))
        self.assertEqual((d.weekday(),d.hour,d.minute),(0,19,30))
    def test_complete_week_budget(self):
        self.assertEqual(self.plan['weeks'][0]['normal_minutes'],540)
        self.assertEqual(self.plan['weeks'][0]['minimum_minutes'],270)
    def test_final_partial_week_no_january_tasks(self):
        w=self.plan['weeks'][-1]
        self.assertEqual(w['end'],'2027-12-31')
        self.assertLess(w['normal_minutes'],540)
    def test_creates_one_weekly_checklist(self):
        c=Fake();r.deliver(c,self.plan,self.config,date(2026,11,16))
        self.assertEqual(len(c.posts),1)
        self.assertEqual(c.posts[0][1],'/issues')
        self.assertIn('AT-2026-11-16-tech',c.posts[0][2]['body'])
        self.assertEqual(c.posts[0][2]['assignees'],['josevalenzuela13'])
    def test_same_day_not_sent_twice(self):
        c=Fake([self.issue('<!-- atlas-reminder:2026-11-16 -->')])
        r.deliver(c,self.plan,self.config,date(2026,11,16));self.assertEqual(c.posts,[])
    def test_existing_comment_deduplicates_retry(self):
        c=Fake([self.issue()],[{'body':'<!-- atlas-reminder:2026-11-16 -->'}])
        r.deliver(c,self.plan,self.config,date(2026,11,16));self.assertEqual(c.posts,[])
    def test_checked_sessions_not_reminded(self):
        body='\n'.join('- [x] `'+t['id']+'`' for t in self.plan['tasks'] if t['date']=='2026-11-16')
        c=Fake([self.issue(body)]);r.deliver(c,self.plan,self.config,date(2026,11,16));self.assertEqual(c.posts,[])
    def test_closed_issue_not_reopened(self):
        c=Fake([self.issue(state='closed')]);r.deliver(c,self.plan,self.config,date(2026,11,16));self.assertEqual(c.posts,[])
    def test_stops_at_end(self):
        c=Fake();r.deliver(c,self.plan,self.config,date(2028,1,1));self.assertEqual(c.posts,[])
    def test_disabled_means_no_posts(self):
        c=Fake();r.deliver(c,self.plan,dict(self.config,enabled=False),date(2026,11,16));self.assertEqual(c.posts,[])
    def test_new_recipient_rejected(self):
        with self.assertRaises(ValueError):r.deliver(Fake(),self.plan,dict(self.config,notify_user='someone-else'),date(2026,11,16))
    def test_issue_body_is_never_overwritten(self):
        c=Fake([self.issue('Mis notas y casillas editadas')]);r.deliver(c,self.plan,self.config,date(2026,11,17))
        self.assertEqual(len(c.posts),1);self.assertEqual(c.posts[0][1],'/issues/1/comments')
    def test_holiday_minimum_budget(self):
        week=self.plan['weeks'][5];self.assertEqual(r.mode_for(self.config,week),'minimum')
        self.assertTrue(all(t['minimum_minutes']>0 for t in r.week_tasks(self.plan,week,self.config)))


if __name__=='__main__':unittest.main()
