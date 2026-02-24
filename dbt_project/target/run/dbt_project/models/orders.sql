
  create or replace   view MCP_DBT_DATABASE.MCP_DATA.orders
  
  
  
  
  as (
    select
  order_id,
  customer,
  amount,
  order_date
from MCP_DBT_DATABASE.RAW.raw_orders
  );

