import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import load_table, run_query

st.title("🧍 Analyse Clients")

st.markdown("""
Cette page présente une analyse complète des **comportements clients**,  
sans répéter les informations déjà visibles dans les autres pages.
""")

# ============================================================
# 1️⃣ Nombre de commandes par client
# ============================================================

st.header("📦 Comportement d'achat des clients")

query_freq = """
SELECT 
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS frequency
FROM clean_orders o
JOIN clean_customers c 
    ON o.customer_id = c.customer_id
WHERE o.order_status IN ("delivered", "shipped", "invoiced")
GROUP BY c.customer_unique_id;
"""

df_freq = run_query(query_freq)

col1, col2 = st.columns([2,1])

with col1:
    fig_freq = px.histogram(
        df_freq, x="frequency",
        nbins=10,
        title="Distribution du nombre de commandes par client"
    )
    st.plotly_chart(fig_freq, use_container_width=True)

with col2:
    one_shot = (df_freq["frequency"] == 1).mean() * 100
    multi = 100 - one_shot

    st.metric("Clients one-shot", f"{one_shot:.1f}%")
    st.metric("Clients récurrents", f"{multi:.1f}%")

st.markdown("👉 *La grande majorité des clients ne commandent qu'une seule fois.*")

# ============================================================
# 2️⃣ Dépense totale par client (Monetary)
# ============================================================

st.header("💰 Répartition des dépenses clients")

query_monetary = """
SELECT 
    c.customer_unique_id,
    SUM(oi.price + oi.freight_value) AS monetary
FROM clean_orders o
JOIN clean_customers c 
    ON o.customer_id = c.customer_id
JOIN clean_order_items oi
    ON o.order_id = oi.order_id
WHERE o.order_status IN ("delivered", "shipped", "invoiced")
GROUP BY c.customer_unique_id;
"""

df_m = run_query(query_monetary)
df_m["log_m"] = np.log1p(df_m["monetary"])

col1, col2 = st.columns([2,1])

with col1:
    fig_m = px.histogram(
        df_m, x="log_m",
        nbins=40,
        title="Distribution log(monetary)"
    )
    st.plotly_chart(fig_m, use_container_width=True)

with col2:
    top5p = df_m["monetary"].quantile(0.95)
    revenue_top5p = df_m[df_m["monetary"] >= top5p]["monetary"].sum()
    revenue_total = df_m["monetary"].sum()

    st.metric("Top 5% threshold", f"{top5p:.0f} R$")
    st.metric("Part du CA (Top 5%)", f"{(revenue_top5p/revenue_total)*100:.1f}%")

st.markdown("👉 *Les dépenses sont extrêmement concentrées : longue traîne marquée.*")

# ============================================================
# 3️⃣ Satisfaction ↔ Dépenses
# ============================================================

st.header("⭐ Satisfaction en fonction des dépenses")

query_review_m = """
SELECT 
    c.customer_unique_id,
    AVG(r.review_score) AS avg_score,
    SUM(oi.price + oi.freight_value) AS monetary
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
JOIN clean_order_items oi ON o.order_id = oi.order_id
JOIN clean_reviews r ON o.order_id = r.order_id
WHERE o.order_status = "delivered"
GROUP BY c.customer_unique_id
HAVING monetary > 0;
"""

df_rm = run_query(query_review_m)
df_rm["log_m"] = np.log1p(df_rm["monetary"])

fig_scatter = px.scatter(
    df_rm, x="log_m", y="avg_score",
    trendline="ols",
    opacity=0.4,
    title="Relation entre dépense et satisfaction",
)
st.plotly_chart(fig_scatter, use_container_width=True)

st.markdown("👉 *Aucune forte corrélation : les gros clients ne sont pas forcément plus satisfaits.*")

# ============================================================
# 4️⃣ Satisfaction ↔ Fidélité
# ============================================================

st.header("🔁 Satisfaction en fonction de la fidélité")

query_review_f = """
SELECT 
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS frequency,
    AVG(r.review_score) AS avg_score
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
JOIN clean_reviews r ON o.order_id = r.order_id
WHERE o.order_status = "delivered"
GROUP BY c.customer_unique_id;
"""

df_rf = run_query(query_review_f)

fig_box = px.box(
    df_rf, x="frequency", y="avg_score",
    title="Notes moyennes selon la fréquence d'achat"
)
st.plotly_chart(fig_box, use_container_width=True)

st.markdown("👉 *Les clients multi-achats ont tendance à donner des notes légèrement plus élevées.*")
