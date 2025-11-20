import streamlit as st
from data import load_table
import pandas as pd

# ----------- CONFIG -----------
st.set_page_config(
    page_title="Olist Dashboard",
    layout="wide"
)

# ----------- CSS DESIGN (style PowerBI) -----------
st.markdown("""
<style>

    /* KPI cards */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 18px;
        margin: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.08);
        border: 1px solid #E6E6E6;
    }

    /* Titles */
    h1, h2, h3 {
        color: #1F77B4 !important;
        font-weight: 600;
    }

    /* Remove footer */
    footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ----------- TITLE -----------
st.title("📊 Olist E-Commerce Dashboard")
st.markdown("### Analyse des performances commerciales & clients")

st.write("")
st.write("")

# ----------- LOAD DATA (extrait KPI) -----------
orders = load_table("clean_orders")
order_items = load_table("clean_order_items")
reviews = load_table("clean_reviews")

# Revenue total
total_revenue = (order_items["price"] + order_items["freight_value"]).sum()

# Nb commandes
nb_orders = orders["order_id"].nunique()

# Note moyenne
avg_score = reviews["review_score"].mean()

# Délai moyen
orders_valid = orders[
    (orders["order_status"].isin(["delivered", "shipped", "invoiced"])) &
    orders["order_delivered_customer_date"].notna()
]

delivery_delay = (
    pd.to_datetime(orders_valid["order_delivered_customer_date"]) -
    pd.to_datetime(orders_valid["order_purchase_timestamp"])
).dt.days.mean()

# ----------- KPI SECTION -----------
st.markdown("## 🧮 Indicateurs Clés")

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Revenue Total", f"{total_revenue:,.0f} R$")
col2.metric("🛍️ Nombre de Commandes", f"{nb_orders:,}")
col3.metric("⭐ Note Moyenne", f"{avg_score:.2f} / 5")
col4.metric("🚚 Délai Moyen", f"{delivery_delay:.2f} jours")

st.write("")
st.markdown("---")
st.write("")

# ----------- INTRO ANALYTIQUE -----------
st.markdown("## 📝 Résumé Analyse")

st.markdown("""
Cette application présente une analyse complète des données Olist :

● **Performance business** (revenue, commandes, délai, satisfaction)  
● **Analyse géographique** (vente par état, délais régionaux, flux seller → client)  
● **Analyse produits** (best sellers, catégories lentes, satisfaction)  
● **Analyse client** (bad reviews, comportements clés)  
● **Recommandations stratégiques** basées sur les insights  

👉 Utilise le menu à gauche pour naviguer entre les différentes sections.
""")
