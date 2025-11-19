import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from data import get_connection, load_table

st.set_page_config(page_title="Analyse Clients", layout="wide")

st.title("👤 Analyse Client – Comportement & Valeur")


# --------------------------------------------------
# CHARGEMENT DES DONNÉES
# --------------------------------------------------

conn = get_connection()

orders = load_table("clean_orders")
customers = load_table("clean_customers")
items = load_table("clean_order_items")
reviews = load_table("clean_reviews")


# --------------------------------------------------
# CONSTRUCTION DU DATAFRAME CLIENT FINAL
# --------------------------------------------------

# Base : orders + customers
df = (
    orders
    .merge(customers, on="customer_id", how="left")
    .merge(items, on="order_id", how="left")
)

# Monetary par client
df_m = df.groupby("customer_unique_id", as_index=False).agg(
    frequency=("order_id", "nunique"),
    price_sum=("price", "sum"),
    freight_sum=("freight_value", "sum")
)
df_m["monetary"] = df_m["price_sum"] + df_m["freight_sum"]
df_m["log_monetary"] = np.log1p(df_m["monetary"])

# Reviews par client
df_r = (
    reviews
    .merge(orders[["order_id", "customer_id"]], on="order_id", how="left")
    .merge(customers, on="customer_id", how="left")
)
df_rev = df_r.groupby("customer_unique_id", as_index=False).agg(
    avg_review_score=("review_score", "mean"),
    review_count=("review_id", "count")
)

# Fusion finale
df_cust = df_m.merge(df_rev, on="customer_unique_id", how="left")


# --------------------------------------------------
# 1. KPIs CLIENTS
# --------------------------------------------------

st.header("📊 Indicateurs clés")

unique_customers = df_cust["customer_unique_id"].nunique()
one_shot_rate = (df_cust["frequency"].eq(1).mean() * 100)
avg_spend = df_cust["monetary"].mean()
median_spend = df_cust["monetary"].median()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Clients uniques", f"{unique_customers:,}")
col2.metric("One-shot buyers", f"{one_shot_rate:.1f}%")
col3.metric("Dépense moyenne", f"{avg_spend:.1f} R$")
col4.metric("Dépense médiane", f"{median_spend:.1f} R$")


# --------------------------------------------------
# 2. FIDÉLITÉ CLIENT
# --------------------------------------------------

st.header("📈 Fidélité des clients")

freq_counts = df_cust["frequency"].value_counts().sort_index()

# Histogramme du nombre de commandes
fig_freq = px.bar(
    freq_counts,
    labels={"index": "Nombre de commandes", "value": "Nombre de clients"},
    title="Distribution du nombre de commandes par client"
)

fig_freq.add_annotation(
    x=1,
    y=freq_counts.max(),
    text=f"{one_shot_rate:.1f}% de one-shot buyers",
    showarrow=True,
    arrowhead=2,
    font=dict(color="red", size=14)
)

st.plotly_chart(fig_freq, use_container_width=True)

# Petit résumé textuel
st.markdown(f"""
### 🧠 Ce que cela montre :
- **{one_shot_rate:.1f}% des clients ne commandent qu'une seule fois.**
- La fidélité est **extrêmement faible**, ce qui est typique d'Olist.
""")



# --------------------------------------------------
# 3. SATISFACTION CLIENT
# --------------------------------------------------

st.header("⭐ Satisfaction Client")

# A — Distribution globale des notes
st.subheader("📌 Distribution des notes")
fig_hist = px.histogram(
    reviews, 
    x="review_score",
    nbins=5,
    color_discrete_sequence=["#6a8caf"],
    title="Répartition des notes clients"
)
st.plotly_chart(fig_hist, use_container_width=True)


# B — Satisfaction selon la fréquence d'achat
st.subheader("📌 Satisfaction selon le type de client")

df_rev_freq = df_cust.groupby("frequency", as_index=False).agg(
    avg_score=("avg_review_score", "mean"),
    count=("customer_unique_id", "count")
)

fig_rev_freq = px.bar(
    df_rev_freq,
    x="frequency",
    y="avg_score",
    title="Note moyenne par fréquence d'achat",
    labels={"frequency": "Nombre de commandes", "avg_score": "Note moyenne"},
    color="avg_score",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_rev_freq, use_container_width=True)

st.markdown("""
💡 *Les clients récurrents donnent-ils de meilleures ou de moins bonnes notes ?  
Cette analyse aide à comprendre la relation entre expérience et fidélité.*
""")


# C — Relation dépenses ↔ satisfaction
st.subheader("📌 Note moyenne selon le niveau de dépense (segments)")

df_cust["spend_segment"] = pd.qcut(
    df_cust["monetary"],
    q=4,
    labels=["Low spenders", "Medium", "High", "Very high"]
)

df_spend_rev = (
    df_cust.groupby("spend_segment", as_index=False)
           .agg(avg_review=("avg_review_score", "mean"))
)

fig_spend_rev = px.bar(
    df_spend_rev,
    x="spend_segment",
    y="avg_review",
    title="Satisfaction selon le niveau de dépense",
    color="avg_review",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_spend_rev, use_container_width=True)



# --------------------------------------------------
# 4. VALEUR CLIENT (Customer Value)
# --------------------------------------------------

st.header("💰 Valeur Client")

colv1, colv2 = st.columns(2)

# Distribution des dépenses
fig_m = px.histogram(
    df_cust,
    x="log_monetary",
    nbins=50,
    title="Distribution log(monetary)",
    color_discrete_sequence=["#445c7a"]
)
colv1.plotly_chart(fig_m, use_container_width=True)

# Percentiles
percentiles = df_cust["monetary"].quantile([0.5, 0.75, 0.9, 0.9]()_
