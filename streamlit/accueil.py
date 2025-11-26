import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import load_table, get_connection
import styles
import queries
import visuel

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="resume")

# Récupération des données KPI
conn = get_connection()

total_rev = pd.read_sql(queries.QUERY_TOTAL_REVENUE, conn)["rev"][0]

nb_orders = pd.read_sql(queries.QUERY_TOTAL_ORDERS, conn)["c"][0]

avg_score = pd.read_sql(queries.QUERY_AVG_REVIEW_SCORE, conn)["avg"][0]

avg_delay = pd.read_sql(queries.QUERY_AVG_DELIVERY_DELAY, conn)["delay"][0]

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
    # Top catégories par CA
    df_revenue_cat = pd.read_sql(queries.QUERY_TOP_REVENUE_CATEGORIES, conn)
    
    fig_revenue_cat = px.bar(
        df_revenue_cat,
        x="revenue",
        y="category",
        orientation="h",
        title="Top 10 Catégories par Chiffre d'Affaires",
        labels={"revenue": "Chiffre d'affaires (R$)", "category": "Catégorie"},
        color="revenue",
        color_continuous_scale="Blues"
    )
    visuel.apply_theme(fig_revenue_cat)
    st.plotly_chart(fig_revenue_cat, use_container_width=True)

with chart_row1[1]:
    # Top états par commandes
    df_states = pd.read_sql(queries.QUERY_TOP_STATES_ORDERS, conn)
    
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
    df_categories = pd.read_sql(queries.QUERY_TOP_CATEGORIES_SALES, conn)
    
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
    # Délais de livraison par état
    df_delays = pd.read_sql(queries.QUERY_DELIVERY_TIME_STATS, conn)
    
    st.markdown("### Délais de Livraison par État (Top 15 plus lents)")
    st.dataframe(
        df_delays.rename(columns={
            "state": "État",
            "nb_orders": "Nb commandes",
            "avg_delay": "Délai moyen (j)",
            "min_delay": "Min (j)",
            "max_delay": "Max (j)"
        }),
        use_container_width=True,
        hide_index=True
    )
