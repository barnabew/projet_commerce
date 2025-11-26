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
""", conn)["delay"][0]

# Affichage des KPI
kpi_cols = st.columns(4, gap="large")

with kpi_cols[0]:
    st.markdown(styles.render_kpi_card("Revenue Total", f"R$ {total_rev:,.0f}"), unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(styles.render_kpi_card("Commandes", f"{nb_orders:,}"), unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(styles.render_kpi_card("Note Moyenne", f"{avg_score} ⭐"), unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(styles.render_kpi_card("Délai Moyen", f"{avg_delay} j"), unsafe_allow_html=True)

# Section titre
st.markdown(styles.render_section_header("Analyses Détaillées"), unsafe_allow_html=True)

# Graphiques
chart_row1 = st.columns(2, gap="large")

with chart_row1[0]:
    st.markdown(styles.render_chart_container("Évolution des Ventes", "Tendance mensuelle du chiffre d'affaires"), unsafe_allow_html=True)

with chart_row1[1]:
    st.markdown(styles.render_chart_container("Répartition Géographique", "Top des régions par volume"), unsafe_allow_html=True)

chart_row2 = st.columns(2, gap="large")

with chart_row2[0]:
    st.markdown(styles.render_chart_container("Catégories Populaires", "Produits les plus vendus"), unsafe_allow_html=True)

with chart_row2[1]:
    st.markdown(styles.render_chart_container("Satisfaction Client", "Distribution des notes"), unsafe_allow_html=True)
