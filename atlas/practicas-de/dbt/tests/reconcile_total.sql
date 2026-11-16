-- Fixture sintético fijo: debe haber 19000 centavos activos.
select sum(total_cents) as total
from {{ ref('daily_credit') }}
having coalesce(sum(total_cents), 0) <> 19000
