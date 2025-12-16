import streamlit as st
from utils import run_query
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import styles
import textes
import visuel
import queries

st.session_state["page"] = "magasins"

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="magasins")

# Titre et intro
st.markdown(styles.render_section_header("Analyse par Type de Magasin"), unsafe_allow_html=True)

st.markdown("""
**Typologie des magasins selon leur taille et performance pour optimiser les stratégies d'assortiment.**

Cette analyse identifie :
- **Les patterns de performance** : Comment la taille influence les résultats
- **Les spécificités par type** : Stratégies différenciées A, B, C
- **Les opportunités d'optimisation** : Leviers par segment de magasin
""")

st.markdown("---")

# Récupération des données par type
df_types = run_query(queries.QUERY_TYPES_DETAILED)

# Sélection du type d'analyse
analysis_type = st.selectbox(
    "Sélectionnez l'analyse :",
    [
        "Vue d'ensemble",
        "Corrélation taille-performance", 
        "Performance départementale par type",
        "Évolution temporelle par type"
    ]
)

if analysis_type == "Vue d'ensemble":
    # KPIs par type
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("Type A (Grands)")
        type_a = df_types[df_types['Type'] == 'A'].iloc[0]
        st.metric("Magasins", f"{type_a['Nb_Magasins']}")
        st.metric("Taille moyenne", f"{type_a['Taille_Moyenne']:,.0f} sqft")
        st.metric("CA moyen", f"${type_a['CA_Moyen']:,.0f}")
    
    with col2:
        st.subheader("Type B (Moyens)")
        type_b = df_types[df_types['Type'] == 'B'].iloc[0]
        st.metric("Magasins", f"{type_b['Nb_Magasins']}")
        st.metric("Taille moyenne", f"{type_b['Taille_Moyenne']:,.0f} sqft")
        st.metric("CA moyen", f"${type_b['CA_Moyen']:,.0f}")
    
    with col3:
        st.subheader("Type C (Petits)")
        type_c = df_types[df_types['Type'] == 'C'].iloc[0]
        st.metric("Magasins", f"{type_c['Nb_Magasins']}")
        st.metric("Taille moyenne", f"{type_c['Taille_Moyenne']:,.0f} sqft")
        st.metric("CA moyen", f"${type_c['CA_Moyen']:,.0f}")

elif analysis_type == "Corrélation taille-performance":
    df_correlation = run_query(queries.QUERY_TAILLE_PERFORMANCE)
    
    fig = px.scatter(
        df_correlation,
        x="Size",
        y="CA_Moyen",
        color="Type",
        title="Corrélation Taille vs Performance (avec ligne de tendance)",
        labels={"Size": "Taille (sqft)", "CA_Moyen": "CA Moyen Hebdomadaire ($)"},
        trendline="ols"
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
    
    # Calcul de la corrélation
    correlation = df_correlation['Size'].corr(df_correlation['CA_Moyen'])
    st.info(f"Coefficient de corrélation : {correlation:.3f}")
    
    st.markdown(textes.analyse_correlation)

elif analysis_type == "Performance départementale par type":
    df_dept_by_type = run_query(queries.QUERY_DEPT_BY_TYPE)
    
    # Graphique des top départements par type
    for store_type in ['A', 'B', 'C']:
        type_data = df_dept_by_type[df_dept_by_type['Type'] == store_type].head(8)
        
        fig = px.bar(
            type_data,
            x="CA_Total",
            y="Dept",
            orientation="h",
            title=f"Top 8 Départements - Type {store_type}",
            labels={"CA_Total": "CA Total ($)", "Dept": "Département"}
        )
        visuel.apply_theme(fig)
        st.plotly_chart(fig, use_container_width=True)

elif analysis_type == "Évolution temporelle par type":
    df_evolution_types = run_query(queries.QUERY_EVOLUTION_BY_TYPE)
    
    fig = px.line(
        df_evolution_types,
        x="Nom_Mois",
        y=["Type_A", "Type_B", "Type_C"],
        title="Évolution du CA Hebdomadaire par Type de Magasin",
        labels={"Nom_Mois": "Mois", "value": "CA Moyen Hebdomadaire ($)"},
        markers=True
    )
    
    # Personnalisation des couleurs
    colors = {'Type_A': '#FF6B6B', 'Type_B': '#4ECDC4', 'Type_C': '#45B7D1'}
    for i, trace in enumerate(fig.data):
        trace.line.color = list(colors.values())[i]
        trace.line.width = 3.5
    
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(textes.analyse_evolution_types)