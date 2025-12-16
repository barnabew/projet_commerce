import streamlit as st
import pandas as pd
import plotly.express as px
from utils import run_query
import styles
import textes
import visuel
import queries

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="temporel")

st.markdown(styles.render_section_header("Analyse Temporelle & Saisonnalité"), unsafe_allow_html=True)
st.markdown(textes.intro_temporel)

# Section 1: Évolution mensuelle globale
with st.expander("Évolution Mensuelle Globale", expanded=True):
    df_mensuel = run_query(queries.QUERY_EVOLUTION_MENSUELLE)
    
    fig = px.line(
        df_mensuel,
        x="Mois",
        y="CA_Moyen_Hebdo",
        title="Évolution du CA Moyen Hebdomadaire par Mois",
        labels={"Mois": "Mois", "CA_Moyen_Hebdo": "CA Moyen Hebdomadaire ($)"},
        markers=True
    )
    fig.update_traces(line_width=4, marker_size=8)
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(textes.insight_evolution_globale)

# Section 2: Performance par type de magasin
with st.expander("Évolution par Type de Magasin", expanded=False):
    df_types_evolution = run_query(queries.QUERY_EVOLUTION_BY_TYPE)
    
    fig = px.line(
        df_types_evolution,
        x="Nom_Mois",
        y=["Type_A", "Type_B", "Type_C"],
        title="Évolution Comparative par Type de Magasin",
        labels={"Nom_Mois": "Mois", "value": "CA Moyen Hebdomadaire ($)"},
        markers=True
    )
    
    # Personnalisation couleurs
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']
    for i, trace in enumerate(fig.data):
        trace.line.color = colors[i]
        trace.line.width = 3.5
        trace.name = f"Type {['A', 'B', 'C'][i]}"
    
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(textes.insight_evolution_types)

# Section 3: Départements saisonniers
with st.expander("Départements Saisonniers – Opportunités Temporelles", expanded=False):
    st.markdown(textes.analyse_saisonnalite)
    
    # Seuil de variation saisonnière
    seuil_variation = st.slider("Coefficient de variation minimum (%) :", 50, 200, 130, key="slider_saison")
    
    df_saisonniers = run_query(queries.get_query_departements_saisonniers(seuil_variation))
    
    # Graphique en barres du coefficient de variation
    fig_variation = px.bar(
        df_saisonniers.head(10),
        x="Dept",
        y="Coefficient_Variation",
        title="Top 10 Départements les Plus Saisonniers",
        labels={"Dept": "Département", "Coefficient_Variation": "Coefficient de Variation (%)"}
    )
    visuel.apply_theme(fig_variation)
    st.plotly_chart(fig_variation, use_container_width=True)
    
    # Évolution détaillée des top départements saisonniers
    top_depts = df_saisonniers.head(6)['Dept'].tolist()
    if top_depts:
        df_evolution_depts = run_query(queries.get_query_evolution_top_depts(top_depts))
        
        # Préparation données pour le graphique
        dept_columns = [f'Dept_{dept}' for dept in top_depts]
        
        fig_depts = px.line(
            df_evolution_depts,
            x="Nom_Mois",
            y=dept_columns,
            title=f"Évolution Saisonnière des Top {len(top_depts)} Départements",
            labels={"Nom_Mois": "Mois", "value": "CA Moyen Hebdomadaire ($)"},
            markers=True
        )
        
        # Couleurs distinctives
        colors_depts = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
        for i, trace in enumerate(fig.data):
            if i < len(colors_depts):
                trace.line.color = colors_depts[i]
            trace.line.width = 3
            # Renommer pour afficher juste le numéro du département
            trace.name = f"Dept {top_depts[i]}"
        
        visuel.apply_theme(fig_depts)
        st.plotly_chart(fig_depts, use_container_width=True)

# Section 4: Impact des promotions
with st.expander("Impact des Promotions sur les Ventes", expanded=False):
    df_promotions = run_query(queries.QUERY_IMPACT_PROMOTIONS)
    
    fig_promo = px.bar(
        df_promotions,
        x="Statut_Promo",
        y="CA_Moyen",
        title="Impact des Promotions sur le CA Moyen",
        labels={"Statut_Promo": "Statut Promotion", "CA_Moyen": "CA Moyen ($)"},
        color="CA_Moyen",
        color_continuous_scale="viridis"
    )
    visuel.apply_theme(fig_promo)
    st.plotly_chart(fig_promo, use_container_width=True)
    
    # Calcul de l'impact
    if len(df_promotions) == 2:
        impact = df_promotions[df_promotions['Statut_Promo'] == 'Avec Promo']['CA_Moyen'].iloc[0]
        baseline = df_promotions[df_promotions['Statut_Promo'] == 'Sans Promo']['CA_Moyen'].iloc[0]
        lift = (impact / baseline - 1) * 100
        
        if lift > 0:
            st.success(f"Impact positif des promotions : +{lift:.1f}% de CA moyen")
        else:
            st.warning(f"Impact négatif des promotions : {lift:.1f}% de CA moyen")
    
    st.markdown(textes.insight_promotions)