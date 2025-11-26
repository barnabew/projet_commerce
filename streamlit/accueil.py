import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import load_table, get_connection, run_query
import styles
import queries
import visuel

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="resume")

# Récupération des données KPI (avec cache)
total_rev = run_query(queries.QUERY_TOTAL_REVENUE)["rev"][0]
nb_orders = run_query(queries.QUERY_TOTAL_ORDERS)["c"][0]
avg_score = run_query(queries.QUERY_AVG_REVIEW_SCORE)["avg"][0]
avg_delay = run_query(queries.QUERY_AVG_DELIVERY_DELAY)["delay"][0]

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
    # Distribution des délais de livraison
    df_delays = run_query(queries.QUERY_DELIVERY_DISTRIBUTION)
    
    fig_delays = px.bar(
        df_delays,
        x="delay_range",
        y="nb_orders",
        title="Distribution des Délais de Livraison",
        labels={"delay_range": "Délai", "nb_orders": "Nombre de commandes"},
        color="nb_orders",
        color_continuous_scale="RdYlGn_r"
    )
    visuel.apply_theme(fig_delays)
    st.plotly_chart(fig_delays, use_container_width=True)

with chart_row1[1]:
    # Top états par commandes
    df_states = run_query(queries.QUERY_TOP_STATES_ORDERS)
    
    fig_states = px.bar(
        df_states,
        x="state",
        y="nb_orders",
        title="Répartition Géographique - Top 10 États",
        labels={"state": "État", "nb_orders": "Nombre de commandes"}
    )
    visuel.apply_theme(fig_states)
    st.plotly_chart(fig_states, use_container_width=True)

chart_row2 = st.columns(2, gap="large")

with chart_row2[0]:
    # Top catégories par ventes
    df_categories = run_query(queries.QUERY_TOP_CATEGORIES_SALES)
    
    fig_categories = px.bar(
        df_categories,
        x="nb_sales",
        y="category",
        orientation="h",
        title="Catégories Populaires - Top 10",
        labels={"nb_sales": "Nombre de ventes", "category": "Catégorie"}
    )
    visuel.apply_theme(fig_categories)
    st.plotly_chart(fig_categories, use_container_width=True)

with chart_row2[1]:
    # Distribution des notes
    df_reviews = run_query(queries.QUERY_REVIEW_DISTRIBUTION)
    
    fig_reviews = px.bar(
        df_reviews,
        x="review_score",
        y="nb_reviews",
        title="Distribution des Notes Client",
        labels={"review_score": "Note", "nb_reviews": "Nombre de reviews"},
        color="review_score",
        color_continuous_scale="RdYlGn"
    )
    visuel.apply_theme(fig_reviews)
    st.plotly_chart(fig_reviews, use_container_width=True)
