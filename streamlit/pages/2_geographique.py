import streamlit as st
from data import run_query,get_connection
import plotly.express as px
import pandas as pd
import requests
import igraph as ig
import plotly.graph_objects as go
import styles
import textes
import visuel

st.session_state["page"] = "geographique"

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="geographique")


with st.expander("📍 Analyse par État", expanded=True):
        st.markdown(textes.analyse_carte_geo)
        
        # Chargement du GeoJSON
        @st.cache_resource
        def load_geojson():
            url = "https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson"
            return requests.get(url).json()

        geojson = load_geojson()

        # Récupération des données par état
        query = """
            SELECT 
                c.customer_state AS state,
                COUNT(DISTINCT o.order_id) AS nb_orders,
                SUM(oi.price + oi.freight_value) AS revenue,
                ROUND(SUM(oi.price + oi.freight_value) * 1.0 
                    / COUNT(DISTINCT o.order_id), 2) AS avg_order_value,
                ROUND(AVG(
                    JULIANDAY(o.order_delivered_customer_date) 
                    - JULIANDAY(o.order_purchase_timestamp)
                ), 2) AS avg_delivery_days,
                ROUND(AVG(r.review_score),2) AS avg_review_score
            FROM clean_orders o
            JOIN clean_customers c ON o.customer_id = c.customer_id
            JOIN clean_order_items oi ON oi.order_id = o.order_id
            LEFT JOIN clean_reviews r ON r.order_id = o.order_id
            WHERE o.order_status IN ('delivered','shipped','invoiced')
            GROUP BY c.customer_state;
        """

        df_state = run_query(query)

        # Sélection du type d'analyse
        analysis_type = st.selectbox(
            "Sélectionnez l’analyse affichée sur la carte :",
            [
                "Chiffre d’affaires",
                "Délai moyen",
                "Nombre de commandes",
                "Panier moyen",
                "Note moyenne"
            ]
        )

        metric_map = {
            "Chiffre d'affaires": ("revenue", "Chiffre d'affaires (R$)"),
            "Délai moyen": ("avg_delivery_days", "Délai moyen (jours)"),
            "Nombre de commandes": ("nb_orders", "Nombre de commandes"),
            "Panier moyen": ("avg_order_value", "Panier moyen (R$)"),
            "Note moyenne": ("avg_review_score", "Note moyenne"),
        }

        metric_col, metric_title = metric_map[analysis_type]

        # Carte choropleth
        fig = visuel.plot_choropleth_map(df_state, geojson, metric_col, f"{analysis_type} par État")
        st.plotly_chart(fig, use_container_width=True)

with st.expander("🔄 Flux Géographiques – Vendeur → Client", expanded=False):
    st.markdown(textes.analyse_flux_geo)
    
    # Chargement des flux
    query_flux = """
    SELECT 
        s.seller_state,
        c.customer_state,
        COUNT(*) AS nb_orders
    FROM clean_order_items coi
    JOIN clean_sellers s ON coi.seller_id = s.seller_id
    JOIN clean_orders o ON coi.order_id = o.order_id
    JOIN clean_customers c ON o.customer_id = c.customer_id
    WHERE o.order_status = 'delivered'
      AND o.order_delivered_customer_date IS NOT NULL
      AND o.order_purchase_timestamp IS NOT NULL
    GROUP BY s.seller_state, c.customer_state
    HAVING nb_orders > 10
    ORDER BY nb_orders DESC;
    """
    conn = get_connection()
    df = pd.read_sql(query_flux, conn)

    # Liste des états vendeurs
    seller_list = sorted(df['seller_state'].unique())

    # Sélecteur d'état vendeur
    selected_state = st.selectbox(
        "Sélectionner un État vendeur",
        seller_list,
        index=seller_list.index("SP") if "SP" in seller_list else 0
    )

    df_state = df[df["seller_state"] == selected_state].copy()

    st.subheader(f"Flux depuis : **{selected_state}**")

    if df_state.empty:
        st.info("Aucun flux significatif pour cet état.")
    else:
        # Diagramme Sankey pour un seul état
        fig = visuel.plot_sankey_flow(df_state, selected_state)
        st.plotly_chart(fig, use_container_width=True)

    # Tableau détaillé des flux
    st.subheader("Détails des flux")
    st.dataframe(df_state)
