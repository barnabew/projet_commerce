import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_table, get_connection, run_query
import styles
import queries



THEME_CONFIG = {
    "paper_bgcolor": "#252936",
    "plot_bgcolor": "#252936",
    "font": dict(color="#ffffff"),
    "title": dict(font=dict(color="#ffffff")),
    "xaxis": dict(gridcolor="#2d3142"),
    "yaxis": dict(gridcolor="#2d3142")
}

def apply_theme(fig):
    """Applique le thème sombre à un graphique Plotly"""
    fig.update_layout(**THEME_CONFIG)
    return fig





# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)




st.markdown("---")

# Objectif du Dashboard
with st.expander("Recommandations", expanded=False):
    st.markdown("""
    ## Stratégie : Optimisation de l'Expérience Unique
    
    L'analyse des données révèle que l'optimisation doit se concentrer sur l'excellence de l'expérience unique 
    plutôt que sur la fidélisation client. L'objectif principal est d'améliorer la satisfaction client grâce 
    aux insights extraits des données.
    
    ## Corrélations Identifiées dans les Données
    
    L'analyse révèle deux corrélations majeures avec la satisfaction client. La plus forte corrélation 
    concerne les délais de livraison. Par ailleurs, 25% des notes négatives se concentrent sur 
    seulement 10% des produits, suggérant des problèmes spécifiques à certaines catégories.
                    
    ## Recommandations Basées sur l'Analyse des Données

    **Optimisation des délais de livraison**
    
    La corrélation la plus forte identifiée dans les données concerne la relation entre délais et satisfaction. 
    Cette relation suggère que l'amélioration des délais de livraison pourrait avoir un impact significatif 
    sur la satisfaction client. Les métriques à suivre incluent le pourcentage de commandes livrées en moins 
    de 7 jours et le délai moyen par états.

    **Amélioration du mix catégories**
    
    Les données montrent une concentration des problèmes sur un faible nombre de catégories. Une optimisation 
    ciblée de ces catégories problématiques pourrait améliorer la satisfaction globale.
        """)

st.markdown("---")

# Récupération des données KPI (avec cache) - Performance Écosystème Olist
pct_5_stars = run_query(queries.QUERY_PERCENT_5_STARS)["pct_5_stars"][0]
pct_fast = run_query(queries.QUERY_PERCENT_FAST_DELIVERY)["pct_fast"][0]
avg_delivery_delay = run_query(queries.QUERY_AVG_DELIVERY_DELAY)["delay"][0]
avg_score = run_query(queries.QUERY_AVG_REVIEW_SCORE)["avg"][0]
total_orders = run_query(queries.QUERY_TOTAL_ORDERS)["c"][0]

# Affichage des 5 KPI
kpi_cols = st.columns(5, gap="medium")

with kpi_cols[0]:
    st.markdown(styles.render_kpi_card("Excellence (5★)", f"{pct_5_stars}%"), unsafe_allow_html=True)

with kpi_cols[1]:
    st.markdown(styles.render_kpi_card("Livraisons Rapides (<7j)", f"{pct_fast}%"), unsafe_allow_html=True)

with kpi_cols[2]:
    st.markdown(styles.render_kpi_card("Délai Moyen", f"{avg_delivery_delay:.1f} jours"), unsafe_allow_html=True)

with kpi_cols[3]:
    st.markdown(styles.render_kpi_card("Score Satisfaction", f"{avg_score:.1f}/5"), unsafe_allow_html=True)

with kpi_cols[4]:
    st.markdown(styles.render_kpi_card("Total Commandes", f"{total_orders:,}"), unsafe_allow_html=True)



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
    apply_theme(fig_delay_sat)
    st.plotly_chart(fig_delay_sat, use_container_width=True)

with chart_row1[1]:
    # États avec les pires délais de livraison (zones à améliorer)
    df_states_metrics = run_query(queries.QUERY_STATES_METRICS)
    df_worst_states_delay = df_states_metrics[df_states_metrics['nb_orders'] > 50].nlargest(10, 'avg_delivery_days')
    
    fig_worst_states_delay = px.bar(
        df_worst_states_delay,
        x="state",
        y="avg_delivery_days",
        title="États avec les Pires Délais de Livraison (Zones à Améliorer)",
        labels={"state": "État", "avg_delivery_days": "Délai moyen (jours)"}
    )
    apply_theme(fig_worst_states_delay)
    st.plotly_chart(fig_worst_states_delay, use_container_width=True)

chart_row2 = st.columns(2, gap="large")

with chart_row2[0]:
    # Catégories avec le plus de notes 1 étoile (problèmes critiques)
    df_categories_1_star = run_query(queries.QUERY_CATEGORIES_1_STAR)
    
    fig_worst_categories_1_star = px.bar(
        df_categories_1_star,
        x="pct_1_stars",
        y="category",
        orientation="h",
        title="Catégories avec le Plus de Notes 1 Étoile (Problèmes Critiques)",
        labels={"pct_1_stars": "% Notes 1 étoile", "category": "Catégorie"}
    )
    apply_theme(fig_worst_categories_1_star)
    st.plotly_chart(fig_worst_categories_1_star, use_container_width=True)

with chart_row2[1]:
    # Distribution des délais de livraison
    df_delivery = run_query(queries.QUERY_DELIVERY_DISTRIBUTION)
    
    fig_delivery = px.bar(
        df_delivery,
        x="delay_range",
        y="nb_orders",
        title="Distribution des Délais de Livraison",
        labels={"delay_range": "Délai de livraison", "nb_orders": "Nombre de commandes"}
    )
    apply_theme(fig_delivery)
    st.plotly_chart(fig_delivery, use_container_width=True)
