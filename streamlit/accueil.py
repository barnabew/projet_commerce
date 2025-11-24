import streamlit as st
from data import load_table
import pandas as pd
import numpy as np

# ------------------------------
# PAGE CONFIG
# ------------------------------
st.set_page_config(page_title="Résumé", layout="wide")

# ------------------------------
# NAVBAR CSS + HTML
# ------------------------------
nav_html = """
<style>
/* Hide Streamlit default */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Top navbar */
.navbar {
    background-color: #0d1b2a;
    padding: 12px 25px;
    display: flex;
    gap: 30px;
    border-radius: 8px;
    margin-bottom: 25px;
    margin-left: 5%;
    margin-right: 5%;
}

.navbtn {
    color: #e0e6ed;
    font-size: 17px;
    text-decoration: none;
    font-weight: 500;
    padding: 8px 16px;
}

.navbtn:hover {
    background-color: #1b263b;
    border-radius: 6px;
}

.nav-active {
    background-color: #415a77;
    border-radius: 6px;
}
</style>

<div class="navbar">
    <a class="navbtn nav-active" href="/Accueil">Résumé</a>
    <a class="navbtn" href="/geographique">Géographique</a>
    <a class="navbtn" href="/produit">Produits</a>
    <a class="navbtn" href="/clients">Clients</a>
    <a class="navbtn" href="/recommandations">Recommandations</a>
</div>
"""
st.markdown(nav_html, unsafe_allow_html=True)

# ------------------------------
# DATA
# ------------------------------
orders = load_table("clean_orders")
order_items = load_table("clean_order_items")
reviews = load_table("clean_reviews")

# Revenue
orders_with_price = order_items.merge(
    orders[["order_id", "order_status"]],
    on="order_id"
)
orders_valid = orders_with_price[
    orders_with_price["order_status"].isin(["delivered", "shipped", "invoiced"])
]
revenue = (orders_valid["price"] + orders_valid["freight_value"]).sum()

# KPIs
total_orders = orders["order_id"].nunique()
avg_score = reviews["review_score"].mean()
avg_delivery = (pd.to_datetime(orders["order_delivered_customer_date"]) -
                pd.to_datetime(orders["order_purchase_timestamp"])
               ).dt.days.mean()

# ------------------------------
# TITLE
# ------------------------------
st.markdown(
    "<h1 style='text-align:center; color:white; margin-bottom:15px;'>📊 OLIST DASHBOARD — Résumé</h1>",
    unsafe_allow_html=True
)

# ------------------------------
# KPI CARDS
# ------------------------------
def metric_card(title, value):
    st.markdown(
        f"""
        <div style="
            background-color:#1b263b;
            padding:20px;
            border-radius:12px;
            text-align:center;
            color:#e0e6ed;
            font-size:18px;
        ">
            <div style='font-size:14px; opacity:0.8;'>{title}</div>
            <div style='font-size:28px; font-weight:600;'>{value}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

col1, col2, col3, col4 = st.columns(4)

with col1: metric_card("Revenu total", f"R$ {revenue:,.0f}")
with col2: metric_card("Commandes", f"{total_orders:,}")
with col3: metric_card("Note moyenne", f"{avg_score:.2f}")
with col4: metric_card("Délai moyen", f"{avg_delivery:.2f} jours")

st.write("")
st.write("")

# ------------------------------
# PLACEHOLDER FOR FUTURE GRAPHS
# ------------------------------
st.markdown("<h3 style='color:white;'>Graphiques (à remplir après validation)</h3>", unsafe_allow_html=True)

g1, g2 = st.columns(2)
g3, g4 = st.columns(2)

for g in [g1, g2, g3, g4]:
    with g:
        st.markdown(
            """
            <div style="
                background-color:#1b263b;
                height:180px;
                border-radius:12px;
                color:white;
                display:flex;
                align-items:center;
                justify-content:center;
                font-size:22px;
                opacity:0.6;
            ">
                Graphique
            </div>
            """,
            unsafe_allow_html=True
        )
