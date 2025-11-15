query="""
SELECT 
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM clean_order_items oi
JOIN clean_orders o 
    ON oi.order_id = o.order_id
WHERE o.order_status IN ("delivered", "shipped", "invoiced");
"""

revenue_total = run_query(query)
