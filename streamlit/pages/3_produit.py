import streamlit as st
import pandas as pd
import plotly.express as px
from utils import run_query
import styles
import visuel
import queries
import textes

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="produit")

st.markdown(styles.render_section_header("Analyse Produits Écosystème Olist"), unsafe_allow_html=True)
st.markdown(textes.intro_produits)

# Section 1: Catégories championnes - % de 5 étoiles
with st.expander("Catégories Championnes – Créatrices d'Ambassadeurs", expanded=True):
    st.markdown(textes.analyse_categories_championnes)
    
    min_sales_champ = st.slider("Min reviews par catégorie :", 50, 500, 100, key="slider_champ")
    
    df_5_stars = run_query(queries.get_query_percent_5_stars_by_category(min_sales_champ))

    fig = px.bar(
        df_5_stars.head(15),
        x="pct_5_stars",
        y="category",
        orientation="h",
        title="Top 15 catégories – % de 5 étoiles (expérience parfaite)",
        labels={"pct_5_stars": "% de 5 étoiles", "category": "Catégorie"}
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 2: Catégories à risque - Faible % de 5 étoiles
with st.expander("Catégories À Risque – Génératrices de Détracteurs", expanded=False):
    st.markdown(textes.analyse_categories_a_risque)
    
    min_sales_risk = st.slider("Min reviews par catégorie :", 50, 500, 100, key="slider_risk")
    
    df_5_stars_bottom = run_query(queries.get_query_percent_5_stars_by_category(min_sales_risk))

    fig = px.bar(
        df_5_stars_bottom.tail(15).iloc[::-1],  # Prendre les 15 derniers et inverser l'ordre
        x="pct_5_stars",
        y="category",
        orientation="h",
        title="Bottom 15 catégories – % de 5 étoiles (expérience décevante)",
        labels={"pct_5_stars": "% de 5 étoiles", "category": "Catégorie"}
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
