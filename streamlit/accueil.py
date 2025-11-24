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
if "current_page" not in st.session_state:
    st.session_state["current_page"] = "resume"


# ============================================================
# CSS : PROFESSIONAL DARK THEME
# ============================================================
st.markdown("""
<style>

/* ========================================
   BASE STYLES
   ======================================== */
html, body, .stApp {
    background: linear-gradient(135deg, #0a1628 0%, #111d30 100%) !important;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
}

/* REMOVE SIDEBAR */
section[data-testid="stSidebar"] { display: none !important; }
div[data-testid="collapsedControl"] { display: none !important; }

.block-container {
    padding-top: 1rem !important;
    max-width: 100% !important;
}

/* ========================================
   NAVBAR - HORIZONTAL LAYOUT
   ======================================== */
.navbar-container {
    background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
    border-bottom: 2px solid rgba(77, 168, 255, 0.2);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
    margin: -1rem -2rem 2rem -2rem;
    padding: 0;
}

.navbar-content {
    max-width: 1600px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    align-items: center;
    gap: 0;
}

.navbar-brand {
    color: #4DA8FF;
    font-size: 20px;
    font-weight: 700;
    padding: 18px 24px 18px 0;
    letter-spacing: -0.5px;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    margin-right: 0;
    flex-shrink: 0;
}

.navbar-buttons {
    display: flex;
    flex: 1;
    gap: 0;
}

/* Style pour les colonnes Streamlit dans la navbar */
.navbar-buttons [data-testid="column"] {
    flex: 1;
}

/* Masquer le style par défaut des boutons Streamlit */
.navbar-buttons button {
    width: 100% !important;
    height: 100% !important;
    min-height: 54px !important;
    padding: 18px 16px !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    color: #95adc7 !important;
    font-size: 15px !important;
    font-weight: 500 !important;
    border-bottom: 3px solid transparent !important;
    transition: all 0.3s ease !important;
    box-shadow: none !important;
}

.navbar-buttons button:hover {
    background: rgba(77, 168, 255, 0.08) !important;
    color: #d4e3f5 !important;
    border-bottom-color: rgba(77, 168, 255, 0.3) !important;
}

.navbar-buttons button:focus,
.navbar-buttons button:active {
    box-shadow: none !important;
    outline: none !important;
}

/* Bouton actif */
.nav-active button {
    color: #ffffff !important;
    background: rgba(77, 168, 255, 0.12) !important;
    border-bottom-color: #4DA8FF !important;
    font-weight: 600 !important;
}

/* ========================================
   KPI CARDS
   ======================================== */
.kpi-card {
    background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
    padding: 28px;
    border-radius: 12px;
    border: 1px solid rgba(77, 168, 255, 0.15);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
}

.kpi-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 30px rgba(77, 168, 255, 0.15);
    border-color: rgba(77, 168, 255, 0.25);
}

.kpi-label {
    color: #95adc7;
    font-size: 13px;
    text-transform: uppercase;
    letter-spacing: 1.2px;
    font-weight: 600;
    margin-bottom: 10px;
}

.kpi-value {
    color: #ffffff;
    font-size: 34px;
    font-weight: 700;
    line-height: 1.2;
    letter-spacing: -0.5px;
}

/* ========================================
   CHART CONTAINERS
   ======================================== */
.chart-container {
    background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
    padding: 30px;
    border-radius: 12px;
    border: 1px solid rgba(77, 168, 255, 0.15);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
    min-height: 300px;
}

.chart-container:hover {
    box-shadow: 0 8px 30px rgba(77, 168, 255, 0.12);
    border-color: rgba(77, 168, 255, 0.22);
}

.chart-title {
    color: #ffffff;
    font-size: 18px;
    font-weight: 600;
    margin-bottom: 8px;
    letter-spacing: -0.3px;
}

.chart-subtitle {
    color: #95adc7;
    font-size: 14px;
    margin-bottom: 20px;
}

/* ========================================
   SECTION TITLE
   ======================================== */
.section-header {
    color: #ffffff;
    font-size: 26px;
    font-weight: 700;
    margin: 40px 0 25px 0;
    letter-spacing: -0.5px;
    padding-left: 15px;
    border-left: 4px solid #4DA8FF;
}

/* ========================================
   SCROLLBAR
   ======================================== */
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
# NAVIGATION HANDLER
# ============================================================
def navigate_to(page_name):
    st.session_state["current_page"] = page_name


# ============================================================
# NAVBAR - STRUCTURE SIMPLE
# ============================================================
st.markdown("""
<div class="navbar-container">
    <div class="navbar-content">
        <div class="navbar-brand">📊 Olist Analytics</div>
        <div class="navbar-buttons">
""", unsafe_allow_html=True)

# Créer les colonnes pour les boutons de navigation
col1, col2, col3, col4, col5 = st.columns(5)

pages = [
    ("resume", "Résumé", col1),
    ("geographique", "Géographique", col2),
    ("produit", "Produits", col3),
    ("clients", "Clients", col4),
    ("recommandations", "Recommandations", col5)
]

for page_id, label, col in pages:
    with col:
        active_class = "nav-active" if st.session_state["current_page"] == page_id else ""
        st.markdown(f'<div class="{active_class}">', unsafe_allow_html=True)
        if st.button(label, key=f"nav_{page_id}", use_container_width=True):
            navigate_to(page_id)
        st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# MAIN CONTENT
# ============================================================

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
kpi_cols = st.columns(4, gap="medium")

with kpi_cols[0]:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-label'>Revenue Total</div>
        <div class='kpi-value'>R$ {total_rev:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-label'>Commandes</div>
        <div class='kpi-value'>{nb_orders:,}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-label'>Note Moyenne</div>
        <div class='kpi-value'>{avg_score} ⭐</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(f"""
    <div class='kpi-card'>
        <div class='kpi-label'>Délai Moyen</div>
        <div class='kpi-value'>{avg_delay} j</div>
    </div>
    """, unsafe_allow_html=True)


# -------------------------------
# SECTION TITLE
# -------------------------------
st.markdown("<div class='section-header'>Analyses Détaillées</div>", unsafe_allow_html=True)


# -------------------------------
# CHARTS
# -------------------------------
chart_row1 = st.columns(2, gap="medium")

with chart_row1[0]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>📈 Évolution des Ventes</div>
        <div class='chart-subtitle'>Tendance mensuelle du chiffre d'affaires</div>
    </div>
    """, unsafe_allow_html=True)

with chart_row1[1]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>🌍 Répartition Géographique</div>
        <div class='chart-subtitle'>Top des régions par volume</div>
    </div>
    """, unsafe_allow_html=True)

chart_row2 = st.columns(2, gap="medium")

with chart_row2[0]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>🛍️ Catégories Populaires</div>
        <div class='chart-subtitle'>Produits les plus vendus</div>
    </div>
    """, unsafe_allow_html=True)

with chart_row2[1]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>⭐ Satisfaction Client</div>
        <div class='chart-subtitle'>Distribution des notes</div>
    </div>
    """, unsafe_allow_html=True)
