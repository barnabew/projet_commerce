import streamlit as st
import pandas as pd
import plotly.express as px
from utils import get_connection
import styles
import visuel
import queries

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="produit")



conn = get_connection()

# Section 1: Top catégories par CA
with st.expander("Top catégories par chiffre d'affaires", expanded=False):
    df_revenue = pd.read_sql(queries.QUERY_TOP_CATEGORIES_REVENUE, conn)

    fig = px.bar(
        df_revenue,
        x="revenue",
        y="category",
        orientation="h",
        title="Top 15 catégories – Chiffre d'affaires",
        labels={"revenue": "Revenue", "category": "Category"},
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 2: Délais de livraison
with st.expander("Délai moyen de livraison par catégorie", expanded=False):
    min_sales = st.slider("Min ventes par catégorie :", 20, 500, 50)

    df_delivery = pd.read_sql(queries.get_query_delivery_by_category(min_sales), conn)

    fig = px.bar(
        df_delivery.head(15),
        x="avg_delivery_days",
        y="category",
        orientation="h",
        title="Catégories les plus lentes (top 15)",
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 3: Satisfaction client
with st.expander("Satisfaction – Notes moyennes par catégorie", expanded=False):
    min_reviews = st.slider("Min reviews par catégorie :", 20, 1000, 100)

    df_reviews = pd.read_sql(queries.get_query_reviews_by_category(min_reviews), conn)

    fig = px.bar(
        df_reviews,
        x="avg_review_score",
        y="category",
        orientation="h",
        color="avg_review_score",
        color_continuous_scale="RdYlGn",
        title="Catégories les moins bien notées",
    )
    visuel.apply_theme(fig)
    st.plotly_chart(fig, use_container_width=True)

# Section 4: Catégories problématiques
with st.expander("Catégories problématiques", expanded=False):
    df_bad = pd.read_sql(queries.QUERY_PROBLEMATIC_CATEGORIES, conn)

    st.dataframe(df_bad)
