-- Un data test falla si devuelve alguna fila.
select event_id, version
from {{ ref('stg_events') }}
group by event_id, version having count(*) > 1
