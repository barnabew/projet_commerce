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

/* Remove default Streamlit padding */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
}

/* PAGE WRAPPER */
.main-container {
    max-width: 1600px;
    margin: 0 auto;
    padding: 0 40px 40px 40px;
}

/* ========================================
   NAVBAR - PROFESSIONAL & CLEAN
   ======================================== */
.top-navbar {
    background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
    padding: 0;
    border-bottom: 2px solid rgba(77, 168, 255, 0.2);
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
    margin: -2rem -40px 40px -40px;
}

.navbar-content {
    max-width: 1600px;
    margin: 0 auto;
    padding: 0 40px;
    display: flex;
    align-items: center;
    gap: 0;
}

.navbar-brand {
    color: #4DA8FF;
    font-size: 22px;
    font-weight: 700;
    padding: 20px 30px 20px 0;
    letter-spacing: -0.5px;
    border-right: 1px solid rgba(255, 255, 255, 0.08);
    margin-right: 0;
}

/* Hide Streamlit button styling */
.stButton button {
    background: transparent !important;
    border: none !important;
    padding: 0 !important;
    color: inherit !important;
    box-shadow: none !important;
    width: 100% !important;
    height: 100% !important;
}

.stButton button:hover {
    background: transparent !important;
    border: none !important;
    color: inherit !important;
}

.stButton button:active,
.stButton button:focus {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
}

/* Navigation tabs */
.nav-tab {
    flex: 1;
    padding: 20px 24px;
    color: #95adc7;
    font-size: 15px;
    font-weight: 500;
    text-align: center;
    cursor: pointer;
    transition: all 0.3s ease;
    border-bottom: 3px solid transparent;
    background: transparent;
}

.nav-tab:hover {
    background: rgba(77, 168, 255, 0.08);
    color: #d4e3f5;
}

.nav-tab-active {
    color: #ffffff !important;
    background: rgba(77, 168, 255, 0.12) !important;
    border-bottom-color: #4DA8FF !important;
    font-weight: 600;
}

/* ========================================
   KPI CARDS - PROFESSIONAL DESIGN
   ======================================== */
.kpi-card {
    background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
    padding: 30px;
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
    margin-top: 20px;
    border: 1px solid rgba(77, 168, 255, 0.15);
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    transition: all 0.3s ease;
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
    margin: 50px 0 25px 0;
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
    st.rerun()


# ============================================================
# NAVBAR
# ============================================================
st.markdown("""
<div class="top-navbar">
    <div class="navbar-content">
        <div class="navbar-brand">📊 Olist Analytics</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Navigation buttons
nav_cols = st.columns(5)
pages = [
    ("resume", "Résumé"),
    ("geographique", "Géographique"),
    ("produit", "Produits"),
    ("clients", "Clients"),
    ("recommandations", "Recommandations")
]

for idx, (page_id, label) in enumerate(pages):
    with nav_cols[idx]:
        active_class = "nav-tab-active" if st.session_state["current_page"] == page_id else ""
        st.markdown(f'<div class="nav-tab {active_class}">', unsafe_allow_html=True)
        if st.button(label, key=f"nav_{page_id}", use_container_width=True):
            navigate_to(page_id)
        st.markdown('</div>', unsafe_allow_html=True)


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
kpi_cols = st.columns(4)

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
chart_row1 = st.columns(2)
chart_row2 = st.columns(2)

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


# CLOSE MAIN WRAPPER
st.markdown("</div>", unsafe_allow_html=True)
