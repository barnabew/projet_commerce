import streamlit as st
from data import run_query
import plotly.express as px
import pandas as pd
import requests
import json

st.set_page_config(page_title="Analyse Géographique", layout="wide")

st.title("🌍 Analyse Géographique des Ventes Olist")
st.markdown(
    """
    Cette page permet d'explorer les performances commerciales selon les régions du Brésil :
    chiffre d'affaires, délais de livraison, satisfaction client et volume de commandes.
    """
)

st.markdown("---")

# ============================================================
# 🔹 CHARGEMENT DU GEOJSON DES ÉTATS DU BRÉSIL
# ============================================================

@st.cache_resource
def load_geojson():
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    return requests.get(url).json()

geojson = load_geojson()

# ============================================================
# 🔹 MENU DE SÉLECTION DE L’ANALYSE
# ============================================================

analysis_type = st.selectbox(
    "Sélectionnez l’analyse à afficher :",
    [
        "Chiffre d’affaires",
        "Délai moyen de livraison",
        "Nombre de commandes",
        "Note moyenne"
    ]
)

# ============================================================
# 🔹 REQUÊTES SQL SELON L’ANALYSE
# ============================================================

if analysis_type == "Chiffre d’affaires":
    query = """
        SELECT 
            c.customer_state AS state,
            SUM(oi.price + oi.freight_value) AS value
        FROM clean_order_items oi
        JOIN clean_orders o ON oi.order_id = o.order_id
        JOIN clean_customers c ON o.customer_id = c.customer_id
        WHERE o.order_status IN ('delivered','shipped','invoiced')
        GROUP BY c.customer_state;
    """
    color_title = "Chiffre d’affaires (R$)"

elif analysis_type == "Délai moyen de livraison":
    query = """
        SELECT 
            c.customer_state AS state,
            ROUND(AVG(
                JULIANDAY(o.order_delivered_customer_date) 
                - JULIANDAY(o.order_purchase_timestamp)
            ), 2) AS value
        FROM clean_orders o
        JOIN clean_customers c ON o.customer_id = c.customer_id
        WHERE o.order_status='delivered'
        GROUP BY c.customer_state;
    """
    color_title = "Délai moyen (jours)"

elif analysis_type == "Nombre de commandes":
    query = """
        SELECT 
            c.customer_state AS state,
            COUNT(*) AS value
        FROM clean_orders o
        JOIN clean_customers c ON o.customer_id = c.customer_id
        WHERE o.order_status IN ('delivered','shipped','invoiced')
        GROUP BY c.customer_state;
    """
    color_title = "Nombre de commandes"

elif analysis_type == "Note moyenne":
    query = """
        SELECT 
            c.customer_state AS state,
            ROUND(AVG(r.review_score),2) AS value
        FROM clean_reviews r
        JOIN clean_orders o ON r.order_id = o.order_id
        JOIN clean_customers c ON o.customer_id = c.customer_id
        GROUP BY c.customer_state;
    """
    color_title = "Note moyenne"

df = run_query(query)

# ============================================================
# 🔹 CARTE CHOROPLETH DU BRÉSIL
# ============================================================

st.subheader(f"🗺 Carte : {analysis_type}")

fig = px.choropleth(
    df,
    geojson=geojson,
    locations="state",
    featureidkey="properties.sigla",
    color="value",
    color_continuous_scale="Viridis",
    title=f"{analysis_type} par État du Brésil",
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0, "t":40, "l":0, "b":0})

st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# ============================================================
# 🔹 TABLEAU DÉTAILLÉ + FOCUS ÉTAT
# ============================================================

st.subheader("🔎 Analyse détaillée par État")

selected_state = st.selectbox("Choisissez un État :", sorted(df["state"].unique()))

st.write(
    df[df["state"] == selected_state]
)

