import streamlit as st
from data import run_query,get_connection
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










st.title("🌐 Flux Géographiques – Vendeur → Client")

st.write(
    "Analyse des flux logistiques entre les états vendeurs et les états "
    "des clients, basée sur les commandes livrées."
)

# -------------------------------------
# Requête SQL
# -------------------------------------
query_flux = """
SELECT 
    s.seller_state,
    c.customer_state,
    COUNT(*) AS nb_orders,
    ROUND(AVG(
        JULIANDAY(o.order_delivered_customer_date) 
        - JULIANDAY(o.order_purchase_timestamp)
    ), 2) AS avg_delivery_days
FROM clean_order_items coi
JOIN clean_sellers s 
    ON coi.seller_id = s.seller_id
JOIN clean_orders o 
    ON coi.order_id = o.order_id
JOIN clean_customers c 
    ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
  AND o.order_purchase_timestamp IS NOT NULL
GROUP BY s.seller_state, c.customer_state
HAVING nb_orders > 10
ORDER BY nb_orders DESC;
"""

conn = get_connection()
df = pd.read_sql(query_flux, conn)

# -------------------------------------
# Vérification & nettoyage
# -------------------------------------
df = df.dropna(subset=["seller_state", "customer_state"])

states = sorted(set(df["seller_state"]).union(df["customer_state"]))

# Mapping index → état
index_map = {state: i for i, state in enumerate(states)}

# -------------------------------------
# Construction de la matrice de flux
# -------------------------------------
matrix = [[0]*len(states) for _ in range(len(states))]

for _, row in df.iterrows():
    s = row["seller_state"]
    t = row["customer_state"]
    w = row["nb_orders"]
    matrix[index_map[s]][index_map[t]] = w

# -------------------------------------
# Diagramme chord-like (Sankey simplifié)
# -------------------------------------
sources = [index_map[s] for s in df["seller_state"]]
targets = [index_map[t] + len(states) for t in df["customer_state"]]
weights = df["nb_orders"].astype(float).tolist()

labels = states + states  # vendeurs + clients

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=labels,
        color="blue"
    ),
    link=dict(
        source=sources,
        target=targets,
        value=weights,
        color="rgba(0, 100, 255, 0.4)"
    )
)])

fig.update_layout(
    title="Flux entre États (Sankey simplifié)",
    font=dict(size=12)
)

st.plotly_chart(fig, use_container_width=True)

# -------------------------------------
# Tableau récapitulatif
# -------------------------------------
st.subheader("📋 Tableau des flux")
st.dataframe(df)
