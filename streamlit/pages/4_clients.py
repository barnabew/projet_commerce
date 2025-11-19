# --------------------------------------------------
# Page 4 — Analyse Client Avancée
# --------------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from data import get_connection, load_table

st.set_page_config(page_title="Analyse Clients", layout="wide")

st.title("👤 Analyse Clients Avancée")
st.markdown("Cette page explore le comportement des clients : fidélité, satisfaction et contribution à la valeur.")


# --------------------------------------------------
# 1. CHARGEMENT DES DONNÉES
# --------------------------------------------------

conn = get_connection()

# clean tables
orders = load_table("clean_orders")
customers = load_table("clean_customers")
items = load_table("clean_order_items")
reviews = load_table("clean_reviews")
products = load_table("clean_products")
translate = load_table("product_category_name_translation")


# --------------------------------------------------
# Préparation : jointure client–orders–items–reviews
# --------------------------------------------------

df = (
    orders
    .merge(customers, on="customer_id", how="left")
    .merge(items, on="order_id", how="left")
)

# monetary per customer_unique_id
df_monetary = df.groupby("customer_unique_id", as_index=False).agg({
    "order_id": "nunique",
    "price": "sum",
    "freight_value": "sum"
})

df_monetary["monetary"] = df_monetary["price"] + df_monetary["freight_value"]
df_monetary["frequency"] = df_monetary["order_id"]
df_monetary["log_monetary"] = np.log1p(df_monetary["monetary"])

# reviews per customer
df_rev = (
    reviews
    .merge(orders[["order_id", "customer_id"]], on="order_id", how="left")
    .merge(customers, on="customer_id", how="left")
)

df_review_cust = df_rev.groupby("customer_unique_id", as_index=False).agg({
    "review_score": "mean"
}).rename(columns={"review_score": "avg_review_score"})


# fusion finale
df_cust = df_monetary.merge(df_review_cust, on="customer_unique_id", how="left")


# --------------------------------------------------
# 1. KPIs
# --------------------------------------------------

st.header("📊 Indicateurs clés")

col1, col2, col3, col4 = st.columns(4)

unique_customers = df_cust["customer_unique_id"].nunique()
one_shot_rate = (df_cust["frequency"].value_counts().get(1, 0) / unique_customers) * 100
avg_spend = df_cust["monetary"].mean()
top1 = df_cust["monetary"].quantile(0.99)

col1.metric("Clients uniques", f"{unique_customers:,}")
col2.metric("One-shot buyers", f"{one_shot_rate:.1f}%")
col3.metric("Dépense moyenne", f"{avg_spend:.1f} R$") 
col4.metric("Panier top 1%", f"{top1:.1f} R$")


# --------------------------------------------------
# 2. FIDÉLITÉ
# --------------------------------------------------

st.header("📈 Fidélité : nombre de commandes par client")

freq_count = df_cust["frequency"].value_counts().sort_index()

fig_freq = px.bar(
    freq_count,
    labels={"index": "Nombre de commandes", "value": "Nb de clients"},
    title="Distribution du nombre de commandes"
)

fig_freq.add_annotation(
    x=1,
    y=freq_count.max(),
    text=f"{one_shot_rate:.1f}% one-shot buyers",
    showarrow=True,
    arrowhead=2,
    font=dict(size=14, color="red")
)

st.plotly_chart(fig_freq, use_container_width=True)


# --------------------------------------------------
# 3. SATISFACTION
# --------------------------------------------------

st.header("⭐ Satisfaction Clients")

# A — Histogramme global
fig_hist = px.histogram(
    reviews, 
    x="review_score", 
    nbins=5,
    title="Distribution des notes",
    color_discrete_sequence=["#6a8caf"]
)
st.subheader("📌 Distribution des notes")
st.plotly_chart(fig_hist, use_container_width=True)


# B — Review moyenne par état
st.subheader("📌 Review moyenne par État")

df_state_rev = (
    df_rev.groupby("customer_state", as_index=False)
          .agg(avg_score=("review_score", "mean"))
          .sort_values("avg_score")
)

fig_state = px.bar(
    df_state_rev, 
    x="customer_state", 
    y="avg_score",
    title="Review moyenne par État",
    color="avg_score",
    color_continuous_scale="Blues"
)
st.plotly_chart(fig_state, use_container_width=True)


# C — Review moyenne par catégorie produit
st.subheader("📌 Review moyenne par catégorie produit")

df_cat = (
    reviews
    .merge(items, on="order_id")
    .merge(products, on="product_id")
    .merge(translate, on="product_category_name", how="left")
)

df_cat["category"] = df_cat["product_category_name_english"].fillna(df_cat["product_category_name"])

df_cat_review = (
    df_cat.groupby("category", as_index=False)
          .agg(avg_score=("review_score", "mean"), count=("review_id", "count"))
          .query("count > 200")
          .sort_values("avg_score")
)

fig_cat = px.bar(
    df_cat_review,
    y="category",
    x="avg_score",
    title="Review moyenne par catégorie (min 200 reviews)",
    orientation="h",
    color="avg_score",
    color_continuous_scale="Blues"
)
st.plotly_chart(fig_cat, use_container_width=True)


# --------------------------------------------------
# 4. HIGH-VALUE CUSTOMERS
# --------------------------------------------------

st.header("💰 High-Value Customers")

# A — Top clients
st.subheader("Top 20 clients")

top20 = df_cust.sort_values("monetary", ascending=False).head(20)[
    ["customer_unique_id", "monetary", "frequency", "avg_review_score"]
]

st.dataframe(top20, use_container_width=True)


# B — histogram log monetary
st.subheader("Distribution des dépenses (log scale)")
fig_m = px.histogram(
    df_cust,
    x="log_monetary",
    nbins=50,
    title="Distribution log(monetary)"
)
st.plotly_chart(fig_m, use_container_width=True)


# C — Catégories achetées par les top clients
st.subheader("Catégories préférées des top clients (top 1%)")

top_ids = df_cust[df_cust["monetary"] >= top1]["customer_unique_id"].unique()

df_top_cat = (
    df[df["customer_unique_id"].isin(top_ids)]
    .merge(products, on="product_id")
    .merge(translate, on="product_category_name", how="left")
)

df_top_cat["category"] = df_top_cat["product_category_name_english"].fillna(df_top_cat["product_category_name"])

fav_cat = df_top_cat["category"].value_counts().head(10).reset_index()
fav_cat.columns = ["category", "count"]

fig_fav = px.bar(
    fav_cat,
    x="count",
    y="category",
    orientation="h",
    title="TOP catégories des clients à forte valeur"
)
st.plotly_chart(fig_fav, use_container_width=True)


# --------------------------------------------------
# 5. INSIGHTS BUSINESS
# --------------------------------------------------

st.header("📌 Insights Business")

st.markdown("""
### 🎯 Principaux enseignements

- **Olist a un taux très élevé de clients “one-shot”** → la fidélité est quasi inexistante.  
- **Les notes clients sont globalement élevées**, mais varient fortement selon les catégories et les États.  
- **Les délais de livraison influencent directement la satisfaction** (vu page géographique).  
- **Le top 1% des clients explique une part significative du CA**, et se concentre sur quelques catégories spécifiques.  

Ces éléments fournissent une base solide pour des recommandations marketing et logistiques.
""")

