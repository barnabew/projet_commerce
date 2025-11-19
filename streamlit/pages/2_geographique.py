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
