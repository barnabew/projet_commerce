import streamlit as st
from data import run_query
from visuel import (
    plot_top_categories_revenue,
    plot_top_categories_sales,
    plot_avg_price,
    plot_best_rated,
    plot_worst_rated,
    plot_delivery_time,
    plot_category_scatter
)
from textes import texte_intro_produits

st.title("🛒 Product Analysis")
st.markdown(texte_intro_produits)

# ======================================================
# 1️⃣ Top categories by revenue
# ======================================================

query_ca = """
SELECT 
    p.product_category_name,
    SUM(oi.price + oi.freight_value) AS revenue
FROM clean_order_items oi
JOIN clean_products p ON oi.product_id = p.product_id
JOIN clean_orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY p.product_category_name
ORDER BY revenue DESC
LIMIT 10;
"""
df_ca = run_query(query_ca)
st.plotly_chart(plot_top_categories_revenue(df_ca), use_container_width=True)

# ======================================================
# 2️⃣ Top categories by sales volume
# ======================================================

query_qty = """
SELECT 
    p.product_category_name,
    COUNT(*) AS sales_count
FROM clean_order_items oi
JOIN clean_products p ON oi.product_id = p.product_id
JOIN clean_orders o ON oi.order_id = o.order_id
WHERE o.order_status = 'delivered'
GROUP BY p.product_category_name
ORDER BY sales_count DESC
LIMIT 10;
"""
df_qty = run_query(query_qty)
st.plotly_chart(plot_top_categories_sales(df_qty), use_container_width=True)

# ======================================================
# 3️⃣ Average price per category
# ======================================================

query_price = """
SELECT 
    p.product_category_name,
    ROUND(AVG(oi.price), 2) AS avg_price
FROM clean_order_items oi
JOIN clean_products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
HAVING COUNT(*) > 50
ORDER BY avg_price DESC
LIMIT 15;
"""
df_price = run_query(query_price)
st.plotly_chart(plot_avg_price(df_price), use_container_width=True)

# ======================================================
# 4️⃣ Ratings (best & worst)
# ======================================================

query_reviews = """
SELECT 
    p.product_category_name,
    COUNT(r.review_id) AS nb_reviews,
    ROUND(AVG(r.review_score), 2) AS avg_review
FROM clean_reviews r
JOIN clean_orders o ON r.order_id = o.order_id
JOIN clean_order_items oi ON o.order_id = oi.order_id
JOIN clean_products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name
HAVING nb_reviews > 50
ORDER BY avg_review DESC;
"""
df_reviews = run_query(query_reviews)

col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_best_rated(df_reviews.head(10)), use_container_width=True)
with col2:
    st.plotly_chart(plot_worst_rated(df_reviews.tail(10)), use_container_width=True)

# ======================================================
# 5️⃣ Delivery time per category
# ======================================================

query_delay = """
SELECT 
    p.product_category_name,
    ROUND(AVG(
        JULIANDAY(o.order_delivered_customer_date) 
        - JULIANDAY(o.order_purchase_timestamp)
    ), 2) AS avg_delivery_days
FROM clean_orders o
JOIN clean_order_items oi ON o.order_id = oi.order_id
JOIN clean_products p ON oi.product_id = p.product_id
WHERE o.order_status = 'delivered'
  AND o.order_delivered_customer_date IS NOT NULL
GROUP BY p.product_category_name
HAVING COUNT(*) > 50
ORDER BY avg_delivery_days DESC;
"""
df_delay = run_query(query_delay)
st.plotly_chart(plot_delivery_time(df_delay.head(15)), use_container_width=True)

# ======================================================
# 6️⃣ Interactive category explorer
# ======================================================

st.header("🔍 Explore a Category")

all_categories = sorted(df_qty["product_category_name"].unique())
selected_category = st.selectbox("Select a category", all_categories)

query_cat = f"""
SELECT 
    oi.price,
    oi.freight_value,
    r.review_score,
    p.product_category_name
FROM clean_order_items oi
JOIN clean_products p ON oi.product_id = p.product_id
JOIN clean_orders o ON oi.order_id = o.order_id
LEFT JOIN clean_reviews r ON o.order_id = r.order_id
WHERE p.product_category_name = '{selected_category}';
"""

df_cat = run_query(query_cat)
st.plotly_chart(plot_category_scatter(df_cat, selected_category), use_container_width=True)
