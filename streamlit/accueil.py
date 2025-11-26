import streamlit as st
import pandas as pd
import numpy as np
from data import load_table, get_connection
import styles

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="resume")

# Récupération des données KPI
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
conn)['delay'][0]

# Affichage des KPI
kpi_cols = st.columns(4, gap="large")

with kpi_cols[0]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Revenue Total</div>
        <div class="kpi-value">R$ {total_rev:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Commandes</div>
        <div class="kpi-value">{nb_orders:,}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Note Moyenne</div>
        <div class="kpi-value">{avg_score} ⭐</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-label">Délai Moyen</div>
        <div class="kpi-value">{avg_delay} j</div>
    </div>
    """, unsafe_allow_html=True)

# Section titre
st.markdown("<div class='section-header'>Analyses Détaillées</div>", unsafe_allow_html=True)

# Graphiques
chart_row1 = st.columns(2, gap="large")

with chart_row1[0]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>Évolution des Ventes</div>
        <div class='chart-subtitle'>Tendance mensuelle du chiffre d'affaires</div>
    </div>
    """, unsafe_allow_html=True)

with chart_row1[1]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>Répartition Géographique</div>
        <div class='chart-subtitle'>Top des régions par volume</div>
    </div>
    """, unsafe_allow_html=True)

chart_row2 = st.columns(2, gap="large")

with chart_row2[0]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>Catégories Populaires</div>
        <div class='chart-subtitle'>Produits les plus vendus</div>
    </div>
    """, unsafe_allow_html=True)

with chart_row2[1]:
    st.markdown("""
    <div class='chart-container'>
        <div class='chart-title'>Satisfaction Client</div>
        <div class='chart-subtitle'>Distribution des notes</div>
    </div>
    """, unsafe_allow_html=True)
