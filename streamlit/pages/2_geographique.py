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
    **Concentration Géographique du Chiffre d'Affaires**
    
    L'analyse révèle une forte concentration du chiffre d'affaires dans l'axe São Paulo - Rio de Janeiro - Minas Gerais, qui constitue le cœur économique de l'écosystème Olist. Cette polarisation reflète à la fois la densité démographique et le développement économique de ces régions.
    
    Les états du Nord présentent des performances nettement inférieures, illustrant les disparités économiques régionales du Brésil. Cette distribution géographique met en évidence les opportunités d'expansion dans les marchés sous-représentés, où le potentiel de croissance reste significatif malgré les défis logistiques.
    
    Cette cartographie du chiffre d'affaires constitue un indicateur clé pour orienter les stratégies de développement commercial et d'allocation des ressources.
    """,
    
    "Délai moyen": """
    **Impact de la Distance et des Infrastructures sur les Délais de Livraison**
    
    L'état de São Paulo bénéficie des délais de livraison les plus courts grâce à la concentration des infrastructures logistiques et des centres de distribution. Cette proximité des hubs logistiques se traduit par une performance opérationnelle optimale.
    
    Les états du Nord subissent des délais jusqu'à quatre fois supérieurs, révélant l'impact combiné de la distance géographique et des limitations infrastructurelles. La géographie amazonienne complexifie davantage l'acheminement des marchandises vers ces régions.
    
    Cette corrélation entre éloignement géographique et dégradation des performances de livraison souligne l'importance critique du maillage logistique dans la stratégie d'expansion nationale d'Olist.
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
