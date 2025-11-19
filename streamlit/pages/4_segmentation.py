import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from data import get_connection

st.title("👥 Segmentation Clients – FM (Frequency & Monetary)")

st.write("""
La segmentation FM permet de classer les clients selon :
- **F (Frequency)** : nombre de commandes passées  
- **M (Monetary)** : montant total dépensé  

Cette approche est adaptée à Olist, car :
- les données temporelles ont des trous (R impossible à calculer correctement),
- les clients réalisent très rarement plusieurs commandes.
""")

conn = get_connection()

# ==========================================
# 1️⃣ FM depuis SQL
# ==========================================
query_fm = """
WITH fm AS (
    SELECT 
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS frequency,
        SUM(coi.price + coi.freight_value) AS monetary
    FROM clean_orders o
    JOIN clean_customers c ON o.customer_id = c.customer_id
    JOIN clean_order_items coi ON o.order_id = coi.order_id
    WHERE o.order_status IN ('delivered', 'shipped', 'invoiced')
    GROUP BY c.customer_unique_id
)
SELECT * FROM fm;
"""

df = pd.read_sql(query_fm, conn)

st.subheader("📊 Distribution des clients (FM)")
st.write(f"{df.shape[0]} clients uniques analysés")

# ==========================================
# 2️⃣ SCORING
# ==========================================

def freq_score(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x == 3:
        return 3
    else:
        return 4

df["F_score"] = df["frequency"].apply(freq_score)
df["M_score"] = pd.qcut(df["monetary"], 4, labels=[1,2,3,4], duplicates="drop")

df["FM_score"] = df["F_score"].astype(int) + df["M_score"].astype(int)

# SEGMENTS
def assign_segment(row):
    if row["F_score"] == 4 and row["M_score"] == 4:
        return "Best Customers"
    elif row["F_score"] >= 3 and row["M_score"] >= 3:
        return "Loyal High-Value"
    elif row["F_score"] >= 3 and row["M_score"] <= 2:
        return "Frequent Low-Value"
    elif row["F_score"] <= 2 and row["M_score"] >= 3:
        return "High-Value One-Timers"
    else:
        return "Low-Value Customers"

df["segment"] = df.apply(assign_segment, axis=1)

# ==========================================
# 3️⃣ VISUALISATIONS
# ==========================================

st.header("📈 Répartition des segments")

fig_pie = px.pie(
    df,
    names="segment",
    title="Répartition des segments FM",
    color="segment",
)
st.plotly_chart(fig_pie, use_container_width=True)

# ----------------------------------------------------------
# Heatmap FM
# ----------------------------------------------------------
st.subheader("🎛️ Heatmap FM (log-scale)")

df_plot = df.copy()
df_plot["log_monetary"] = np.log1p(df_plot["monetary"])

fig_heat = px.density_heatmap(
    df_plot,
    x="log_monetary",
    y="frequency",
    nbinsx=30,
    nbinsy=10,
    color_continuous_scale="Viridis",
    title="Répartition des clients selon Frequency et Monetary",
)
st.plotly_chart(fig_heat, use_container_width=True)

# ----------------------------------------------------------
# Tableau résumé
# ----------------------------------------------------------
st.header("📋 Tableau des segments")

summary = df.groupby("segment").agg(
    clients=("customer_unique_id", "count"),
    avg_frequency=("frequency", "mean"),
    avg_monetary=("monetary", "mean")
).sort_values("clients", ascending=False)

st.dataframe(summary)

# ----------------------------------------------------------
# Affichage dataset FM
# ----------------------------------------------------------
with st.expander("Voir les données FM complètes"):
    st.dataframe(df)
