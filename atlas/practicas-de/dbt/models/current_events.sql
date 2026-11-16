with ranked as (
    select *, row_number() over (
        partition by event_id order by version desc
    ) as rn
    from {{ ref('stg_events') }}
)
select event_id, version, event_day, amount_cents, op
from ranked where rn = 1
