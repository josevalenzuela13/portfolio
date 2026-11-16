select event_day, count(*) as events, sum(amount_cents) as total_cents
from {{ ref('current_events') }}
where op = 'UPSERT'
group by event_day
