import streamlit as st
import pandas as pd
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

# Objectif du Dashboard
with st.expander("Comprendre l'Écosystème Retail", expanded=True):
    st.markdown("""
    **Retail Analytics Dashboard** - Analyse des performances de ventes retail pour optimiser 
    l'assortiment départemental et les stratégies par type de magasin.
    
    **Contexte**: Données retail multi-magasins avec segmentation par type (A, B, C)
    
    **Objectif**: Analyser les performances pour:
    - Optimiser l'assortiment départemental par type de magasin
    - Identifier les leviers de croissance saisonniers
    - Améliorer la performance globale de l'écosystème retail
    - Développer des stratégies différenciées selon la taille des magasins
    """)

st.markdown("---")

# Récupération des données KPI
ca_total = run_query(queries.QUERY_CA_TOTAL)["CA_Total"][0]
ca_moyen = run_query(queries.QUERY_CA_MOYEN)["CA_Moyen"][0]
nb_magasins = run_query(queries.QUERY_NB_MAGASINS)["Nb_Magasins"][0]
nb_departements = run_query(queries.QUERY_NB_DEPARTEMENTS)["Nb_Departements"][0]

# Affichage des KPI
kpi_cols = st.columns(4, gap="large")

with kpi_cols[0]:
    st.markdown(styles.render_kpi_card("CA Total", f"${ca_total:,.0f}"), unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(styles.render_kpi_card("CA Moyen Hebdo", f"${ca_moyen:,.0f}"), unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(styles.render_kpi_card("Magasins", f"{nb_magasins}"), unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(styles.render_kpi_card("Départements", f"{nb_departements}"), unsafe_allow_html=True)

st.markdown("---")

# Graphiques
chart_row1 = st.columns(2, gap="large")

with chart_row1[0]:
    # Corrélation Taille-Performance
    df_taille_perf = run_query(queries.QUERY_TAILLE_PERFORMANCE)
    
    fig_taille_perf = px.scatter(
        df_taille_perf,
        x="Size",
        y="CA_Moyen",
        color="Type",
        title="Corrélation Taille-Performance par Type",
        labels={"Size": "Taille (sqft)", "CA_Moyen": "CA Moyen Hebdomadaire ($)"}
    )
    visuel.apply_theme(fig_taille_perf)
    st.plotly_chart(fig_taille_perf, use_container_width=True)

with chart_row1[1]:
    # Performance par Type de Magasin
    df_types_performance = run_query(queries.QUERY_TYPES_PERFORMANCE)
    
    fig_types_performance = px.bar(
        df_types_performance,
        x="Type",
        y="CA_Moyen",
        title="Performance Moyenne par Type de Magasin",
        labels={"Type": "Type de magasin", "CA_Moyen": "CA Moyen Hebdomadaire ($)"}
    )
    visuel.apply_theme(fig_types_performance)
    st.plotly_chart(fig_types_performance, use_container_width=True)

chart_row2 = st.columns(2, gap="large")

with chart_row2[0]:
    # Top départements par CA
    df_top_depts = run_query(queries.QUERY_TOP_DEPARTMENTS)
    
    fig_top_depts = px.bar(
        df_top_depts.head(10),
        x="CA_Total",
        y="Dept",
        orientation="h",
        title="Top 10 Départements par CA Total",
        labels={"CA_Total": "Chiffre d'affaires ($)", "Dept": "Département"}
    )
    visuel.apply_theme(fig_top_depts)
    st.plotly_chart(fig_top_depts, use_container_width=True)

with chart_row2[1]:
    # Évolution temporelle globale
    df_evolution = run_query(queries.QUERY_EVOLUTION_MENSUELLE)
    
    fig_evolution = px.line(
        df_evolution,
        x="Mois",
        y="CA_Total_Mensuel",
        title="Évolution du CA Mensuel",
        labels={"Mois": "Mois", "CA_Total_Mensuel": "CA Total Mensuel ($)"},
        markers=True
    )
    visuel.apply_theme(fig_evolution)
    st.plotly_chart(fig_evolution, use_container_width=True)