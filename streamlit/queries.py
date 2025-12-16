"""
Fichier centralisé contenant toutes les requêtes SQL du projet.
Organisation par thème : KPI, Graphiques
"""

# ===========================
# KPI GLOBAUX (Accueil)
# ===========================

QUERY_TOTAL_ORDERS = """
SELECT COUNT(DISTINCT order_id) AS c 
FROM clean_orders
"""

QUERY_PERCENT_5_STARS = """
SELECT ROUND(
    100.0 * SUM(CASE WHEN review_score = 5 THEN 1 ELSE 0 END) / COUNT(*), 
    1
) AS pct_5_stars
FROM clean_reviews
WHERE review_score IS NOT NULL
"""

QUERY_PERCENT_FAST_DELIVERY = """
SELECT ROUND(
    100.0 * SUM(CASE 
        WHEN JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp) < 7 
        THEN 1 ELSE 0 END
    ) / COUNT(*), 
    1
) AS pct_fast
FROM clean_orders 
WHERE order_status = 'delivered'
AND order_delivered_customer_date IS NOT NULL
AND order_purchase_timestamp IS NOT NULL
"""

QUERY_AVG_REVIEW_SCORE = """
SELECT ROUND(AVG(review_score), 2) AS avg 
FROM clean_reviews
"""

QUERY_AVG_DELIVERY_DELAY = """
SELECT ROUND(AVG(
    JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp)
), 2) AS delay
FROM clean_orders 
WHERE order_status = 'delivered'
"""

# ===========================
# GRAPHIQUES (Accueil)
# ===========================

QUERY_DELAY_VS_SATISFACTION = """
SELECT 
    r.review_score,
    ROUND(JULIANDAY(o.order_delivered_customer_date) - JULIANDAY(o.order_purchase_timestamp), 1) AS delivery_days
FROM clean_orders o
JOIN clean_reviews r ON o.order_id = r.order_id
WHERE o.order_delivered_customer_date IS NOT NULL
  AND o.order_purchase_timestamp IS NOT NULL
  AND r.review_score BETWEEN 1 AND 5
  AND JULIANDAY(o.order_delivered_customer_date) - JULIANDAY(o.order_purchase_timestamp) BETWEEN 0 AND 100;
"""

QUERY_STATES_METRICS = """
SELECT 
    c.customer_state AS state,
    COUNT(DISTINCT o.order_id) AS nb_orders,
    SUM(oi.price + oi.freight_value) AS revenue,
    ROUND(SUM(oi.price + oi.freight_value) * 1.0 
        / COUNT(DISTINCT o.order_id), 2) AS avg_order_value,
    ROUND(AVG(
        JULIANDAY(o.order_delivered_customer_date) 
        - JULIANDAY(o.order_purchase_timestamp)
    ), 2) AS avg_delivery_days,
    ROUND(AVG(r.review_score), 2) AS avg_review_score
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
JOIN clean_order_items oi ON oi.order_id = o.order_id
LEFT JOIN clean_reviews r ON r.order_id = o.order_id
WHERE o.order_status IN ('delivered', 'shipped', 'invoiced')
GROUP BY c.customer_state;
"""

QUERY_CATEGORIES_1_STAR = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(r.review_id) AS nb_reviews,
    ROUND(100.0 * SUM(CASE WHEN r.review_score = 1 THEN 1 ELSE 0 END) / COUNT(r.review_id), 1) AS pct_1_stars
FROM clean_reviews r
JOIN clean_orders o ON r.order_id = o.order_id
JOIN clean_order_items coi ON o.order_id = coi.order_id
JOIN clean_products cp ON coi.product_id = cp.product_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
WHERE o.order_status = 'delivered'
  AND r.review_score BETWEEN 1 AND 5
GROUP BY category
HAVING nb_reviews > 200
ORDER BY pct_1_stars DESC
LIMIT 10;
"""

QUERY_DELIVERY_DISTRIBUTION = """
SELECT 
    CASE 
        WHEN JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp) < 7 THEN '< 7 jours'
        WHEN JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp) < 14 THEN '7-14 jours'
        WHEN JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp) < 21 THEN '14-21 jours'
        WHEN JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp) < 30 THEN '21-30 jours'
        ELSE '> 30 jours'
    END AS delay_range,
    COUNT(*) AS nb_orders
FROM clean_orders
WHERE order_delivered_customer_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL
GROUP BY delay_range
ORDER BY 
    CASE delay_range
        WHEN '< 7 jours' THEN 1
        WHEN '7-14 jours' THEN 2
        WHEN '14-21 jours' THEN 3
        WHEN '21-30 jours' THEN 4
        WHEN '> 30 jours' THEN 5
    END;
"""
