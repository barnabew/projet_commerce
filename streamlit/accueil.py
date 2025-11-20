import streamlit as st
import pandas as pd
import numpy as np
from data import load_table, get_connection

# -----------------------------------
# CONFIG
# -----------------------------------
st.set_page_config(page_title="Olist Dashboard", layout="wide")

# -----------------------------------
# CSS DARK + MARGES + NAVBAR
# -----------------------------------
st.markdown("""
<style>

/* Full dark background */
html, body, .stApp {
    background-color: #0E1A2B !important;
}

/* Remove sidebar */
section[data-testid="stSidebar"] {
    display: none !important;
}
div[data-testid="collapsedControl"] {
    display: none !important;
}

/* PAGE CONTAINER (adds nice side margins) */
.main-container {
    max-width: 1600px;
    margin: auto;
    padding-left: 40px;
    padding-right: 40px;
}

/* NAVBAR */
.navbar {
    background-color: #152B44;
    padding: 12px 40px;
    display: flex;
    gap: 35px;
    align-items: center;
    border-bottom: 1px solid rgba(255,255,255,0.07);
}

.navitem {
    color: #BFD7FF;
    font-size: 18px;
    text-decoration: none;
    font-weight: 500;
}

.navitem:hover {
    color: white;
}

/* KPI CARDS */
.card {
    background-color: #152B44;
    padding: 25px;
    border-radius: 12px;
    margin-top: 20px;
    text-align: left;
    border: 1px solid rgba(255,255,255,0.05);
}

.card p {
    color: #8CA3C1;
    margin-bottom: 5px;
    font-size: 15px;
}

.card h2 {
    color: white;
    font-size: 30px;
    margin: 0;
}

</style>
""", unsafe_allow_html=True)


# -----------------------------------
# NAVBAR (fonctionnelle avec PageLink)
# -----------------------------------
st.markdown("""
<div class="navbar">
    <a class="navitem" href="/Accueil">Résumé</a>
    <a class="navitem" href="/geographique">Géographique</a>
    <a class="navitem" href="/produit">Produits</a>
    <a class="navitem" href="/clients">Clients</a>
    <a class="navitem" href="/recommandations">Recommandations</a>
</div>
""", unsafe_allow_html=True)


# -----------------------------------
# MAIN CONTAINER (marges latérales)
# -----------------------------------
st.markdown("<div class='main-container'>", unsafe_allow_html=True)


# -------------------------------
# KPI DATA
# -------------------------------
conn = get_connection()

total_rev = pd.read_sql("""
SELECT SUM(price + freight_value) AS rev FROM clean_order_items
""", conn)["rev"][0]

nb_orders = pd.read_sql("""
SELECT COUNT(DISTINCT order_id) AS c FROM clean_orders
""", conn)["c"][0]

avg_score = pd.read_sql("""
SELECT ROUND(AVG(review_score),2) AS avg FROM clean_reviews
""", conn)["avg"][0]

avg_delay = pd.read_sql("""
SELECT ROUND(AVG(
    JULIANDAY(order_delivered_customer_date) - JULIANDAY(order_purchase_timestamp)
),2) AS delay
FROM clean_orders WHERE order_status='delivered'
""", conn)["delay"][0]


# -------------------------------
# TITLE
# -------------------------------
st.markdown(
    "<h1 style='text-align:center; color:white; margin-top:25px;'>📊 OLIST DASHBOARD — Résumé</h1>",
    unsafe_allow_html=True
)


# -------------------------------
# KPIs
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='card'><p>Revenue total</p><h2>R$ {total_rev:,.0f}</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card'><p>Commandes</p><h2>{nb_orders:,}</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='card'><p>Note moyenne</p><h2>{avg_score}</h2></div>", unsafe_allow_html=True)

with col4:
    st.markdown(f"<div class='card'><p>Délai moyen</p><h2>{avg_delay} jours</h2></div>", unsafe_allow_html=True)



# -------------------------------
# GRAPH PLACEHOLDERS
# -------------------------------
g1, g2 = st.columns(2)
g3, g4 = st.columns(2)

with g1:
    st.markdown("<div class='card'><h3 style='color:white'>Graphique 1</h3></div>", unsafe_allow_html=True)

with g2:
    st.markdown("<div class='card'><h3 style='color:white'>Graphique 2</h3></div>", unsafe_allow_html=True)

with g3:
    st.markdown("<div class='card'><h3 style='color:white'>Graphique 3</h3></div>", unsafe_allow_html=True)

with g4:
    st.markdown("<div class='card'><h3 style='color:white'>Graphique 4</h3></div>", unsafe_allow_html=True)


# Close container
st.markdown("</div>", unsafe_allow_html=True)
