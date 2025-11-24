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
st.markdown("""
<style>

html, body, .stApp {
    background: linear-gradient(135deg, #0a1628 0%, #0e1f38 100%) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="collapsedControl"] { display: none !important; }

.main-container {
    max-width: 1600px;
    margin: 0 auto;
    padding: 0 40px 40px 40px;
}

/* ========== NAVBAR ========== */

/* === NAVBAR WRAPPER === */
.nav-wrapper {
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 14px 30px;
    border-bottom: 1px solid rgba(77,168,255,0.2);
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin: -20px -40px 30px -40px;
    display: flex;
    gap: 0px;
}

.nav-wrapper [data-testid="column"] {
    display: flex;
    justify-content: center;
}

/* === REMOVE STREAMLIT DEFAULT LINK STYLE === */
div[data-testid="stPageLink"] a {
    text-decoration: none !important;
}

/* === NAV BUTTON STYLE (like your old ones) === */
div[data-testid="stPageLink"] a span[data-testid="stPageLink-label"] {
    display: block;
    background: transparent;
    color: #a8c5e0;
    padding: 12px 16px;
    text-align: center;
    border-radius: 8px;
    font-size: 15px;
    font-weight: 500;
    transition: all .25s ease;
    border: 1px solid transparent;
}

/* === HOVER === */
div[data-testid="stPageLink"] a:hover span[data-testid="stPageLink-label"] {
    background: rgba(77,168,255,0.15);
    border-color: rgba(77,168,255,0.3);
    color: #fff;
    transform: translateY(-2px);
}

/* === ACTIVE PAGE (Streamlit sets aria-current="page") === */
div[data-testid="stPageLink"] a[aria-current="page"] span[data-testid="stPageLink-label"] {
    background: linear-gradient(135deg, #4DA8FF, #3d8fe0);
    color: white !important;
    border-color: rgba(255,255,255,0.3);
    box-shadow: 0 4px 12px rgba(77,168,255,0.4);
}

/* ========== CARD STYLES ========== */

.card {
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 28px;
    border-radius: 16px;
    margin-top: 20px;
    border: 1px solid rgba(77, 168, 255, 0.15);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

.card p {
    color: #8ca3c1;
    margin-bottom: 8px;
    font-size: 14px;
    text-transform: uppercase;
}

.card h2 {
    color: #fff;
    font-size: 32px;
    margin: 0;
    font-weight: 700;
}

.chart-card {
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 32px;
    border-radius: 16px;
    margin-top: 20px;
    border: 1px solid rgba(77,168,255,0.15);
}

.chart-card h3 {
    color: white;
    margin-bottom: 8px;
}

</style>
""", unsafe_allow_html=True)



# ============================================================
# NAVBAR (Streamlit-native but styled)
# ============================================================
st.markdown("<div class='nav-wrapper'>", unsafe_allow_html=True)

nav = st.container()
with nav:
    c1, c2, c3, c4, c5 = st.columns([1,1,1,1,1])

    with c1:
        st.page_link("accueil.py", label="Résumé")

    with c2:
        st.page_link("pages/2_geographique.py", label="Géographique")

    with c3:
        st.page_link("pages/3_produit.py", label="Produits")

    with c4:
        st.page_link("pages/4_clients.py", label="Clients")

    with c5:
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
