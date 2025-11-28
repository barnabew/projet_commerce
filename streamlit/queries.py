"""
Fichier centralisé contenant toutes les requêtes SQL du projet.
Organisation par thème : KPI, Produits, Clients, Géographie
"""

# ===========================
# KPI GLOBAUX (Accueil) - Focus Expérience One-Shot
# ===========================

QUERY_TOTAL_REVENUE = """
SELECT SUM(price + freight_value) AS rev 
FROM clean_order_items
"""

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

QUERY_AVG_BASKET = """
SELECT ROUND(
    SUM(price + freight_value) * 1.0 / COUNT(DISTINCT order_id), 
    2
) AS avg_basket
FROM clean_order_items
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
# PRODUITS
# ===========================

QUERY_TOP_CATEGORIES_REVENUE = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    SUM(coi.price + coi.freight_value) AS revenue
FROM clean_order_items coi
JOIN clean_products cp ON coi.product_id = cp.product_id
JOIN clean_orders co ON coi.order_id = co.order_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
WHERE co.order_status IN ('delivered', 'shipped', 'invoiced')
GROUP BY category
ORDER BY revenue DESC
LIMIT 15;
"""

def get_query_delivery_by_category(min_sales):
    """Requête pour délais de livraison par catégorie avec filtre"""
    return f"""
    SELECT 
        COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
        ROUND(AVG(
            JULIANDAY(o.order_delivered_customer_date) 
            - JULIANDAY(o.order_purchase_timestamp)
        ), 2) AS avg_delivery_days,
        COUNT(*) AS total_sales
    FROM clean_orders o
    JOIN clean_order_items coi ON o.order_id = coi.order_id
    JOIN clean_products cp ON cp.product_id = coi.product_id
    LEFT JOIN product_category_name_translation tr 
        ON cp.product_category_name = tr.product_category_name
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
      AND o.order_purchase_timestamp IS NOT NULL
    GROUP BY category
    HAVING total_sales > {min_sales}
    ORDER BY avg_delivery_days DESC;
    """

def get_query_reviews_by_category(min_reviews):
    """Requête pour notes moyennes par catégorie avec filtre"""
    return f"""
    SELECT 
        COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
        ROUND(AVG(r.review_score), 2) AS avg_review_score,
        COUNT(r.review_id) AS nb_reviews
    FROM clean_reviews r
    JOIN clean_orders o ON r.order_id = o.order_id
    JOIN clean_order_items coi ON o.order_id = coi.order_id
    JOIN clean_products cp ON cp.product_id = coi.product_id
    LEFT JOIN product_category_name_translation tr 
        ON cp.product_category_name = tr.product_category_name
    WHERE r.review_score BETWEEN 1 AND 5
    GROUP BY category
    HAVING nb_reviews > {min_reviews}
    ORDER BY avg_review_score;
    """

QUERY_PROBLEMATIC_CATEGORIES = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(coi.order_id) AS nb_sales,
    ROUND(AVG(r.review_score), 2) AS avg_review_score
FROM clean_order_items coi
JOIN clean_orders o ON coi.order_id = o.order_id
JOIN clean_products cp ON coi.product_id = cp.product_id
JOIN clean_reviews r ON o.order_id = r.order_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
WHERE o.order_status = 'delivered'
GROUP BY category
HAVING nb_sales > 200
   AND avg_review_score < 3.8
ORDER BY nb_sales DESC;
"""

# ===========================
# CLIENTS
# ===========================

QUERY_CLIENT_KPI = """
SELECT
    SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) AS one_time,
    COUNT(*) AS total_clients
FROM (
    SELECT customer_unique_id, COUNT(*) AS cnt
    FROM clean_orders o
    JOIN clean_customers c ON o.customer_id = c.customer_id
    GROUP BY customer_unique_id
);
"""

QUERY_ACQUISITION_CATEGORIES = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(*) AS first_order_count,
    ROUND(AVG(oi.price + oi.freight_value), 2) AS avg_basket
FROM clean_orders o
JOIN clean_order_items oi ON o.order_id = oi.order_id
JOIN clean_products cp ON cp.product_id = oi.product_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
WHERE o.customer_id IN (
    SELECT customer_id
    FROM clean_orders
    GROUP BY customer_id
    HAVING COUNT(*) = 1
)
GROUP BY category
ORDER BY first_order_count DESC
LIMIT 15;
"""

QUERY_BAD_FIRST_EXPERIENCE = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(*) AS first_orders,
    SUM(CASE WHEN r.review_score <= 2 THEN 1 ELSE 0 END) AS bad_reviews,
    ROUND(
        SUM(CASE WHEN r.review_score <= 2 THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS bad_review_rate
FROM clean_orders o
JOIN clean_order_items oi ON o.order_id = oi.order_id
JOIN clean_products cp ON cp.product_id = oi.product_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
JOIN clean_reviews r ON r.order_id = o.order_id
WHERE o.customer_id IN (
    SELECT customer_id
    FROM clean_orders
    GROUP BY customer_id
    HAVING COUNT(*) = 1
)
GROUP BY category
HAVING first_orders > 50
ORDER BY bad_review_rate DESC
LIMIT 15;
"""

QUERY_DELAY_IMPACT_NEW_CLIENTS = """
SELECT
    ROUND(AVG(JULIANDAY(order_delivered_customer_date) 
        - JULIANDAY(order_purchase_timestamp)), 2) AS avg_delivery_days,
    ROUND(AVG(review_score), 2) AS avg_score,
    COUNT(*) AS nb_orders
FROM clean_orders o
JOIN clean_reviews r ON o.order_id = r.order_id
WHERE o.order_status = 'delivered'
AND o.customer_id IN (
    SELECT customer_id
    FROM clean_orders
    GROUP BY customer_id
    HAVING COUNT(*) = 1
)
AND o.order_delivered_customer_date IS NOT NULL
AND o.order_purchase_timestamp IS NOT NULL;
"""

# ===========================
# GÉOGRAPHIE
# ===========================

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

QUERY_GEOGRAPHIC_FLOWS = """
SELECT 
    s.seller_state,
    c.customer_state,
    COUNT(*) AS nb_orders
FROM clean_order_items coi
JOIN clean_sellers s ON coi.seller_id = s.seller_id
JOIN clean_orders o ON coi.order_id = o.order_id
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
  AND o.order_purchase_timestamp IS NOT NULL
GROUP BY s.seller_state, c.customer_state
HAVING nb_orders > 10
ORDER BY nb_orders DESC;
"""

# ===========================
# ACCUEIL - GRAPHIQUES
# ===========================

QUERY_MONTHLY_SALES = """
SELECT 
    strftime('%Y-%m', o.order_purchase_timestamp) AS month,
    COUNT(DISTINCT o.order_id) AS nb_orders,
    SUM(oi.price + oi.freight_value) AS revenue
FROM clean_orders o
JOIN clean_order_items oi ON o.order_id = oi.order_id
WHERE o.order_status IN ('delivered', 'shipped', 'invoiced')
  AND o.order_purchase_timestamp IS NOT NULL
GROUP BY month
ORDER BY month;
"""

QUERY_TOP_STATES_ORDERS = """
SELECT 
    c.customer_state AS state,
    COUNT(DISTINCT o.order_id) AS nb_orders
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status IN ('delivered', 'shipped', 'invoiced')
GROUP BY c.customer_state
ORDER BY nb_orders DESC
LIMIT 10;
"""

QUERY_TOP_CATEGORIES_SALES = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(DISTINCT coi.order_id) AS nb_sales
FROM clean_order_items coi
JOIN clean_products cp ON coi.product_id = cp.product_id
JOIN clean_orders co ON coi.order_id = co.order_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
WHERE co.order_status IN ('delivered', 'shipped', 'invoiced')
GROUP BY category
ORDER BY nb_sales DESC
LIMIT 10;
"""

QUERY_REVIEW_DISTRIBUTION = """
SELECT 
    review_score,
    COUNT(*) AS nb_reviews
FROM clean_reviews
WHERE review_score BETWEEN 1 AND 5
GROUP BY review_score
ORDER BY review_score;
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
