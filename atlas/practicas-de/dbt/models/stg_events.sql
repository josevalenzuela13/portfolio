-- Contrato didáctico: versiones enteras, claves no nulas y conflictos prohibidos.
select distinct event_id, version, cast(event_day as date) as event_day,
       amount_cents, op
from {{ ref('events') }}
