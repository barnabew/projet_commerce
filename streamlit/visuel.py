import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

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
