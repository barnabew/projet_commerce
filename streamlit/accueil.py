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

# Message stratégique
st.markdown("""
### 🎯 Stratégie : Expérience One-Shot Parfaite → Viralité

**97% des clients Olist n'achètent qu'une seule fois.**  
Plutôt que de lutter contre cette réalité, nous optimisons **chaque première expérience** pour transformer les clients en **ambassadeurs**.

**Objectif** : Croissance via bouche-à-oreille et parrainage (20% d'acquisition organique d'ici 12 mois)
""")

st.markdown("---")

# Récupération des données KPI (avec cache) - Focus Expérience One-Shot
pct_5_stars = run_query(queries.QUERY_PERCENT_5_STARS)["pct_5_stars"][0]
pct_fast = run_query(queries.QUERY_PERCENT_FAST_DELIVERY)["pct_fast"][0]
avg_basket = run_query(queries.QUERY_AVG_BASKET)["avg_basket"][0]
avg_score = run_query(queries.QUERY_AVG_REVIEW_SCORE)["avg"][0]

# Affichage des KPI
kpi_cols = st.columns(4, gap="large")

with kpi_cols[0]:
    st.markdown(styles.render_kpi_card("Clients 5⭐", f"{pct_5_stars}%"), unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(styles.render_kpi_card("Livraison <7j", f"{pct_fast}%"), unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(styles.render_kpi_card("Panier Moyen", f"R$ {avg_basket:,.0f}"), unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(styles.render_kpi_card("Satisfaction", f"{avg_score}/5 ⭐"), unsafe_allow_html=True)

# Section titre
st.markdown(styles.render_section_header("Analyses Détaillées"), unsafe_allow_html=True)

# Graphiques
chart_row1 = st.columns(2, gap="large")

with chart_row1[0]:
    # Corrélation Délai vs Satisfaction
    df_delay_sat = run_query(queries.QUERY_DELAY_VS_SATISFACTION)
    
    fig_delay_sat = px.box(
        df_delay_sat,
        x="review_score",
        y="delivery_days",
        title="Impact du Délai de Livraison sur la Satisfaction",
        labels={"review_score": "Note", "delivery_days": "Délai de livraison (jours)"}
    )
    fig_delay_sat.update_traces(marker=dict(opacity=0), showlegend=False)
    visuel.apply_theme(fig_delay_sat)
    st.plotly_chart(fig_delay_sat, use_container_width=True)

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
        labels={"review_score": "Note", "nb_reviews": "Nombre de reviews"}
    )
    visuel.apply_theme(fig_reviews)
    st.plotly_chart(fig_reviews, use_container_width=True)
