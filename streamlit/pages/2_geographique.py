import streamlit as st
from data import run_query
import plotly.express as px
import pandas as pd
import requests

st.set_page_config(page_title="Analyse Géographique", layout="wide")

st.title("🌍 Analyse Géographique des Ventes Olist")

# ============================================================
# 🔹 GEOJSON
# ============================================================

@st.cache_resource
def load_geojson():
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    return requests.get(url).json()

geojson = load_geojson()

# ============================================================
# 🔹 RÉCUPÉRATION DE TOUTES LES DONNÉES PAR ÉTAT
# ============================================================

query = """
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
        ROUND(AVG(r.review_score),2) AS avg_review_score
    FROM clean_orders o
    JOIN clean_customers c ON o.customer_id = c.customer_id
    JOIN clean_order_items oi ON oi.order_id = o.order_id
    LEFT JOIN clean_reviews r ON r.order_id = o.order_id
    WHERE o.order_status IN ('delivered','shipped','invoiced')
    GROUP BY c.customer_state;
"""

df_state = run_query(query)

# ============================================================
# 🔹 MENU DE L’ANALYSE À COLORER
# ============================================================

analysis_type = st.selectbox(
    "Sélectionnez l’analyse affichée sur la carte :",
    [
        "Chiffre d’affaires",
        "Délai moyen",
        "Nombre de commandes",
        "Panier moyen",
        "Note moyenne"
    ]
)

metric_map = {
    "Chiffre d’affaires": ("revenue", "Chiffre d’affaires (R$)"),
    "Délai moyen": ("avg_delivery_days", "Délai moyen (jours)"),
    "Nombre de commandes": ("nb_orders", "Nombre de commandes"),
    "Panier moyen": ("avg_order_value", "Panier moyen (R$)"),
    "Note moyenne": ("avg_review_score", "Note moyenne"),
}

metric_col, metric_title = metric_map[analysis_type]

# ============================================================
# 🔹 CARTE CHOROPLETH ENRICHIE
# ============================================================

fig = px.choropleth(
    df_state,
    geojson=geojson,
    locations="state",
    featureidkey="properties.sigla",
    color=metric_col,
    color_continuous_scale="Viridis",
    hover_data={
        "state": True,
        "nb_orders": True,
        "revenue": True,
        "avg_order_value": True,
        "avg_delivery_days": True,
        "avg_review_score": True,
        metric_col: True,
    },
    labels={
        "state": "État",
        "revenue": "CA (R$)",
        "nb_orders": "Nbre commandes",
        "avg_order_value": "Panier moyen",
        "avg_delivery_days": "Délai moyen",
        "avg_review_score": "Note moyenne"
    },
    title=f"{analysis_type} par État"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 🔹 TABLEAU DE L'ÉTAT SÉLECTIONNÉ
# ============================================================

st.markdown("---")
st.subheader("🔎 Analyse détaillée par État")

state_select = st.selectbox(
    "Choisissez un État :",
    sorted(df_state["state"].unique())
)

st.dataframe(df_state[df_state["state"] == state_select])
