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

st.markdown(styles.render_section_header("Produits et Première Impression"), unsafe_allow_html=True)
st.markdown(textes.intro_produits)

# Section 1: Catégories championnes - % de 5 étoiles
with st.expander("🌟 Catégories Championnes – Créatrices d'Ambassadeurs", expanded=True):
    st.markdown(textes.analyse_categories_championnes)
    
    min_sales_champ = st.slider("Min reviews par catégorie :", 50, 500, 100, key="slider_champ")
    
    df_5_stars = run_query(queries.get_query_percent_5_stars_by_category(min_sales_champ))

    fig = px.bar(
        df_5_stars.head(15),
        x="pct_5_stars",
        y="category",
        orientation="h",
        title="Top 15 catégories – % de 5 étoiles (expérience parfaite)",
        labels={"pct_5_stars": "% de 5 étoiles", "category": "Catégorie"},
        color="pct_5_stars",
        color_continuous_scale=[[0, "#ff4b4b"], [0.5, "#ffa500"], [1, "#00cc66"]]
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 2: Catégories à risque - Faible % de 5 étoiles
with st.expander("⚠️ Catégories À Risque – Génératrices de Détracteurs", expanded=False):
    st.markdown(textes.analyse_categories_a_risque)
    
    min_sales_risk = st.slider("Min reviews par catégorie :", 50, 500, 100, key="slider_risk")
    
    df_5_stars_bottom = run_query(queries.get_query_percent_5_stars_by_category(min_sales_risk))

    fig = px.bar(
        df_5_stars_bottom.tail(15).iloc[::-1],  # Prendre les 15 derniers et inverser l'ordre
        x="pct_5_stars",
        y="category",
        orientation="h",
        title="Bottom 15 catégories – % de 5 étoiles (expérience décevante)",
        labels={"pct_5_stars": "% de 5 étoiles", "category": "Catégorie"},
        color="pct_5_stars",
        color_continuous_scale=[[0, "#ff4b4b"], [0.5, "#ffa500"], [1, "#00cc66"]]
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 3: Impact des délais sur la première impression
with st.expander("⏱️ Impact des Délais sur la Première Impression", expanded=False):
    st.markdown(textes.analyse_impact_delais_produits)
    
    min_sales_delay = st.slider("Min ventes par catégorie :", 20, 500, 50, key="slider_delay")

    df_delivery = run_query(queries.get_query_delivery_by_category(min_sales_delay))

    fig = px.bar(
        df_delivery.head(15),
        x="avg_delivery_days",
        y="category",
        orientation="h",
        title="Catégories les plus lentes – Délai moyen de livraison",
        labels={"avg_delivery_days": "Délai moyen (jours)", "category": "Catégorie"},
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 4: Recommandations
with st.expander("💡 Recommandations Data-Driven", expanded=False):
    st.markdown(textes.analyse_recommandations_produits)
