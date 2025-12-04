import streamlit as st
from utils import run_query
import plotly.express as px
import pandas as pd
import requests
import plotly.graph_objects as go
import styles
import textes
import visuel
import queries

st.session_state["page"] = "geographique"

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="geographique")

# Titre et intro
st.markdown(styles.render_section_header("Performance Géographique de l'Écosystème Olist"), unsafe_allow_html=True)

st.markdown("""
**Analyse spatiale des transactions facilitées par Olist pour optimiser le service B2B.**

Cette analyse identifie :
- **Les régions performantes** : Où l'écosystème Olist génère le plus de satisfaction
- **Les zones à améliorer** : Où Olist peut développer de nouveaux services logistiques
- **Les flux commerciaux** : Patterns géographiques pour optimiser les intégrations marketplace
""")

st.markdown("---")

st.markdown(textes.analyse_carte_geo)

# Chargement du GeoJSON
@st.cache_resource
def load_geojson():
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    return requests.get(url).json()

geojson = load_geojson()

# Récupération des données par état
df_state = run_query(queries.QUERY_STATES_METRICS)

# Sélection du type d'analyse
analysis_type = st.selectbox(
    "Sélectionnez l'analyse affichée sur la carte :",
    [
        "Chiffre d'affaires",
        "Délai moyen",
        "Nombre de commandes",
        "Panier moyen",
        "Note moyenne"
    ]
)

metric_map = {
    "Chiffre d'affaires": ("revenue", "Chiffre d'affaires (R$)"),
    "Délai moyen": ("avg_delivery_days", "Délai moyen (jours)"),
    "Nombre de commandes": ("nb_orders", "Nombre de commandes"),
    "Panier moyen": ("avg_order_value", "Panier moyen (R$)"),
    "Note moyenne": ("avg_review_score", "Note moyenne"),
}

metric_col, metric_title = metric_map[analysis_type]

# Carte choropleth
fig = visuel.plot_choropleth_map(df_state, geojson, metric_col, f"{analysis_type} par État")
st.plotly_chart(fig, use_container_width=True)
