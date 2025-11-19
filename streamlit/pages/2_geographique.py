import streamlit as st
from data import run_query
import plotly.express as px
import pandas as pd
import requests
import plotly.graph_objects as go


# Coordonnées approximatives des capitales des États du Brésil
state_coords = {
    "AC": (-9.97499, -67.8243),
    "AL": (-9.66599, -35.735),
    "AM": (-3.13159, -60.02),
    "AP": (0.034934, -51.0694),
    "BA": (-12.9718, -38.5011),
    "CE": (-3.71722, -38.5434),
    "DF": (-15.7797, -47.9297),
    "ES": (-20.3155, -40.3128),
    "GO": (-16.6864, -49.2643),
    "MA": (-2.53874, -44.2825),
    "MG": (-19.9167, -43.9345),
    "MS": (-20.4428, -54.6464),
    "MT": (-15.5989, -56.0949),
    "PA": (-1.45583, -48.5039),
    "PB": (-7.1195, -34.845),
    "PE": (-8.04666, -34.8771),
    "PI": (-5.08921, -42.8016),
    "PR": (-25.4284, -49.2733),
    "RJ": (-22.9068, -43.1729),
    "RN": (-5.79448, -35.211),
    "RO": (-8.76077, -63.8999),
    "RR": (2.81972, -60.6733),
    "RS": (-30.0331, -51.23),
    "SC": (-27.5945, -48.5477),
    "SE": (-10.9167, -37.05),
    "SP": (-23.5505, -46.6333),
    "TO": (-10.1841, -48.3336),
}







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



st.markdown("---")
st.header("🔄 Flux géographiques des ventes (Vendeur → Client)")

# Sélection top flux
top_n = st.slider("Nombre de flux à afficher :", 10, 200, 50)

# Requête SQL flux
query_flux = """
    SELECT 
        s.seller_state,
        c.customer_state,
        COUNT(*) AS nb_orders
    FROM clean_order_items coi
    JOIN clean_sellers s ON coi.seller_id = s.seller_id
    JOIN clean_orders o ON coi.order_id = o.order_id
    JOIN clean_customers c ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
    GROUP BY s.seller_state, c.customer_state
    HAVING nb_orders > 0
    ORDER BY nb_orders DESC
    LIMIT {n};
""".format(n=top_n)

df_flux = run_query(query_flux)

# Construction des arcs
lines = []
for _, row in df_flux.iterrows():
    s_state = row["seller_state"]
    c_state = row["customer_state"]

    if s_state not in state_coords or c_state not in state_coords:
        continue

    s_lat, s_lon = state_coords[s_state]
    c_lat, c_lon = state_coords[c_state]

    lines.append(
        go.Scattergeo(
            locationmode="ISO-3",
            lon=[s_lon, c_lon],
            lat=[s_lat, c_lat],
            mode="lines",
            line=dict(width=max(1, row["nb_orders"] / df_flux["nb_orders"].max() * 6)),
            opacity=0.6,
            hoverinfo="text",
            text=f"{s_state} → {c_state}<br>Commandes : {row['nb_orders']}",
        )
    )

# Ajout titre
fig_flux = go.Figure(lines)

fig_flux.update_layout(
    title_text="Flux des commandes entre États brésiliens",
    showlegend=False,
    geo=dict(
        scope="south america",
        projection_type="mercator",
        showland=True,
        landcolor="rgb(240, 240, 240)",
        countrycolor="white",
    ),
    margin=dict(l=0, r=0, t=40, b=0)
)

st.plotly_chart(fig_flux, use_container_width=True)

