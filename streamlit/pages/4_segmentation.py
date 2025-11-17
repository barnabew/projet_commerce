import streamlit as st
from data import run_query
from visuel import (
    plot_fm_heatmap,
    plot_fm_scatter,
    plot_segment_distribution
)
from textes import texte_fm

st.title("⭐ Customer Segmentation (FM)")
st.markdown(texte_fm)

# ======================================================
# 1️⃣ Compute FM table in SQL
# ======================================================

query_fm = """
WITH fm AS (
    SELECT 
        c.customer_unique_id,
        COUNT(DISTINCT o.order_id) AS frequency,
        SUM(oi.price + oi.freight_value) AS monetary
    FROM clean_customers c
    JOIN clean_orders o ON c.customer_id = o.customer_id
    JOIN clean_order_items oi ON o.order_id = oi.order_id
    WHERE o.order_status = 'delivered'
    GROUP BY c.customer_unique_id
)
SELECT *,
CASE 
    WHEN frequency >= 3 AND monetary >= 500 THEN 'Best Customers'
    WHEN frequency = 1 AND monetary >= 300 THEN 'High-Value One-Timers'
    WHEN frequency >= 2 THEN 'Loyal Customers'
    ELSE 'Low-Value Customers'
END AS segment
FROM fm;
"""

df_fm = run_query(query_fm)

# ======================================================
# 2️⃣ Segment distribution
# ======================================================

st.subheader("Segment Distribution")
st.plotly_chart(plot_segment_distribution(df_fm), use_container_width=True)

# ======================================================
# 3️⃣ FM Heatmap
# ======================================================

st.subheader("FM Heatmap")
st.plotly_chart(plot_fm_heatmap(df_fm), use_container_width=True)

# ======================================================
# 4️⃣ FM Scatter
# ======================================================

st.subheader("FM Scatter (log monetary)")
st.plotly_chart(plot_fm_scatter(df_fm), use_container_width=True)

# ======================================================
# 5️⃣ Explore a segment
# ======================================================

st.subheader("🔍 Explore a Segment")

segments = df_fm["segment"].unique()
selected_segment = st.selectbox("Choose a segment", segments)

df_segment = df_fm[df_fm["segment"] == selected_segment]

st.write(df_segment.head(20))
