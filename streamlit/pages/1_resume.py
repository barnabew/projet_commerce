import streamlit as st
import pandas as pd
import plotly.express as px
from data import load_table

# -----------------------------------------
# CONFIG
# -----------------------------------------
st.set_page_config(page_title="Résumé | Olist", layout="wide")

# -----------------------------------------
# CSS design type Geckoboard / PowerBI
# -----------------------------------------
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


# -----------------------------------------
# TITLE
# -----------------------------------------
st.title("📊 Résumé Global — Olist")
st.markdown("### Vue d’ensemble des performances commerciales")

st.write("")


# -----------------------------------------
# LOAD DATA
# -----------------------------------------
orders = load_table("clean_orders")
order_items = load_table("clean_order_items")
reviews = load_table("clean_reviews")
products = load_table("clean_products")
customers = load_table("clean_customers")


# -----------------------------------------
# KPI CALCULATIONS
# -----------------------------------------

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


# -----------------------------------------
# KPI SECTION
# -----------------------------------------
st.markdown("## 🧮 Indicateurs clés")

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Revenue Total", f"R$ {total_revenue:,.0f}")
col2.metric("🛍️ Nombre de Commandes", f"{nb_orders:,}")
col3.metric("⭐ Note Moyenne", f"{avg_score:.2f} / 5")
col4.metric("🚚 Délai Moyen", f"{delivery_delay:.2f} jours")

st.markdown("---")
st.write("")


# ========================================================
# SECTION 1 — Revenue dans le temps
# ========================================================

st.markdown("## 📈 Évolution du Chiffre d’Affaires")

order_items["total"] = order_items["price"] + order_items["freight_value"]

df_time = orders.merge(order_items, on="order_id")
df_time["date"] = pd.to_datetime(df_time["order_purchase_timestamp"]).dt.to_period("M").astype(str)

rev_time = df_time.groupby("date")["total"].sum().reset_index()

fig_rev = px.line(
    rev_time,
    x="date",
    y="total",
    title="Revenue Mensuel",
    markers=True
)

fig_rev.update_layout(height=350)

st.plotly_chart(fig_rev, use_container_width=True)

st.write("")


# ========================================================
# SECTION 2 — CA par État (carte)
# ========================================================

st.markdown("## 🌍 Répartition Géographique du CA")

query_geo = """
SELECT 
    c.customer_state AS state,
    SUM(coi.price + coi.freight_value) AS revenue
FROM clean_order_items coi
JOIN clean_orders o ON coi.order_id = o.order_id
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status IN ('delivered', 'shipped', 'invoiced')
GROUP BY c.customer_state;
"""

df_geo = load_table("clean_customers")  # fallback
df_geo = pd.read_sql(query_geo, st.session_state["connection"])

fig_geo = px.choropleth(
    df_geo,
    locations="state",
    locationmode="geojson-id",
    color="revenue",
    color_continuous_scale="Blues",
    title="CA par État"
)

st.plotly_chart(fig_geo, use_container_width=True)

st.write("")


# ========================================================
# SECTION 3 — Top 10 catégories
# ========================================================

st.markdown("## 🥇 Top 10 Catégories (CA)")

query_ctg = """
SELECT 
    COALESCE(tr.product_category_name_english, cp.product_category_name) AS category,
    SUM(coi.price + coi.freight_value) AS revenue
FROM clean_order_items coi
JOIN clean_products cp ON cp.product_id = coi.product_id
LEFT JOIN product_category_name_translation tr
    ON cp.product_category_name = tr.product_category_name
JOIN clean_orders o ON o.order_id = coi.order_id
WHERE o.order_status IN ('delivered','shipped','invoiced')
GROUP BY category
ORDER BY revenue DESC
LIMIT 10;
"""

df_ctg = pd.read_sql(query_ctg, st.session_state["connection"])

fig_ctg = px.bar(
    df_ctg,
    x="revenue",
    y="category",
    orientation="h",
    title="Top 10 Catégories par CA",
    color="revenue",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_ctg, use_container_width=True)

st.write("")


# ========================================================
# SECTION 4 — Distribution des notes
# ========================================================

st.markdown("## ⭐ Distribution des Notes Clients")

fig_score = px.histogram(
    reviews,
    x="review_score",
    nbins=5,
    title="Répartition des Notes",
    color_discrete_sequence=["#1F77B4"]
)

st.plotly_chart(fig_score, use_container_width=True)

st.markdown("---")

# ========================================================
# INSIGHTS
# ========================================================

st.markdown("## 🔍 Insights clés")

st.markdown("""
- **SP** représente plus de **36 %** du CA total  
- Les retards (>20 jours) génèrent **35 % de mauvaises notes**  
- 97 % des clients sont des **one-time buyers**  
- Les catégories **beauty / gifts** dominent les ventes  
- Les délais de livraison varient fortement selon l’état  
""")

st.info("📌 Pour les actions business : consulte la page **Recommandations**.")
