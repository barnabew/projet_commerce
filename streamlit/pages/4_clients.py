import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from data import run_query

st.set_page_config(page_title="Analyse Clients", layout="wide")

st.title("👥 Analyse des Clients")
st.markdown("""
Cette page se concentre uniquement sur les **clients Olist**, avec un focus particulier sur les  
**one-time buyers** (97% des clients).  
Objectif : comprendre les **leviers d’acquisition** plutôt que de la fidélisation.
""")

# --------------------------------------------------------------------
# 📌 1) KPI GLOBAUX
# --------------------------------------------------------------------

st.subheader("📊 Indicateurs clés")

# % one-time buyers
query_one_time = """
SELECT
    SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) AS one_time,
    COUNT(*) AS total
FROM (
    SELECT customer_unique_id, COUNT(*) AS cnt
    FROM clean_orders o
    JOIN clean_customers c ON o.customer_id = c.customer_id
    GROUP BY customer_unique_id
)
"""

one_time_df = run_query(query_one_time)
one_time = one_time_df["one_time"][0]
total = one_time_df["total"][0]
pct_one_time = round(one_time * 100 / total, 2)

# ticket moyen
query_ticket = """
SELECT
    ROUND(AVG(price + freight_value), 2) AS avg_item_value
FROM clean_order_items
"""
ticket_df = run_query(query_ticket)

# note moyenne
query_review = "SELECT ROUND(AVG(review_score), 2) AS avg_score FROM clean_reviews"
review_df = run_query(query_review)

col1, col2, col3 = st.columns(3)

col1.metric("🧍‍♂️ Clients one-time", f"{pct_one_time} %")
col2.metric("🛒 Panier moyen (article)", f"{ticket_df['avg_item_value'][0]} R$")
col3.metric("⭐ Note moyenne", review_df["avg_score"][0])

# --------------------------------------------------------------------
# 📌 2) Quels produits attirent le plus les nouveaux clients ?
# --------------------------------------------------------------------

st.header("🎯 Produits d’acquisition (premier achat)")

query_acquisition = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(*) AS first_order_count,
    ROUND(AVG(oi.price + oi.freight_value), 2) AS avg_basket
FROM clean_orders o
JOIN clean_order_items oi ON o.order_id = oi.order_id
JOIN clean_products cp ON oi.product_id = cp.product_id
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

df_acq = run_query(query_acquisition)

fig_acq = px.bar(
    df_acq,
    x="category",
    y="first_order_count",
    title="Top 15 des catégories qui attirent le plus de nouveaux clients",
)
fig_acq.update_layout(xaxis_title="Catégorie", yaxis_title="Nombre de clients")

st.plotly_chart(fig_acq, use_container_width=True)

# --------------------------------------------------------------------
# 📌 3) Quelles catégories génèrent les pires premières expériences ?
# --------------------------------------------------------------------

st.header("⚠️ Produits problématiques (mauvaises premières expériences)")

query_bad_first = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    COUNT(*) AS bad_first_reviews
FROM clean_orders o
JOIN clean_reviews r ON r.order_id = o.order_id
JOIN clean_order_items oi ON oi.order_id = o.order_id
JOIN clean_products cp ON cp.product_id = oi.product_id
LEFT JOIN product_category_name_translation tr 
       ON cp.product_category_name = tr.product_category_name
WHERE r.review_score <= 2
  AND o.customer_id IN (
      SELECT customer_id
      FROM clean_orders
      GROUP BY customer_id
      HAVING COUNT(*) = 1
  )
GROUP BY category
HAVING bad_first_reviews > 20
ORDER BY bad_first_reviews DESC
LIMIT 15;
"""

df_bad = run_query(query_bad_first)

fig_bad = px.bar(
    df_bad,
    x="category",
    y="bad_first_reviews",
    color="bad_first_reviews",
    title="Catégories causant le plus de mauvaises premières notes",
    color_continuous_scale="Reds",
)
fig_bad.update_layout(xaxis_title="Catégorie", yaxis_title="Bad Reviews (≤ 2)")

st.plotly_chart(fig_bad, use_container_width=True)

# --------------------------------------------------------------------
# 📌 4) Impact du délai de livraison sur les one-time buyers
# --------------------------------------------------------------------

st.header("⏱️ Impact du délai sur la satisfaction des nouveaux clients")

query_delay = """
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
AND o.order_purchase_timestamp IS NOT NULL
"""

df_delay = run_query(query_delay)

colA, colB = st.columns(2)
colA.metric("📦 Délai moyen (first-time)", f"{df_delay['avg_delivery_days'][0]} jours")
colB.metric("⭐ Note moyenne (first-time)", df_delay["avg_score"][0])

st.markdown("""
💡 *Les nouveaux clients sont extrêmement sensibles au délai de livraison.
Un délai élevé = risque majeur de non-retour.*
""")
