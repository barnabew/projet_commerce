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

# Objectif du Dashboard
with st.expander("Recommandations", expanded=False):
    st.markdown("""
    **Olist** est une plateforme B2B SaaS qui connecte les petits vendeurs brésiliens aux grandes marketplaces 
    (Amazon, Mercado Libre, etc.). Ce dashboard analyse les données transactionnelles de l'écosystème Olist 
    pour identifier les leviers d'optimisation de leur service B2B.
    
    **Contexte**: 2016-2018, transactions facilitées par la plateforme Olist
    
    **Objectif**: Analyser la performance de l'écosystème pour aider Olist à:
    - Optimiser son service d'intégration marketplace
    - Identifier les points de friction (logistique, satisfaction)
    - Développer de nouveaux services pour leurs clients vendeurs
    - Améliorer l'expérience globale de l'écosystème
    """)

st.markdown("---")

# Récupération des données KPI (avec cache) - Performance Écosystème Olist
pct_5_stars = run_query(queries.QUERY_PERCENT_5_STARS)["pct_5_stars"][0]
pct_fast = run_query(queries.QUERY_PERCENT_FAST_DELIVERY)["pct_fast"][0]
avg_basket = run_query(queries.QUERY_AVG_BASKET)["avg_basket"][0]
avg_score = run_query(queries.QUERY_AVG_REVIEW_SCORE)["avg"][0]

# Affichage des KPI
kpi_cols = st.columns(4, gap="large")

with kpi_cols[0]:
    st.markdown(styles.render_kpi_card("Excellence (5★)", f"{pct_5_stars}%"), unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(styles.render_kpi_card("Livraisons Rapides", f"{pct_fast}%"), unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(styles.render_kpi_card("Panier Moyen", f"R$ {avg_basket:,.0f}"), unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(styles.render_kpi_card("Score Satisfaction", f"{avg_score}/5"), unsafe_allow_html=True)



st.markdown("---")

# Graphiques
chart_row1 = st.columns(2, gap="large")

with chart_row1[0]:
    # Corrélation Délai vs Satisfaction
    df_delay_sat = run_query(queries.QUERY_DELAY_VS_SATISFACTION)
    
    fig_delay_sat = px.box(
        df_delay_sat,
        x="review_score",
        y="delivery_days",
        title="Corrélation Délais-Satisfaction dans l'Écosystème Olist",
        labels={"review_score": "Note", "delivery_days": "Délai de livraison (jours)"}
    )
    fig_delay_sat.update_traces(marker=dict(opacity=0), showlegend=False)
    visuel.apply_theme(fig_delay_sat)
    st.plotly_chart(fig_delay_sat, use_container_width=True)

with chart_row1[1]:
    # Volume par état (marché géographique de l'écosystème)
    df_states_volume = run_query(queries.QUERY_TOP_STATES_ORDERS)
    
    fig_states_volume = px.bar(
        df_states_volume.head(8),  # Top 8 pour lisibilité
        x="state",
        y="nb_orders",
        title="Volume de Commandes par État (Top Marchés)",
        labels={"state": "État", "nb_orders": "Nombre de commandes"}
    )
    visuel.apply_theme(fig_states_volume)
    st.plotly_chart(fig_states_volume, use_container_width=True)

chart_row2 = st.columns(2, gap="large")

with chart_row2[0]:
    # Top catégories par chiffre d'affaires (segments clés écosystème)
    df_categories_revenue = run_query(queries.QUERY_TOP_CATEGORIES_REVENUE)
    
    fig_categories_revenue = px.bar(
        df_categories_revenue.head(8),  # Top 8 pour lisibilité
        x="revenue",
        y="category",
        orientation="h",
        title="Top Catégories par Chiffre d'Affaires (Segments Clés)",
        labels={"revenue": "Chiffre d'affaires (R$)", "category": "Catégorie"}
    )
    visuel.apply_theme(fig_categories_revenue)
    st.plotly_chart(fig_categories_revenue, use_container_width=True)

with chart_row2[1]:
    # Distribution des notes
    df_reviews = run_query(queries.QUERY_REVIEW_DISTRIBUTION)
    
    fig_reviews = px.bar(
        df_reviews,
        x="review_score",
        y="nb_reviews",
        title="Distribution des Notes Client",
        labels={"review_score": "Note", "nb_reviews": "Nombre de reviews"}
    )
    visuel.apply_theme(fig_reviews)
    st.plotly_chart(fig_reviews, use_container_width=True)
