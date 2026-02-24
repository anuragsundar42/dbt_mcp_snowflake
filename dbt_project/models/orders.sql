select
  order_id,
  customer,
  amount,
  order_date
from {{ source('raw', 'raw_orders') }}