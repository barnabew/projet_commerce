import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ===========================
# CONFIGURATION THEME
# ===========================

THEME_CONFIG = {
    "paper_bgcolor": "#252936",
    "plot_bgcolor": "#252936",
    "font": dict(color="#ffffff"),
    "title": dict(font=dict(color="#ffffff")),
    "xaxis": dict(gridcolor="#2d3142"),
    "yaxis": dict(gridcolor="#2d3142")
}

def apply_theme(fig):
    """Applique le thème sombre à un graphique Plotly"""
    fig.update_layout(**THEME_CONFIG)
    return fig

# ===========================
# CARTES GÉOGRAPHIQUES
# ===========================

def plot_choropleth_map(df_state, geojson, metric_col, metric_title):
    """
    Crée une carte choroplèthe du Brésil par état
    
    Args:
        df_state: DataFrame avec colonnes state, metric_col
        geojson: Données GeoJSON des états du Brésil
        metric_col: Nom de la colonne à afficher
        metric_title: Titre de la métrique
    """
    import plotly.express as px
    
    fig = px.choropleth(
        df_state,
        geojson=geojson,
        locations="state",
        featureidkey="properties.sigla",
        color=metric_col,
        color_continuous_scale="Viridis",
        hover_data={
            "state": True,
            "nb_orders": True,
            "revenue": True,
            "avg_order_value": True,
            "avg_delivery_days": True,
            "avg_review_score": True,
            metric_col: True,
        },
        labels={
            "state": "État",
            "revenue": "CA (R$)",
            "nb_orders": "Nbre commandes",
            "avg_order_value": "Panier moyen",
            "avg_delivery_days": "Délai moyen",
            "avg_review_score": "Note moyenne"
        },
        title=metric_title
    )
    
    fig.update_geos(fitbounds="locations", visible=False, bgcolor="#252936")
    fig.update_layout(
        margin={"r":0,"t":40,"l":0,"b":0},
        geo=dict(bgcolor="#252936", lakecolor="#252936")
    )
    apply_theme(fig)
    
    return fig


def plot_sankey_flow(df_state, selected_state):
    """
    Crée un diagramme Sankey pour les flux vendeur → client
    
    Args:
        df_state: DataFrame filtré pour un état vendeur
        selected_state: Code de l'état vendeur sélectionné
    """
    import plotly.graph_objects as go
    
    sources = [0] * len(df_state)
    targets = list(range(1, len(df_state) + 1))
    values = df_state["nb_orders"].tolist()
    
    labels = [f"{selected_state} (vendeur)"] + list(df_state["customer_state"])
    
    fig = go.Figure(
        data=[
            go.Sankey(
                node=dict(
                    pad=15,
                    thickness=20,
                    label=labels
                ),
                link=dict(
                    source=sources,
                    target=targets,
                    value=values
                ),
            )
        ]
    )
    
    fig.update_layout(height=600)
    apply_theme(fig)
    
    return fig

# ===========================
# Delivery Time by State
# ===========================

def plot_delivery_by_state(df):
    fig = px.bar(
        df,
        x="customer_state",
        y="avg_delivery_days",
        title="Average Delivery Time per Destination State",
        color="avg_delivery_days",
        color_continuous_scale="Viridis"
    )
    fig.update_xaxes(categoryorder="total descending")
    return fig


# ===========================
# Seller → Customer Flows (Sankey)
# ===========================

def plot_logistic_flow(df):
    fig = px.sunburst(
        df,
        path=["seller_state", "customer_state"],
        values="nb_orders",
        title="Seller → Customer State Flow"
    )
    return fig


# ===========================
# Heatmap state-to-state delivery
# ===========================

def plot_state_heatmap(df):
    fig = px.density_heatmap(
        df,
        x="seller_state",
        y="customer_state",
        z="nb_orders",
        color_continuous_scale="Viridis",
        title="Orders Flow Heatmap (Seller → Customer State)"
    )
    return fig


# ===========================
# Scatter: delivery time vs review score
# ===========================

def plot_delay_vs_review(df):
    fig = px.scatter(
        df,
        x="delivery_days",
        y="review_score",
        opacity=0.4,
        trendline="ols",
        title="Impact of Delivery Delay on Review Score"
    )
    return fig

# ===========================
# FM Heatmap
# ===========================

def plot_fm_heatmap(df):
    fig = px.density_heatmap(
        df,
        x="frequency",
        y="monetary",
        nbinsx=20,
        nbinsy=20,
        title="FM Density Heatmap"
    )
    return fig


# ===========================
# FM Scatter (log monetary)
# ===========================

def plot_fm_scatter(df):
    import numpy as np
    fig = px.scatter(
        df,
        x="frequency",
        y=np.log1p(df["monetary"]),
        color="segment",
        title="FM Scatter (log monetary)",
        opacity=0.6
    )
    return fig


# ===========================
# Distribution of segments
# ===========================

def plot_segment_distribution(df):
    fig = px.bar(
        df.groupby("segment")["customer_unique_id"].count().reset_index(),
        x="segment",
        y="customer_unique_id",
        title="Customer Segment Distribution",
        color="segment"
    )
    return fig

# ===========================
# Top Revenue Categories
# ===========================

def plot_top_categories_revenue(df):
    fig = px.bar(
        df,
        x="revenue",
        y="product_category_name",
        orientation="h",
        title="Top 10 Categories by Revenue",
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig


# ===========================
# Top Sales Categories
# ===========================

def plot_top_categories_sales(df):
    fig = px.bar(
        df,
        x="sales_count",
        y="product_category_name",
        orientation="h",
        title="Top 10 Categories by Sales Volume",
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    return fig


# ===========================
# Average Price by Category
# ===========================

def plot_avg_price(df):
    fig = px.bar(
        df,
        x="product_category_name",
        y="avg_price",
        title="Categories With the Highest Average Price",
    )
    fig.update_xaxes(tickangle=45)
    return fig


# ===========================
# Best Rated
# ===========================

def plot_best_rated(df):
    fig = px.bar(
        df,
        x="product_category_name",
        y="avg_review",
        color="avg_review",
        title="Top 10 Best Rated Categories",
    )
    fig.update_xaxes(tickangle=45)
    return fig


# ===========================
# Worst Rated
# ===========================

def plot_worst_rated(df):
    fig = px.bar(
        df,
        x="product_category_name",
        y="avg_review",
        color="avg_review",
        title="Bottom 10 Worst Rated Categories",
    )
    fig.update_xaxes(tickangle=45)
    return fig


# ===========================
# Delivery Time by Category
# ===========================

def plot_delivery_time(df):
    fig = px.bar(
        df,
        x="product_category_name",
        y="avg_delivery_days",
        title="Categories With the Longest Delivery Time",
    )
    fig.update_xaxes(tickangle=45)
    return fig


# ===========================
# Category Explorer (Price vs Freight vs Reviews)
# ===========================

def plot_category_scatter(df, selected_category):
    fig = px.scatter(
        df,
        x="price",
        y="freight_value",
        size="review_score",
        color="review_score",
        title=f"Price vs Freight Cost – {selected_category}",
    )
    return fig
