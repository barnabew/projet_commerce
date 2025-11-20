import streamlit as st
import pandas as pd
import plotly.express as px

from data import load_table  # ✅ ta fonction

# -----------------------------------------
# CONFIG GLOBALE
# (si tu as déjà un set_page_config dans un autre fichier, enlève celui-ci)
# -----------------------------------------
st.set_page_config(
    page_title="Olist – Résumé",
    layout="wide"
)

# -----------------------------------------
# CSS DESIGN – STYLE CORPORATE CLEAN
# -----------------------------------------
st.markdown("""
<style>
    /* Fond global gris très léger */
    .stApp {
        background-color: #F5F7FB;
    }

    /* Conteneur principal plus étroit comme un vrai dashboard */
    .block-container {
        max-width: 1200px;
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }

    /* KPI cards */
    div[data-testid="metric-container"] {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 18px;
        margin: 4px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        border: 1px solid #E6E6E6;
    }

    /* Titres */
    h1, h2, h3 {
        color: #1F77B4 !important;
        font-weight: 600;
    }

    /* Séparateurs plus discrets */
    hr {
        border: none;
        border-top: 1px solid #E0E0E0;
        margin: 1.5rem 0;
    }

    /* Masquer le footer Streamlit */
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -----------------------------------------
# TITRE
# -----------------------------------------
st.title("📊 Olist – Résumé Global")
st.markdown("Vue d’ensemble des performances commerciales, produits et satisfaction client.")

st.write("")

# -----------------------------------------
# CHARGEMENT DES DONNÉES
# -----------------------------------------
orders = load_table("clean_orders")
order_items = load_table("clean_order_items")
reviews = load_table("clean_reviews")
customers = load_table("clean_customers")
products = load_table("clean_products")

# -----------------------------------------
# KPI CALCULS
# -----------------------------------------

# Revenue total
order_items["total"] = order_items["price"] + order_items["freight_value"]
total_revenue = order_items["total"].sum()

# Nombre de commandes
nb_orders = orders["order_id"].nunique()

# Note moyenne
avg_score = reviews["review_score"].mean()

# Délai moyen de livraison (commandes livrées / valides)
orders_valid = orders[
    (orders["order_status"].isin(["delivered", "shipped", "invoiced"])) &
    orders["order_delivered_customer_date"].notna() &
    orders["order_purchase_timestamp"].notna()
].copy()

orders_valid["order_delivered_customer_date"] = pd.to_datetime(
    orders_valid["order_delivered_customer_date"]
)
orders_valid["order_purchase_timestamp"] = pd.to_datetime(
    orders_valid["order_purchase_timestamp"]
)

delivery_delay_days = (
    orders_valid["order_delivered_customer_date"]
    - orders_valid["order_purchase_timestamp"]
).dt.days.mean()

# -----------------------------------------
# BANDEAU KPI
# -----------------------------------------
st.markdown("## 🧮 Indicateurs clés")

k1, k2, k3, k4 = st.columns(4)
k1.metric("💰 Revenue total", f"R$ {total_revenue:,.0f}")
k2.metric("🛍️ Nombre de commandes", f"{nb_orders:,}")
k3.metric("⭐ Note moyenne", f"{avg_score:.2f} / 5")
k4.metric("🚚 Délai moyen de livraison", f"{delivery_delay_days:.2f} jours")

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------
# SECTION 1 – REVENUE DANS LE TEMPS
# -----------------------------------------
st.markdown("## 📈 Vue globale des ventes")

# Join orders + order_items pour CA mensuel
df_time = orders[["order_id", "order_purchase_timestamp"]].merge(
    order_items[["order_id", "total"]], on="order_id", how="inner"
)
df_time["order_purchase_timestamp"] = pd.to_datetime(df_time["order_purchase_timestamp"])
df_time["month"] = df_time["order_purchase_timestamp"].dt.to_period("M").astype(str)

rev_by_month = (
    df_time.groupby("month", as_index=False)["total"]
    .sum()
    .sort_values("month")
)

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("#### Chiffre d’affaires mensuel")
    fig_rev = px.line(
        rev_by_month,
        x="month",
        y="total",
        markers=True,
        labels={"month": "Mois", "total": "CA (R$)"},
    )
    fig_rev.update_layout(height=320, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_rev, use_container_width=True)

# -----------------------------------------
# SECTION 2 – CA PAR ÉTAT
# -----------------------------------------
# Join orders + items + customers pour CA par state
df_geo = (
    orders.merge(order_items, on="order_id", how="inner")
          .merge(customers, on="customer_id", how="left")
)

df_geo_valid = df_geo[df_geo["order_status"].isin(["delivered", "shipped", "invoiced"])]
rev_by_state = (
    df_geo_valid.groupby("customer_state", as_index=False)["total"]
    .sum()
    .rename(columns={"customer_state": "state", "total": "revenue"})
    .sort_values("revenue", ascending=False)
)

with col_right:
    st.markdown("#### Chiffre d’affaires par État (TOP)")
    fig_state = px.bar(
        rev_by_state.head(10),
        x="revenue",
        y="state",
        orientation="h",
        labels={"state": "État", "revenue": "CA (R$)"},
    )
    fig_state.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=40, b=10),
        yaxis=dict(autorange="reversed"),
    )
    st.plotly_chart(fig_state, use_container_width=True)

st.write("")
st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------
# SECTION 3 – TOP CATÉGORIES PRODUITS
# -----------------------------------------
st.markdown("## 🥇 Catégories produits")

# On suppose que tu as déjà chargé la table de traduction dans une autre page,
# sinon tu peux la charger ici également :
try:
    from data import load_table
    translation = load_table("product_category_name_translation")
except Exception:
    translation = pd.DataFrame(columns=["product_category_name", "product_category_name_english"])

df_prod = (
    order_items.merge(products, on="product_id", how="left")
               .merge(translation, on="product_category_name", how="left")
)

df_prod["category"] = df_prod["product_category_name_english"].fillna(
    df_prod["product_category_name"]
)

rev_by_cat = (
    df_prod.groupby("category", as_index=False)["total"]
    .sum()
    .rename(columns={"total": "revenue"})
    .sort_values("revenue", ascending=False)
    .head(10)
)

c1, c2 = st.columns(2)

with c1:
    st.markdown("#### Top 10 catégories par CA")
    fig_cat = px.bar(
        rev_by_cat,
        x="revenue",
        y="category",
        orientation="h",
        labels={"category": "Catégorie", "revenue": "CA (R$)"},
    )
    fig_cat.update_layout(
        height=320,
        margin=dict(l=10, r=10, t=40, b=10),
        yaxis=dict(autorange="reversed"),
    )
    st.plotly_chart(fig_cat, use_container_width=True)

# -----------------------------------------
# SECTION 4 – DISTRIBUTION DES NOTES
# -----------------------------------------
with c2:
    st.markdown("#### Distribution des notes clients")
    fig_score = px.histogram(
        reviews,
        x="review_score",
        nbins=5,
        labels={"review_score": "Note"},
    )
    fig_score.update_layout(height=320, margin=dict(l=10, r=10, t=40, b=10))
    st.plotly_chart(fig_score, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)

# -----------------------------------------
# INSIGHTS CLÉS
# -----------------------------------------
st.markdown("## 🔍 Insights clés")

st.markdown("""
- **Le CA est concentré sur quelques mois et quelques États (notamment SP).**  
- **Les délais moyens restent élevés (~{:.1f} jours)** pour un e-commerce, impactant la satisfaction.  
- **Certaines catégories dominent largement le CA**, ce sont des leviers marketing prioritaires.  
- **Les notes clients sont globalement bonnes (≈ {:.2f}/5)** mais très sensibles aux délais de livraison.  

👉 Pour une analyse plus détaillée, utilise les pages : Géographie, Produits, Clients et Recommandations.
""".format(delivery_delay_days, avg_score))
