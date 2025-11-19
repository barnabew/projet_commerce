import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from data import load_table  # ta fonction existante

st.title("📊 Segmentation Clients – FM")

st.markdown("""
La segmentation FM repose sur 2 dimensions uniquement :
- **Frequency** : nombre d'achats par client
- **Monetary** : montant total dépensé

Nous utilisons `customer_unique_id` pour regrouper les achats d’un même client réel.
""")

# -----------------------------
# 📌 1. Chargement des données
# -----------------------------
orders = load_table("clean_orders")
customers = load_table("clean_customers")
items = load_table("clean_order_items")

# FM computation
df = (
    orders.merge(customers, on="customer_id")
          .merge(items, on="order_id")
          .query("order_status in ['delivered','shipped','invoiced']")
)

fm = df.groupby("customer_unique_id").agg(
    frequency=("order_id", "nunique"),
    monetary=("price", "sum")
).reset_index()

# -----------------------------
# 📌 2. Scores F & M
# -----------------------------
def freq_score(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    return 4

fm["F_score"] = fm["frequency"].apply(freq_score)
fm["M_score"] = pd.qcut(
    fm["monetary"], q=4, labels=[1,2,3,4], duplicates="drop"
)

# Segment
def assign_segment(row):
    if row["F_score"] == 4 and row["M_score"] == 4:
        return "Best Customers"
    elif row["F_score"] >= 3 and row["M_score"] >= 3:
        return "Loyal High-Value"
    elif row["F_score"] >= 3:
        return "Frequent Low-Value"
    elif row["M_score"] >= 3:
        return "High-Value One-Timers"
    return "Low-Value Customers"

fm["segment"] = fm.apply(assign_segment, axis=1)

# Palette couleurs cohérente
colors = {
    "Low-Value Customers": "#A7C7E7",
    "High-Value One-Timers": "#1F77B4",
    "Frequent Low-Value": "#2CA02C",
    "Loyal High-Value": "#FF5733",
    "Best Customers": "#FFC300"
}

# -----------------------------
# 📌 3. Répartition des segments (bar chart)
# -----------------------------
st.subheader("📌 Répartition des segments FM")

seg_counts = fm["segment"].value_counts().reset_index()
seg_counts.columns = ["segment", "count"]
seg_counts["percent"] = seg_counts["count"] / seg_counts["count"].sum() * 100

fig = px.bar(
    seg_counts,
    x="percent",
    y="segment",
    orientation="h",
    color="segment",
    color_discrete_map=colors,
    text="percent",
)
fig.update_traces(texttemplate="%{text:.1f}%", textposition="outside")
fig.update_layout(height=450)

st.plotly_chart(fig, use_container_width=True)

st.markdown("🔍 **Lecture** : la majorité des clients sont des *One-Timers*, ce qui est normal sur Olist.")

# -----------------------------
# 📌 4. FM Distribution (hexbin)
# -----------------------------
st.subheader("📌 Distribution FM (2D Density Contour)")

fm["log_monetary"] = np.log1p(fm["monetary"])

fig = go.Figure()

fig.add_trace(go.Histogram2dContour(
    x=fm["log_monetary"],
    y=fm["frequency"],
    colorscale="Viridis",
    reversescale=False,
    xbins=dict(size=0.15),
    ybins=dict(size=1),
    contours=dict(
        coloring="heatmap",
        showlines=False
    )
))

fig.update_layout(
    height=500,
    title="FM Distribution — 2D Density Contour (Plotly)",
    xaxis_title="log(Monetary)",
    yaxis_title="Frequency"
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
💡 *Pourquoi ce graphique ?*  
Plotly Express ne supporte pas directement les hexbin,  
mais les **2D Contours remplis (Histogram2dContour)** offrent  
une lecture beaucoup plus claire qu’une heatmap classique.
""")


# -----------------------------
# 📌 5. Statistiques clés
# -----------------------------
st.subheader("📌 Tableau des segments FM")

seg_stats = fm.groupby("segment").agg(
    clients=("customer_unique_id", "count"),
    avg_frequency=("frequency", "mean"),
    avg_monetary=("monetary", "mean"),
    percent=("customer_unique_id", lambda x: len(x) / len(fm) * 100)
).reset_index()

st.dataframe(seg_stats)

# -----------------------------
# 📌 6. Interprétation automatique
# -----------------------------
st.subheader("📌 Interprétation automatique")

st.markdown("""
- **Low-Value Customers** : majorité des clients, achats uniques et petits paniers.  
- **High-Value One-Timers** : gros panier mais un seul achat → segment clé pour remarketing.  
- **Frequent Low-Value** : clients fidèles mais petits paniers → cross-sell.  
- **Loyal High-Value** : clients rentables et réguliers → à choyer.  
- **Best Customers** : cœur business, forte priorité.  
""")
