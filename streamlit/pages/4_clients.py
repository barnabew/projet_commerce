import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from data import run_query
import styles

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="clients")

st.markdown("<div class='section-header'>Analyse Clients</div>", unsafe_allow_html=True)
st.markdown("""
Olist est un marketplace dominé par les **one-time buyers** (≈ 97%).  
L'objectif business n'est donc **pas la fidélisation**, mais la qualité de la **première expérience**.

Cette page analyse :
- les catégories qui **attirent** des nouveaux clients,
- celles qui **génèrent des mauvaises premières expériences**,
- l'impact du **délai de livraison** sur la satisfaction.
""")

# Indicateurs clés des clients
st.header("Indicateurs clés des clients")

query_kpi = """
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
df_kpi = run_query(query_kpi)

pct_one_time = round(df_kpi["one_time"][0] * 100 / df_kpi["total_clients"][0], 2)

query_ticket = "SELECT ROUND(AVG(price + freight_value), 2) AS avg_item FROM clean_order_items;"
avg_item = run_query(query_ticket)["avg_item"][0]

query_score = "SELECT ROUND(AVG(review_score), 2) AS avg_score FROM clean_reviews;"
avg_score = run_query(query_score)["avg_score"][0]

col1, col2, col3 = st.columns(3)
col1.metric("Clients one-time", f"{pct_one_time} %")
col2.metric("Panier moyen (par article)", f"{avg_item} R$")
col3.metric("Note moyenne", avg_score)

st.divider()

# Catégories qui attirent le plus de nouveaux clients
st.header("Catégories qui attirent le plus de nouveaux clients")

query_acquisition = """
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

df_acq = run_query(query_acquisition)

fig_acq = px.bar(
    df_acq,
    x="category",
    y="first_order_count",
    title="Top 15 catégories (premier achat)",
    labels={"first_order_count": "Nouveaux clients"}
)
fig_acq.update_layout(xaxis_title="Catégorie", yaxis_title="Nombre de nouveaux clients")

st.plotly_chart(fig_acq, use_container_width=True)

st.markdown("""
💡 *Ces catégories jouent un rôle clé dans l’acquisition : ce sont les produits les plus visibles, les plus attractifs ou les moins risqués.*
""")

st.divider()

# Catégories avec les pires premières expériences
st.header("Catégories avec les pires premières expériences")

query_bad_rate = """
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

df_bad = run_query(query_bad_rate)

fig_bad = px.bar(
    df_bad,
    x="category",
    y="bad_review_rate",
    color="bad_review_rate",
    color_continuous_scale="Reds",
    title="Taux de mauvaises reviews (first-time buyers)",
    labels={"bad_review_rate": "% Bad Reviews"}
)
fig_bad.update_layout(xaxis_title="Catégorie", yaxis_title="% Bad Reviews")

st.plotly_chart(fig_bad, use_container_width=True)

st.markdown("""
💡 *Une mauvaise première expérience = client perdu.  
Ces catégories nécessitent une action immédiate (qualité, logistique, description produit…)*  
""")

st.divider()

# Impact du délai sur la satisfaction
st.header("Impact du délai sur la satisfaction des nouveaux clients")

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
AND o.order_purchase_timestamp IS NOT NULL;
"""

df_delay = run_query(query_delay)

colA, colB = st.columns(2)
colA.metric("Délai moyen (first-time)", f"{df_delay['avg_delivery_days'][0]} jours")
colB.metric("Note moyenne (first-time)", df_delay['avg_score'][0])

st.markdown("""
💡 *Les nouveaux clients sont extrêmement sensibles au délai.  
Allonger la livraison augmente fortement le risque de non-retour.*  
""")

st.divider()

# Recommandations Business
st.header("Recommandations Business")

st.markdown("""
### ✔️ *1. Optimiser les catégories à fort taux de mauvaises reviews*  
Ce sont les produits qui font perdre le plus de clients dès le premier achat.

### ✔️ *2. Mettre en avant les catégories d’acquisition*  
Elles sont idéales pour publicité, SEO, campagnes d’accueil.

### ✔️ *3. Réduire les délais sur les premières commandes*  
Impact direct sur la satisfaction → augmente les chances de retour.

### ✔️ *4. Améliorer la transparence produit (photo, taille, description)*  
Souvent la vraie cause des bad reviews sur un premier achat.

### ✔️ *5. Ajouter un “suivi proactif” sur la première commande*  
Email, notifications → réduit l’anxiété → augmente la satisfaction.
""")
