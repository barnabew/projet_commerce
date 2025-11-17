import plotly.express as px

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
