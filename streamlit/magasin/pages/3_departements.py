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
styles.render_navbar(st, current_page="departements")

st.markdown(styles.render_section_header("Analyse Départements & Assortiment"), unsafe_allow_html=True)
st.markdown(textes.intro_departements)

# Section 1: Segmentation des départements
with st.expander("Segmentation Départements – Classification Stratégique", expanded=True):
    st.markdown(textes.analyse_segmentation_depts)
    
    df_segmentation = run_query(queries.QUERY_SEGMENTATION_DEPARTEMENTS)

    fig = px.pie(
        df_segmentation,
        values="Nb_Depts",
        names="Categorie",
        title="Répartition des Départements par Catégorie"
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
    
    # Tableau détaillé
    st.subheader("Détail par Catégorie")
    st.dataframe(df_segmentation, use_container_width=True)

# Section 2: Champions départementaux
with st.expander("Départements Champions – Top Performers", expanded=False):
    st.markdown(textes.analyse_champions)
    
    min_presence = st.slider("Seuil minimum de présence (%) :", 10, 100, 50, key="slider_champions")
    
    df_champions = run_query(queries.get_query_departements_champions(min_presence))

    fig = px.bar(
        df_champions.head(15),
        x="CA_Total",
        y="Dept",
        orientation="h",
        title="Top 15 Départements Champions (CA Total)",
        labels={"CA_Total": "Chiffre d'affaires total ($)", "Dept": "Département"}
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 3: Départements spécialisés
with st.expander("Départements Spécialisés – Niches Rentables", expanded=False):
    st.markdown(textes.analyse_specialises)
    
    max_presence = st.slider("Seuil maximum de présence (%) :", 10, 50, 30, key="slider_specialises")
    
    df_specialises = run_query(queries.get_query_departements_specialises(max_presence))

    fig = px.scatter(
        df_specialises,
        x="Taux_Presence",
        y="CA_Moyen_Magasin",
        size="CA_Total",
        hover_data=["Dept", "Nb_Magasins"],
        title="Départements Spécialisés : Exclusivité vs Performance",
        labels={
            "Taux_Presence": "Taux de présence (%)",
            "CA_Moyen_Magasin": "CA moyen par magasin ($)"
        }
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 4: Performance par type de magasin
with st.expander("Performance Départementale par Type de Magasin", expanded=False):
    st.markdown(textes.analyse_perf_par_type)
    
    type_selected = st.selectbox("Choisissez un type de magasin :", ["A", "B", "C"])
    
    df_perf_type = run_query(queries.get_query_perf_by_type(type_selected))

    fig = px.bar(
        df_perf_type.head(10),
        x="Dept",
        y="CA_Moyen",
        title=f"Top 10 Départements - Magasins Type {type_selected}",
        labels={"Dept": "Département", "CA_Moyen": "CA Moyen ($)"}
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)