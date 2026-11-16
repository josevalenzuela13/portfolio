select * from {{ ref('stg_events') }}
where event_id is null or version is null or version < 1
   or amount_cents is null or amount_cents < 0 or event_day is null
   or op is null or op not in ('UPSERT', 'DELETE')
