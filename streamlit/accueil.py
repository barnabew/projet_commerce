import streamlit as st
import pandas as pd
import numpy as np
from data import load_table, get_connection

# ============================================================
# PAGE CONFIG
# ============================================================
st.set_page_config(page_title="Olist Dashboard", layout="wide")

# ============================================================
# ACTIVE PAGE IDENTIFICATION
# ============================================================
st.session_state["page"] = "resume"


# ============================================================
# CSS : MODERN DARK THEME + BEAUTIFUL NAVBAR + ENHANCED LAYOUT
# ============================================================
st.markdown("""
<style>

/* ========================================
   BASE STYLES
   ======================================== */
html, body, .stApp {
    background: linear-gradient(135deg, #0a1628 0%, #0e1f38 100%) !important;
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* REMOVE SIDEBAR */
section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="collapsedControl"] { display: none !important; }

/* PAGE WRAPPER */
.main-container {
    max-width: 1600px;
    margin: 0 auto;
    padding: 0 40px 40px 40px;
}

/* ========================================
   NAVBAR - MODERN & ELEGANT
   ======================================== */
.navbar {
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 16px 40px;
    display: flex;
    gap: 0px;
    align-items: stretch;
    border-bottom: 1px solid rgba(77, 168, 255, 0.2);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3);
    margin: -20px -40px 30px -40px;
    backdrop-filter: blur(10px);
}

/* Logo/Brand area (optional) */
.navbar-brand {
    color: #4DA8FF;
    font-size: 20px;
    font-weight: 700;
    margin-right: 20px;
    letter-spacing: -0.5px;
    display: flex;
    align-items: center;
}

/* Nav buttons container */
.nav-buttons {
    display: flex;
    flex: 1;
    gap: 4px;
}

/* Nav buttons - prennent toute la largeur */
.navbtn {
    flex: 1;
    padding: 12px 16px;
    border-radius: 8px;
    color: #a8c5e0;
    font-size: 15px;
    text-decoration: none;
    font-weight: 500;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
    border: 1px solid transparent;
    text-align: center;
    cursor: pointer;
    background: transparent;
    display: flex;
    align-items: center;
    justify-content: center;
}

/* Hover effect with subtle glow */
.navbtn:hover {
    background: rgba(77, 168, 255, 0.1);
    color: #fff;
    border-color: rgba(77, 168, 255, 0.3);
    transform: translateY(-1px);
}

/* ACTIVE TAB - Beautiful highlight */
.nav-active {
    background: linear-gradient(135deg, #4DA8FF 0%, #3d8fe0 100%);
    color: #ffffff !important;
    box-shadow: 0 4px 15px rgba(77, 168, 255, 0.4);
    border-color: rgba(255, 255, 255, 0.2);
    font-weight: 600;
}

.nav-active:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(77, 168, 255, 0.5);
}

/* Streamlit button override */
div[data-testid="column"] button {
    width: 100%;
    background: transparent;
    border: none;
    color: inherit;
    padding: 0;
    font: inherit;
}

/* ========================================
   KPI CARDS - ENHANCED DESIGN
   ======================================== */
.card {
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 28px;
    border-radius: 16px;
    margin-top: 20px;
    text-align: left;
    border: 1px solid rgba(77, 168, 255, 0.15);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
    position: relative;
    overflow: hidden;
}

/* Subtle gradient overlay */
.card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #4DA8FF, #7B61FF);
    opacity: 0;
    transition: opacity 0.3s ease;
}

.card:hover {
    transform: translateY(-4px);
    box-shadow: 0 12px 40px rgba(77, 168, 255, 0.2);
    border-color: rgba(77, 168, 255, 0.3);
}

.card:hover::before {
    opacity: 1;
}

.card p {
    color: #8ca3c1;
    margin-bottom: 8px;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: 500;
}

.card h2 {
    color: #ffffff;
    font-size: 32px;
    margin: 0;
    font-weight: 700;
    background: linear-gradient(135deg, #ffffff 0%, #a8c5e0 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

/* ========================================
   CHART CONTAINERS
   ======================================== */
.chart-card {
    background: linear-gradient(135deg, #1a2f4a 0%, #162841 100%);
    padding: 32px;
    border-radius: 16px;
    margin-top: 20px;
    border: 1px solid rgba(77, 168, 255, 0.15);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
    transition: all 0.3s ease;
}

.chart-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 40px rgba(77, 168, 255, 0.15);
    border-color: rgba(77, 168, 255, 0.25);
}

.chart-card h3 {
    color: #ffffff;
    margin: 0 0 20px 0;
    font-size: 18px;
    font-weight: 600;
    letter-spacing: -0.3px;
}

/* ========================================
   UTILITY CLASSES
   ======================================== */
.section-title {
    color: #dbd7d7;
    font-size: 28px;
    font-weight: 700;
    margin: 40px 0 20px 0;
    letter-spacing: -0.5px;
}

/* Scrollbar styling */
::-webkit-scrollbar {
    width: 10px;
    height: 10px;
}

::-webkit-scrollbar-track {
    background: #0a1628;
}

::-webkit-scrollbar-thumb {
    background: rgba(77, 168, 255, 0.3);
    border-radius: 5px;
}

::-webkit-scrollbar-thumb:hover {
    background: rgba(77, 168, 255, 0.5);
}

</style>
""", unsafe_allow_html=True)




# ============================================================
# NAVBAR (Enhanced with brand)
# ============================================================
if "page" not in st.session_state:
    st.session_state["page"] = "resume"

def nav_item(label, link, page_id):
    active = "nav-active" if st.session_state["page"] == page_id else ""
    return f'<a class="navbtn {active}" href="{link}">{label}</a>'

navbar = f"""
<div class="navbar">
    {nav_item('Résumé', '/', 'resume')}
    {nav_item('Géographique', '/geographique', 'geographique')}
    {nav_item('Produits', '/produit', 'produit')}
    {nav_item('Clients', '/clients', 'clients')}
    {nav_item('Recommandations', '/recommandations', 'recommandations')}
</div>
"""

st.markdown(navbar, unsafe_allow_html=True)


# ============================================================
# MAIN PAGE CONTENT
# ============================================================
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
# KPIs ROW
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(
        f"<div class='card'><p>Revenue Total</p><h2>R$ {total_rev:,.0f}</h2></div>",
        unsafe_allow_html=True)

with col2:
    st.markdown(
        f"<div class='card'><p>Commandes</p><h2>{nb_orders:,}</h2></div>",
        unsafe_allow_html=True)

with col3:
    st.markdown(
        f"<div class='card'><p>Note Moyenne</p><h2>{avg_score} ⭐</h2></div>",
        unsafe_allow_html=True)

with col4:
    st.markdown(
        f"<div class='card'><p>Délai Moyen</p><h2>{avg_delay} jours</h2></div>",
        unsafe_allow_html=True)



# -------------------------------
# GRAPH PLACEHOLDERS
# -------------------------------
g1, g2 = st.columns(2)
g3, g4 = st.columns(2)

with g1:
    st.markdown("<div class='chart-card'><h3>📈 Évolution des Ventes</h3><p style='color: #8ca3c1;'>Tendance mensuelle du chiffre d'affaires</p></div>",
                unsafe_allow_html=True)

with g2:
    st.markdown("<div class='chart-card'><h3>🌍 Répartition Géographique</h3><p style='color: #8ca3c1;'>Top des régions par volume</p></div>",
                unsafe_allow_html=True)

with g3:
    st.markdown("<div class='chart-card'><h3>🛍️ Catégories Populaires</h3><p style='color: #8ca3c1;'>Produits les plus vendus</p></div>",
                unsafe_allow_html=True)

with g4:
    st.markdown("<div class='chart-card'><h3>⭐ Satisfaction Client</h3><p style='color: #8ca3c1;'>Distribution des notes</p></div>",
                unsafe_allow_html=True)



# CLOSE MAIN WRAPPER
st.markdown("</div>", unsafe_allow_html=True)
