import streamlit as st
from data import run_query
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Analyse Géographique", layout="wide")

st.title("🌍 Analyse Géographique des Ventes Olist")
st.markdown(
    """
    Cette section analyse la performance commerciale selon la localisation des clients et des vendeurs.
    Nous examinons le chiffre d'affaires par État, le délai moyen de livraison, et les flux 
    entre régions du Brésil.
    """
)

st.markdown("---")

# ============================================================
# 🔹 1. Chiffre d'affaires par État (clients)
# ============================================================

st.subheader("📍 Chiffre d’affaires par État client")

df_state = run_query("""
SELECT 
    c.customer_state AS state,
    SUM(oi.price + oi.freight_value) AS revenue
FROM clean_order_items oi
JOIN clean_orders o ON oi.order_id = o.order_id
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status IN ('delivered','shipped','invoiced')
GROUP BY c.customer_state;
""")

fig_state = px.bar(
    df_state.sort_values("revenue", ascending=False),
    x="state", y="revenue",
    color="revenue",
    color_continuous_scale="Plasma",
    title="Chiffre d’affaires par État (clients)"
)
st.plotly_chart(fig_state, use_container_width=True)

st.markdown("---")

# ============================================================
# 🔹 2. Délai moyen de livraison par État
# ============================================================

st.subheader("⏱️ Délai moyen de livraison par État")

df_delay = run_query("""
SELECT 
    c.customer_state AS state,
    ROUND(AVG(
        JULIANDAY(o.order_delivered_customer_date) 
        - JULIANDAY(order_purchase_timestamp)
    ), 2) AS avg_delay
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status='delivered'
  AND o.order_delivered_customer_date IS NOT NULL
GROUP BY c.customer_state;
""")

fig_delay = px.bar(
    df_delay.sort_values("avg_delay", ascending=False),
    x="state", y="avg_delay",
    color="avg_delay",
    color_continuous_scale="Viridis",
    title="Délai moyen de livraison par État"
)
st.plotly_chart(fig_delay, use_container_width=True)

st.markdown("---")

# ============================================================
# 🔹 3. Flux vendeur → client (heatmap)
# ============================================================

st.subheader("🔄 Flux entre vendeurs et clients (Heatmap)")

df_flux = run_query("""
SELECT 
    s.seller_state AS seller_state,
    c.customer_state AS customer_state,
    COUNT(*) AS nb_orders
FROM clean_order_items coi
JOIN clean_sellers s ON coi.seller_id = s.seller_id
JOIN clean_orders o ON o.order_id = coi.order_id
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status='delivered'
GROUP BY s.seller_state, c.customer_state;
""")

pivot = df_flux.pivot_table(
    values="nb_orders", 
    index="seller_state", 
    columns="customer_state",
    fill_value=0
)

fig_heatmap = px.imshow(
    pivot,
    labels=dict(x="État client", y="État vendeur", color="Nb commandes"),
    title="Flux vendeur → client (nombre de commandes)"
)
st.plotly_chart(fig_heatmap, use_container_width=True)

st.markdown("---")

# ============================================================
# 🔹 4. Focus interactif : sélection d’un État
# ============================================================

st.subheader("🎯 Analyse détaillée d’un État")

all_states = sorted(set(df_state["state"]))

state_choice = st.selectbox("Sélectionnez un État client :", all_states)

df_focus = run_query(f"""
SELECT 
    s.seller_state,
    c.customer_state,
    COUNT(*) AS nb_orders,
    ROUND(AVG(
        JULIANDAY(o.order_delivered_customer_date) 
        - JULIANDAY(o.order_purchase_timestamp)
    ),2) AS avg_delay
FROM clean_order_items coi
JOIN clean_sellers s ON coi.seller_id = s.seller_id
JOIN clean_orders o ON o.order_id = coi.order_id
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status='delivered'
  AND c.customer_state = '{state_choice}'
GROUP BY s.seller_state;
""")

st.markdown(f"### 🔎 Flux vers l’État **{state_choice}**")

fig_focus = px.bar(
    df_focus.sort_values("nb_orders", ascending=False),
    x="seller_state", y="nb_orders",
    color="avg_delay",
    color_continuous_scale="Bluered",
    title=f"Commandes envoyées vers l’État {state_choice}"
)

st.plotly_chart(fig_focus, use_container_width=True)
