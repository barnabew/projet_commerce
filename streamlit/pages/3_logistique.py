import streamlit as st
from data import run_query
from visuel import (
    plot_delivery_by_state,
    plot_logistic_flow,
    plot_state_heatmap,
    plot_delay_vs_review
)
from textes import texte_logistique

st.title("🚚 Logistics & Delivery Analysis")
st.markdown(texte_logistique)

# ======================================================
# 1️⃣ Delivery time by destination state
# ======================================================

query_delay_state = """
SELECT 
    c.customer_state,
    ROUND(AVG(
       JULIANDAY(o.order_delivered_customer_date) 
       - JULIANDAY(o.order_purchase_timestamp)
    ), 2) AS avg_delivery_days
FROM clean_orders o
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY c.customer_state
ORDER BY avg_delivery_days DESC;
"""
df_delay_state = run_query(query_delay_state)
st.plotly_chart(plot_delivery_by_state(df_delay_state), use_container_width=True)

# ======================================================
# 2️⃣ Seller → Customer flows (sunburst)
# ======================================================

query_flow = """
SELECT 
    s.seller_state,
    c.customer_state,
    COUNT(*) AS nb_orders
FROM clean_order_items oi
JOIN clean_orders o ON oi.order_id = o.order_id
JOIN clean_sellers s ON oi.seller_id = s.seller_id
JOIN clean_customers c ON o.customer_id = c.customer_id
WHERE o.order_status = 'delivered'
GROUP BY s.seller_state, c.customer_state;
"""
df_flow = run_query(query_flow)
st.plotly_chart(plot_logistic_flow(df_flow), use_container_width=True)

# ======================================================
# 3️⃣ Heatmap state → state
# ======================================================

st.subheader("Heatmap of Orders Flows (State → State)")
st.plotly_chart(plot_state_heatmap(df_flow), use_container_width=True)

# ======================================================
# 4️⃣ Delivery delay vs review score
# ======================================================

query_delay_review = """
SELECT 
    r.review_score,
    JULIANDAY(o.order_delivered_customer_date) 
        - JULIANDAY(o.order_purchase_timestamp) AS delivery_days
FROM clean_reviews r
JOIN clean_orders o ON r.order_id = o.order_id
WHERE o.order_status = 'delivered';
"""
df_delay_review = run_query(query_delay_review)

st.subheader("Impact of Delivery Delay on Reviews")
st.plotly_chart(plot_delay_vs_review(df_delay_review), use_container_width=True)
