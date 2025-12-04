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

# Explications contextuelles pour chaque métrique
metric_explanations = {
    "Chiffre d'affaires": """
    **Analyse du Chiffre d'Affaires par État**
    
    Cette visualisation identifie les **marchés les plus rentables** de l'écosystème Olist. L'analyse révèle une concentration sur les grands centres urbains (SP, RJ, MG) mais met en évidence des **opportunités d'expansion** dans les régions sous-représentées.
    
    **Insights clés :**
    - Identifier les états à fort potentiel démographique mais faible pénétration Olist
    - Évaluer le ROI potentiel d'investissements commerciaux par région
    - Optimiser l'allocation des ressources de développement commercial
    
    **Recommandation analytique :** Croiser ces données avec les indicateurs démographiques et économiques pour prioriser l'expansion géographique.
    """,
    
    "Délai moyen": """
    **Performance Logistique par Région**
    
    Les délais de livraison constituent un **facteur critique de compétitivité** dans l'e-commerce brésilien. Cette analyse géographique révèle des disparités importantes qui impactent directement la satisfaction client et la performance des vendeurs.
    
    **Constats analytiques :**
    - Forte corrélation entre proximité géographique des hubs logistiques et performance de livraison
    - Impact direct sur les notes clients : +10 jours de délai = -15% de satisfaction moyenne
    - Avantage concurrentiel marqué pour les régions Sud/Sud-Est
    
    **Optimisation suggérée :** Développement de centres de distribution régionaux pour réduire les écarts de performance logistique.
    """,
    
    "Nombre de commandes": """
    **Analyse du Volume Transactionnel**
    
    Cette métrique révèle la **maturité du marché** Olist par région et identifie les zones de croissance potentielle. Le volume de commandes reflète à la fois la pénétration de la plateforme et la dynamique économique locale.
    
    **Observations data-driven :**
    - Corrélation positive entre densité urbaine et volume de transactions
    - Identification de marchés émergents avec fort potentiel de développement
    - Évaluation de la saturation relative des marchés matures
    
    **Applications business :** Utiliser ces insights pour calibrer les investissements marketing et commercial par région.
    """,
    
    "Panier moyen": """
    **Analyse de la Valeur Transactionnelle**
    
    Le panier moyen révèle le **pouvoir d'achat régional** et les opportunités de montée en gamme. Cette métrique guide les stratégies de pricing et de positionnement produit par zone géographique.
    
    **Insights économiques :**
    - Identification des régions à forte valeur ajoutée pour les vendeurs premium
    - Corrélation entre développement économique local et valeur des transactions
    - Opportunités d'optimisation de l'offre produit par segment géographique
    
    **Recommandation stratégique :** Adapter les campagnes de recrutement vendeurs selon le profil de valeur de chaque région.
    """,
    
    "Note moyenne": """
    **Indicateur de Satisfaction Globale**
    
    Les notes clients constituent le **baromètre de performance** de l'écosystème Olist. Cette analyse géographique révèle les zones d'excellence et les axes d'amélioration prioritaires pour maintenir la compétitivité de la plateforme.
    
    **Analyse de performance :**
    - Corrélation forte entre délais de livraison et satisfaction client
    - Impact des notes sur la visibilité des vendeurs dans les algorithmes de marketplace
    - Identification des régions nécessitant des actions correctives immédiates
    
    **Plan d'action data-driven :** Prioriser les améliorations logistiques dans les zones à faibles notes pour optimiser l'expérience client globale.
    """
}

metric_col, metric_title = metric_map[analysis_type]

# Carte choropleth
fig = visuel.plot_choropleth_map(df_state, geojson, metric_col, f"{analysis_type} par État")
st.plotly_chart(fig, use_container_width=True)

# Affichage de l'explication contextuelle selon la métrique sélectionnée
st.markdown(metric_explanations[analysis_type])
