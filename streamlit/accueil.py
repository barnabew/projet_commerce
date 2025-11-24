import streamlit as st
import pandas as pd
import numpy as np
from data import load_table, get_connection

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Olist Dashboard", layout="wide")


# ============================================================
# CSS : NAVBAR + THEME
# ============================================================
# ============================================================
# NAVBAR CLEAN + PRO
# ============================================================

st.markdown("""
<style>

.navbar {
    display: flex;
    justify-content: center;
    gap: 40px;
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 20px 0;
    border-bottom: 1px solid rgba(77,168,255,0.25);
    margin: -30px 0 30px 0;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}

/* Supprime style par défaut */
.navbar a {
    text-decoration: none !important;
}

/* Style des boutons */
.navbar a span[data-testid="stPageLink-label"] {
    background: transparent;
    color: #a8c5e0;
    padding: 10px 22px;
    border-radius: 10px;
    font-size: 16px;
    font-weight: 500;
    border: 1px solid rgba(255,255,255,0.05);
    transition: all .25s ease;
}

/* Hover */
.navbar a:hover span[data-testid="stPageLink-label"] {
    background: rgba(77,168,255,0.18);
    color: white;
    border-color: rgba(77,168,255,0.5);
    transform: translateY(-2px);
}

/* Active page */
.navbar a[aria-current="page"] span[data-testid="stPageLink-label"] {
    background: linear-gradient(135deg, #4DA8FF, #3d8fe0);
    color: white !important;
    box-shadow: 0 4px 14px rgba(77,168,255,0.4);
    border-color: rgba(255,255,255,0.3);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVBAR (Streamlit-native but styled)
# ============================================================
st.markdown("<div class='navbar'>", unsafe_allow_html=True)

st.page_link("accueil.py", label="Résumé")
st.page_link("pages/2_geographique.py", label="Géographique")
st.page_link("pages/3_produit.py", label="Produits")
st.page_link("pages/4_clients.py", label="Clients")
st.page_link("pages/5_recommandations.py", label="Recommandations")

st.markdown("</div>", unsafe_allow_html=True)



# ============================================================
# MAIN CONTENT WRAPPER
# ============================================================
st.markdown("<div class='main-container'>", unsafe_allow_html=True)



# ============================================================
# KPI SECTION
# ============================================================
conn = get_connection()

total_rev = pd.read_sql("SELECT SUM(price + freight_value) AS rev FROM clean_order_items", conn)["rev"][0]
nb_orders = pd.read_sql("SELECT COUNT(DISTINCT order_id) AS c FROM clean_orders", conn)["c"][0]
avg_score = pd.read_sql("SELECT ROUND(AVG(review_score),2) AS avg FROM clean_reviews", conn)["avg"][0]
avg_delay = pd.read_sql("""
SELECT ROUND(AVG(
    JULIANDAY(order_delivered_customer_date)-JULIANDAY(order_purchase_timestamp)
),2) AS delay
FROM clean_orders WHERE order_status='delivered'""", conn)["delay"][0]


col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"<div class='card'><p>Revenue Total</p><h2>R$ {total_rev:,.0f}</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown(f"<div class='card'><p>Commandes</p><h2>{nb_orders:,}</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown(f"<div class='card'><p>Note Moyenne</p><h2>{avg_score} ⭐</h2></div>", unsafe_allow_html=True)

with col4:
    st.markdown(f"<div class='card'><p>Délai Moyen</p><h2>{avg_delay} jours</h2></div>", unsafe_allow_html=True)



# ============================================================
# PLACEHOLDER GRAPHS
# ============================================================
g1, g2 = st.columns(2)
g3, g4 = st.columns(2)

with g1:
    st.markdown("<div class='chart-card'><h3>📈 Évolution des Ventes</h3></div>", unsafe_allow_html=True)

with g2:
    st.markdown("<div class='chart-card'><h3>🌍 Répartition Géographique</h3></div>", unsafe_allow_html=True)

with g3:
    st.markdown("<div class='chart-card'><h3>🛍️ Catégories Populaires</h3></div>", unsafe_allow_html=True)

with g4:
    st.markdown("<div class='chart-card'><h3>⭐ Satisfaction Client</h3></div>", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)
