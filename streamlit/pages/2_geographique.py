import streamlit as st
from data import run_query
import plotly.express as px
import pandas as pd
import requests
import igraph as ig
import plotly.graph_objects as go









st.set_page_config(page_title="Analyse Géographique", layout="wide")

st.title("🌍 Analyse Géographique des Ventes Olist")

# ============================================================
# 🔹 GEOJSON
# ============================================================

@st.cache_resource
def load_geojson():
    url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
    return requests.get(url).json()

geojson = load_geojson()

# ============================================================
# 🔹 RÉCUPÉRATION DE TOUTES LES DONNÉES PAR ÉTAT
# ============================================================

query = """
    SELECT 
        c.customer_state AS state,
        COUNT(DISTINCT o.order_id) AS nb_orders,
        SUM(oi.price + oi.freight_value) AS revenue,
        ROUND(SUM(oi.price + oi.freight_value) * 1.0 
              / COUNT(DISTINCT o.order_id), 2) AS avg_order_value,
        ROUND(AVG(
            JULIANDAY(o.order_delivered_customer_date) 
            - JULIANDAY(o.order_purchase_timestamp)
        ), 2) AS avg_delivery_days,
        ROUND(AVG(r.review_score),2) AS avg_review_score
    FROM clean_orders o
    JOIN clean_customers c ON o.customer_id = c.customer_id
    JOIN clean_order_items oi ON oi.order_id = o.order_id
    LEFT JOIN clean_reviews r ON r.order_id = o.order_id
    WHERE o.order_status IN ('delivered','shipped','invoiced')
    GROUP BY c.customer_state;
"""

df_state = run_query(query)

# ============================================================
# 🔹 MENU DE L’ANALYSE À COLORER
# ============================================================

analysis_type = st.selectbox(
    "Sélectionnez l’analyse affichée sur la carte :",
    [
        "Chiffre d’affaires",
        "Délai moyen",
        "Nombre de commandes",
        "Panier moyen",
        "Note moyenne"
    ]
)

metric_map = {
    "Chiffre d’affaires": ("revenue", "Chiffre d’affaires (R$)"),
    "Délai moyen": ("avg_delivery_days", "Délai moyen (jours)"),
    "Nombre de commandes": ("nb_orders", "Nombre de commandes"),
    "Panier moyen": ("avg_order_value", "Panier moyen (R$)"),
    "Note moyenne": ("avg_review_score", "Note moyenne"),
}

metric_col, metric_title = metric_map[analysis_type]

# ============================================================
# 🔹 CARTE CHOROPLETH ENRICHIE
# ============================================================

fig = px.choropleth(
    df_state,
    geojson=geojson,
    locations="state",
    featureidkey="properties.sigla",
    color=metric_col,
    color_continuous_scale="Viridis",
    hover_data={
        "state": True,
        "nb_orders": True,
        "revenue": True,
        "avg_order_value": True,
        "avg_delivery_days": True,
        "avg_review_score": True,
        metric_col: True,
    },
    labels={
        "state": "État",
        "revenue": "CA (R$)",
        "nb_orders": "Nbre commandes",
        "avg_order_value": "Panier moyen",
        "avg_delivery_days": "Délai moyen",
        "avg_review_score": "Note moyenne"
    },
    title=f"{analysis_type} par État"
)

fig.update_geos(fitbounds="locations", visible=False)
fig.update_layout(margin={"r":0,"t":40,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)

# ============================================================
# 🔹 TABLEAU DE L'ÉTAT SÉLECTIONNÉ
# ============================================================

st.markdown("---")
st.subheader("🔎 Analyse détaillée par État")

state_select = st.selectbox(
    "Choisissez un État :",
    sorted(df_state["state"].unique())
)

st.dataframe(df_state[df_state["state"] == state_select])

st.set_page_config(page_title="Flux géographiques – Chord Diagram", layout="wide")

st.title("🔄 Flux géographiques des ventes – Chord Diagram")

st.markdown("""
Le diagramme chord montre les relations **vendeur → client** entre les États du Brésil.  
L'épaisseur du lien correspond au volume des commandes.  
""")

# ===============================================
# 1. Charger les flux
# ===============================================

query = """
    SELECT 
        s.seller_state AS source,
        c.customer_state AS target,
        COUNT(*) AS nb_orders
    FROM clean_order_items coi
    JOIN clean_sellers s ON coi.seller_id = s.seller_id
    JOIN clean_orders o ON coi.order_id = o.order_id
    JOIN clean_customers c ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
    GROUP BY s.seller_state, c.customer_state
    HAVING nb_orders > 0;
"""

df = run_query(query)

# Filtrer les flux trop petits
min_orders = st.slider("Filtrer les flux minimum :", 10, 500, 50)
df = df[df["nb_orders"] >= min_orders]

# ===============================================
# 2. Construire le Chord Diagram
# ===============================================

states = sorted(list(set(df["source"]) | set(df["target"])))
index_map = {state: i for i, state in enumerate(states)}

sources = df["source"].map(index_map)
targets = df["target"].map(index_map)
weights = df["nb_orders"]

# Création du graph igraph
g = ig.Graph()
g.add_vertices(states)
g.add_edges(list(zip(sources, targets)))
g.es["weight"] = weights

# Extraire matrices
matrix = [[0]*len(states) for _ in range(len(states))]
for _, row in df.iterrows():
    s = index_map[row["source"]]
    t = index_map[row["target"]]
    matrix[s][t] = row["nb_orders"]

# ===============================================
# 3. Plotly Chord (custom using Sankey logic)
# ===============================================

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=states,
        color="rgba(0, 100, 200, 0.8)"
    ),
    link=dict(
        source=sources,
        target=targets,
        value=weights,
        color=[
            f"rgba(0, 0, 150, {0.2 + 0.8*(w/max(weights))})"
            for w in weights
        ]
    )
)])

fig.update_layout(
    title="Chord Diagram – Flux Vendeur → Client (États du Brésil)",
    font=dict(size=14),
    height=900
)

st.plotly_chart(fig, use_container_width=True)

