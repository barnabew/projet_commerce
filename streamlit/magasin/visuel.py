import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# ===========================
# CONFIGURATION THEME
# ===========================

THEME_CONFIG = {
    "paper_bgcolor": "#1e3c72",
    "plot_bgcolor": "#1e3c72", 
    "font": dict(color="#ffffff", family="Inter"),
    "title": dict(font=dict(color="#ffffff", size=16, family="Inter")),
    "xaxis": dict(
        gridcolor="#2d3142",
        color="#ffffff",
        linecolor="#2d3142"
    ),
    "yaxis": dict(
        gridcolor="#2d3142", 
        color="#ffffff",
        linecolor="#2d3142"
    ),
    "colorway": [
        "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEAA7",
        "#DDA0DD", "#98D8C8", "#FDCB6E", "#6C5CE7", "#A29BFE"
    ]
}

def apply_theme(fig):
    """Applique le thème sombre retail au graphique Plotly"""
    fig.update_layout(**THEME_CONFIG)
    
    # Configuration supplémentaire pour un look moderne
    fig.update_layout(
        margin=dict(t=50, l=50, r=50, b=50),
        showlegend=True,
        legend=dict(
            bgcolor="rgba(255,255,255,0.1)",
            bordercolor="rgba(255,255,255,0.2)",
            borderwidth=1
        )
    )
    
    # Style pour les axes
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor="rgba(255,255,255,0.1)"
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1, 
        gridcolor="rgba(255,255,255,0.1)"
    )
    
    return fig

# ===========================
# GRAPHIQUES SPÉCIALISÉS RETAIL
# ===========================

def plot_performance_by_type(df):
    """Graphique de performance par type de magasin"""
    fig = px.bar(
        df,
        x="Type",
        y="CA_Moyen",
        color="Type",
        title="Performance par Type de Magasin",
        color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#45B7D1"]
    )
    
    apply_theme(fig)
    return fig

def plot_correlation_scatter(df):
    """Graphique de corrélation taille-performance"""
    fig = px.scatter(
        df,
        x="Size",
        y="CA_Moyen",
        color="Type",
        title="Corrélation Taille vs Performance",
        trendline="ols",
        color_discrete_sequence=["#FF6B6B", "#4ECDC4", "#45B7D1"]
    )
    
    apply_theme(fig)
    return fig

def plot_department_ranking(df, title="Top Départements"):
    """Graphique en barres horizontales pour les départements"""
    fig = px.bar(
        df,
        x="CA_Total",
        y="Dept",
        orientation="h",
        title=title,
        color="CA_Total",
        color_continuous_scale="viridis"
    )
    
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    apply_theme(fig)
    return fig

def plot_temporal_evolution(df, y_columns, title="Évolution Temporelle"):
    """Graphique temporel multi-lignes"""
    fig = px.line(
        df,
        x="Nom_Mois",
        y=y_columns,
        title=title,
        markers=True
    )
    
    # Personnalisation des lignes
    for i, trace in enumerate(fig.data):
        trace.line.width = 3.5
        if i < len(THEME_CONFIG["colorway"]):
            trace.line.color = THEME_CONFIG["colorway"][i]
    
    apply_theme(fig)
    return fig

def plot_seasonal_departments(df, title="Départements Saisonniers"):
    """Graphique de variation saisonnière"""
    fig = px.bar(
        df,
        x="Dept",
        y="Coefficient_Variation",
        title=title,
        color="Coefficient_Variation",
        color_continuous_scale="plasma"
    )
    
    apply_theme(fig)
    return fig

def plot_segmentation_pie(df, title="Segmentation"):
    """Graphique en secteurs pour la segmentation"""
    fig = px.pie(
        df,
        values="Nb_Depts",
        names="Categorie",
        title=title,
        color_discrete_sequence=THEME_CONFIG["colorway"]
    )
    
    apply_theme(fig)
    return fig

def plot_promotion_impact(df, title="Impact Promotions"):
    """Graphique d'impact des promotions"""
    fig = px.bar(
        df,
        x="Statut_Promo",
        y="CA_Moyen",
        title=title,
        color="CA_Moyen",
        color_continuous_scale="viridis"
    )
    
    apply_theme(fig)
    return fig

# ===========================
# UTILITAIRES
# ===========================

def format_currency(value):
    """Formate une valeur en devise"""
    return f"${value:,.0f}"

def format_percentage(value):
    """Formate une valeur en pourcentage"""
    return f"{value:.1f}%"

def get_color_palette(n_colors):
    """Retourne une palette de couleurs"""
    colors = THEME_CONFIG["colorway"]
    if n_colors <= len(colors):
        return colors[:n_colors]
    else:
        # Répète les couleurs si nécessaire
        return (colors * ((n_colors // len(colors)) + 1))[:n_colors]