import streamlit as st
import pandas as pd
import plotly.express as px
from data import get_connection
import styles

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="produit")

st.markdown(styles.render_section_header("Analyse Produits"), unsafe_allow_html=True)

st.write(
    "Cette page présente une analyse complète par catégorie de produits : "
    "performance commerciale, délais de livraison, et satisfaction client."
)

conn = get_connection()

# Top catégories par chiffre d'affaires
st.header("Top catégories par chiffre d'affaires")

query_revenue = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    SUM(coi.price + coi.freight_value) AS revenue
FROM clean_order_items coi
JOIN clean_products cp ON coi.product_id = cp.product_id
JOIN clean_orders co ON coi.order_id = co.order_id
LEFT JOIN product_category_name_translation tr 
    ON cp.product_category_name = tr.product_category_name
WHERE co.order_status IN ("delivered", "shipped", "invoiced")
GROUP BY category
ORDER BY revenue DESC
LIMIT 15;
"""

df_revenue = pd.read_sql(query_revenue, conn)

fig = px.bar(
    df_revenue,
    x="revenue",
    y="category",
    orientation="h",
    title="Top 15 catégories – Chiffre d’affaires",
    labels={"revenue": "Revenue", "category": "Category"},
)
st.plotly_chart(fig, use_container_width=True)

# Délai moyen de livraison par catégorie
st.header("Délai moyen de livraison par catégorie")

min_sales = st.slider("Min ventes par catégorie :", 20, 500, 50)

query_delivery = f"""
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

df_delivery = pd.read_sql(query_delivery, conn)

fig = px.bar(
    df_delivery.head(15),
    x="avg_delivery_days",
    y="category",
    orientation="h",
    title="Catégories les plus lentes (top 15)",
)
st.plotly_chart(fig, use_container_width=True)

# Notes moyennes par catégorie
st.header("Satisfaction – Notes moyennes par catégorie")

min_reviews = st.slider("Min reviews par catégorie :", 20, 1000, 100)

query_reviews = f"""
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

df_reviews = pd.read_sql(query_reviews, conn)

fig = px.bar(
    df_reviews,
    x="avg_review_score",
    y="category",
    orientation="h",
    color="avg_review_score",
    color_continuous_scale="RdYlGn",
    title="Catégories les moins bien notées",
)
st.plotly_chart(fig, use_container_width=True)

# Catégories problématiques
st.header("Catégories problématiques")

query_bad = """
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

df_bad = pd.read_sql(query_bad, conn)

st.dataframe(df_bad)
