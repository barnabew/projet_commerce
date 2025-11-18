from data import run_query,get_connexion,load_table
from textes import intro

query="""
SELECT 
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM clean_order_items oi
JOIN clean_orders o 
    ON oi.order_id = o.order_id
WHERE o.order_status IN ("delivered", "shipped", "invoiced");
"""

revenue_total = run_query(query)


query="""
SELECT 
    (SELECT SUM(price + freight_value) FROM olist_order_items_dataset) /
    (SELECT COUNT(DISTINCT order_id) FROM olist_orders_dataset) AS Panier_Moyen;
"""

panier_moyen = run_query(query)

query="""
SELECT 
    ROUND(AVG(
        JULIANDAY(order_delivered_customer_date) 
        - JULIANDAY(order_purchase_timestamp)
    ), 2) AS avg_delivery_time_days
FROM clean_orders
WHERE order_status = "delivered"
  AND order_delivered_customer_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL;
"""

delai_moyen = run_query(query)
pd.read_sql(query,conn)
