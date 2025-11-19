from data import run_query,get_connection,load_table
from textes import intro
import streamlit as st


st.set_page_config(page_title="Résumé général", layout="wide")

# -------------------------------------------------------------
# 🟦 TITRE DE LA PAGE
# -------------------------------------------------------------
st.title("📊 Résumé général du commerce Olist")

st.markdown(
    """
    Cette page présente une synthèse des indicateurs clés du dataset Olist.
    Elle permet d'obtenir une vision rapide et globale de la performance :
    chiffre d'affaires, panier moyen, délai de livraison et satisfaction client.
    """
)

st.markdown("---")

# -------------------------------------------------------------
# 🟦 RÉCUPÉRATION DES KPI
# -------------------------------------------------------------

# Chiffre d'affaires
df_revenue = run_query("""
SELECT 
    SUM(oi.price + oi.freight_value) AS total_revenue
FROM clean_order_items oi
JOIN clean_orders o 
    ON oi.order_id = o.order_id
WHERE o.order_status IN ('delivered','shipped','invoiced');
""")
total_revenue = df_revenue["total_revenue"][0]

# Panier moyen
df_avg_cart = run_query("""
SELECT 
    SUM(price + freight_value) * 1.0 
    / COUNT(DISTINCT order_id) AS avg_cart
FROM clean_order_items;
""")
avg_cart = df_avg_cart["avg_cart"][0]

# Délai moyen
df_delay = run_query("""
SELECT 
    ROUND(AVG(
        JULIANDAY(order_delivered_customer_date) 
        - JULIANDAY(order_purchase_timestamp)
    ), 2) AS avg_delay
FROM clean_orders
WHERE order_status='delivered';
""")
avg_delay = df_delay["avg_delay"][0]

# Note moyenne
df_review = run_query("""
SELECT ROUND(AVG(review_score),2) AS avg_score
FROM clean_reviews;
""")
avg_score = df_review["avg_score"][0]

# Nombre de commandes validées
df_orders = run_query("""
SELECT COUNT(*) AS nb_orders
FROM clean_orders
WHERE order_status IN ('delivered','shipped','invoiced');
""")
nb_orders = df_orders["nb_orders"][0]

# Nombre de clients
df_customers = run_query("""
SELECT COUNT(DISTINCT customer_unique_id) AS nb_customers
FROM clean_customers;
""")
nb_customers = df_customers["nb_customers"][0]

# Nombre de vendeurs actifs
df_sellers = run_query("""
SELECT COUNT(DISTINCT seller_id) AS nb_sellers
FROM clean_sellers;
""")
nb_sellers = df_sellers["nb_sellers"][0]

# -------------------------------------------------------------
# 🟦 AFFICHAGE DES KPI (style PRO)
# -------------------------------------------------------------
def kpi_card(label, value, sub=None):
    st.markdown(
        f"""
        <div style="
            padding: 18px;
            border-radius: 12px;
            background-color: #F7F7F9;
            border: 1px solid #E0E0E0;
            box-shadow: 0 1px 2px rgba(0,0,0,0.05);
            text-align: center;
            height: 110px;
        ">
            <div style="font-size: 16px; font-weight: 600; color:#333;">{label}</div>
            <div style="font-size: 26px; font-weight: 700; margin-top: 4px; color:#000;">
                {value}
            </div>
            <div style="font-size: 13px; color:#888; margin-top: 2px;">
                {sub if sub else ""}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# Affichage en 2 lignes
col1, col2, col3, col4 = st.columns(4)
with col1:
    kpi_card("💰 Chiffre d'affaires total", f"{total_revenue:,.0f} R$")
with col2:
    kpi_card("🛒 Panier moyen", f"{avg_cart:,.2f} R$")
with col3:
    kpi_card("⏱️ Délai moyen", f"{avg_delay} j")
with col4:
    kpi_card("⭐ Note moyenne", avg_score)

st.markdown("")

col5, col6, col7 = st.columns(3)
with col5:
    kpi_card("📦 Nombre de commandes", f"{nb_orders:,}")
with col6:
    kpi_card("👥 Clients uniques", f"{nb_customers:,}")
with col7:
    kpi_card("🏬 Vendeurs actifs", f"{nb_sellers:,}")

st.markdown("---")

st.info(
    "ℹ️ Les analyses détaillées sont disponibles dans les sections suivantes : "
    "**Géographie**, **Produits**, et **Segmentation Clients**."
)
