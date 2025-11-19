import streamlit as st
import pandas as pd
import plotly.express as px
from data import get_connection

st.title("📦 Analyse Produits – Olist")

st.write(
    "Cette page présente une analyse complète par catégorie de produits : "
    "performance commerciale, délais de livraison, et satisfaction client."
)

conn = get_connection()

# ==========================================
# 1️⃣ TOP CATEGORIES PAR CHIFFRE D'AFFAIRES
# ==========================================
st.header("🏆 Top catégories par chiffre d’affaires")

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

# ==========================================
# 2️⃣ DÉLAI MOYEN DE LIVRAISON PAR CATÉGORIE
# ==========================================
st.header("⏱️ Délai moyen de livraison par catégorie")

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

# ==========================================
# 3️⃣ NOTES MOYENNES PAR CATÉGORIE
# ==========================================
st.header("⭐ Satisfaction – Notes moyennes par catégorie")

min_reviews = st.slider("Min reviews par catégorie :", 20, 1000, 100)

query_reviews = f"""
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    ROUND(AVG(r.review_score), 2) AS avg_review_score,
