"""
styles.py
Gestion des styles CSS pour le dashboard Olist Analytics
"""

def get_page_config():
    """
    Configuration de la page Streamlit
    
    Returns:
        dict: Configuration à passer à st.set_page_config()
    """
    return {
        "page_title": "Olist Dashboard",
        "layout": "wide",
        "initial_sidebar_state": "collapsed"
    }


def get_custom_css():
    """
    Retourne le CSS personnalisé pour le dashboard (style Geckoboard)
    
    Returns:
        str: Code CSS complet avec balises <style>
    """
    return """
    <style>
    
    /* ========================================
       BASE STYLES - GECKOBOARD DARK THEME
       ======================================== */
    html, body, .stApp {
        background: #1a1d29 !important;
        font-family: 'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* REMOVE SIDEBAR */
    section[data-testid="stSidebar"] { display: none !important; }
    div[data-testid="collapsedControl"] { display: none !important; }

    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 2rem !important;
        max-width: 100% !important;
    }

    /* ========================================
       NAVBAR - GECKOBOARD STYLE
       ======================================== */
    
    /* Masquer les éléments par défaut de Streamlit dans la navbar */
    .navbar-buttons > div[data-testid="stVerticalBlock"] {
        gap: 0 !important;
    }
    
    .navbar-buttons {
        background: #1a1d29 !important;
        border-bottom: 1px solid #2d3142 !important;
        margin: -1rem -2rem 3rem -2rem !important;
        padding: 1.5rem 2rem 0 2rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        display: flex !important;
        align-items: stretch !important;
    }

    /* Colonnes de la navbar */
    .navbar-buttons [data-testid="column"] {
        flex: 1 !important;
        background: transparent !important;
        padding: 0 !important;
        margin: 0 !important;
    }

    .navbar-buttons [data-testid="column"] > div {
        background: transparent !important;
        padding: 0 !important;
    }

    /* Boutons de navigation inactifs - Style Geckoboard */
    .navbar-buttons button {
        width: 100% !important;
        height: 50px !important;
        min-height: 50px !important;
        padding: 0 24px !important;
        margin: 0 !important;
        background: #252936 !important;
        background-color: #252936 !important;
        border: 1px solid #2d3142 !important;
        border-bottom: 3px solid transparent !important;
        border-radius: 6px 6px 0 0 !important;
        color: #8b92a7 !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        letter-spacing: 0.3px !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
        text-transform: none !important;
    }

    /* Hover sur boutons inactifs */
    .nav-inactive button:hover {
        background: #ffffff !important;
        background-color: #ffffff !important;
        color: #1a1d29 !important;
        border-bottom-color: rgba(94, 129, 244, 0.4) !important;
    }

    /* Bouton actif - Rouge */
    .nav-active button {
        background: #ff4b4b !important;
        background-color: #ff4b4b !important;
        color: #ffffff !important;
        border-bottom-color: #ff4b4b !important;
        border-color: #ff1a1a !important;
        font-weight: 600 !important;
    }

    .nav-active button:hover {
        background: #ff6b6b !important;
        background-color: #ff6b6b !important;
        color: #ffffff !important;
    }

    .navbar-buttons button:focus,
    .navbar-buttons button:active {
        box-shadow: none !important;
        outline: none !important;
    }

    /* ========================================
       KPI CARDS - GECKOBOARD STYLE
       ======================================== */
    .kpi-card {
        background: #252936 !important;
        padding: 24px !important;
        border-radius: 8px !important;
        border: 1px solid #2d3142 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.2s ease !important;
    }

    .kpi-card:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        border-color: #3d4152 !important;
    }

    .kpi-label {
        color: #8b92a7 !important;
        font-size: 12px !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
        font-weight: 600 !important;
        margin-bottom: 8px !important;
    }

    .kpi-value {
        color: #ffffff !important;
        font-size: 32px !important;
        font-weight: 700 !important;
        line-height: 1.2 !important;
        letter-spacing: -0.5px !important;
    }

    /* ========================================
       CHART CONTAINERS - GECKOBOARD STYLE
       ======================================== */
    .chart-container {
        background: #252936 !important;
        padding: 24px !important;
        border-radius: 8px !important;
        border: 1px solid #2d3142 !important;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.2) !important;
        transition: all 0.2s ease !important;
    }

    .chart-container:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
        border-color: #3d4152 !important;
    }

    .chart-title {
        color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        margin-bottom: 6px !important;
    }

    .chart-subtitle {
        color: #8b92a7 !important;
        font-size: 13px !important;
        margin-bottom: 16px !important;
    }

    /* ========================================
       SECTION TITLE - GECKOBOARD STYLE
       ======================================== */
    .section-header {
        color: #ffffff !important;
        font-size: 22px !important;
        font-weight: 600 !important;
        margin: 32px 0 20px 0 !important;
        letter-spacing: -0.3px !important;
        padding-left: 12px !important;
        border-left: 3px solid #5e81f4 !important;
    }

    /* ========================================
       STREAMLIT ELEMENTS OVERRIDE
       ======================================== */
    
    /* Espacement entre les rangées de colonnes */
    [data-testid="column"] {
        padding: 0 0.75rem !important;
    }
    
    /* Espacement vertical entre les rangées */
    [data-testid="stHorizontalBlock"] {
        margin-bottom: 1.5rem !important;
    }
    
    /* Titres */
    h1, h2, h3 {
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    h1 {
        font-size: 2.2rem !important;
        margin-top: 1.5rem !important;
    }
    
    h2 {
        font-size: 1.6rem !important;
        margin-top: 1.2rem !important;
    }
    
    h3 {
        font-size: 1.3rem !important;
        margin-top: 1rem !important;
    }
    
    /* Texte */
    p, div, span, label {
        color: #c5c9d6 !important;
    }
    
    /* Dataframes / Tables */
    [data-testid="stDataFrame"] {
        background: #252936 !important;
        border: 1px solid #2d3142 !important;
        border-radius: 8px !important;
        padding: 1rem !important;
    }
    
    [data-testid="stDataFrame"] table {
        color: #ffffff !important;
    }
    
    [data-testid="stDataFrame"] th {
        background: #2d3344 !important;
        color: #ffffff !important;
        font-weight: 600 !important;
    }
    
    [data-testid="stDataFrame"] td {
        color: #c5c9d6 !important;
    }
    
    /* Graphiques Plotly */
    .js-plotly-plot {
        background: #252936 !important;
        border-radius: 8px !important;
    }
    
    /* Selectbox / Dropdowns */
    [data-baseweb="select"] {
        background: #252936 !important;
        border-radius: 6px !important;
    }
    
    [data-baseweb="select"] > div {
        background: #252936 !important;
        border: 1px solid #2d3142 !important;
        color: #ffffff !important;
    }
    
    /* Sliders */
    [data-testid="stSlider"] {
        padding: 1rem 0 !important;
    }
    
    [data-testid="stSlider"] [role="slider"] {
        background: #5e81f4 !important;
    }
    
    [data-testid="stSlider"] [data-baseweb="slider"] {
        background: #2d3142 !important;
    }
    
    /* Info boxes */
    .stAlert {
        background: #252936 !important;
        border: 1px solid #2d3142 !important;
        border-radius: 8px !important;
        color: #c5c9d6 !important;
    }
    
    [data-testid="stNotification"] {
        background: #252936 !important;
        border-radius: 8px !important;
    }
    
    /* Success boxes */
    .stSuccess {
        background: rgba(94, 244, 165, 0.1) !important;
        border-left: 4px solid #5ef4a5 !important;
        color: #5ef4a5 !important;
    }
    
    /* Warning boxes */
    .stWarning {
        background: rgba(255, 196, 0, 0.1) !important;
        border-left: 4px solid #ffc400 !important;
        color: #ffc400 !important;
    }
    
    /* Error boxes */
    .stError {
        background: rgba(255, 75, 75, 0.1) !important;
        border-left: 4px solid #ff4b4b !important;
        color: #ff4b4b !important;
    }
    
    /* Info boxes */
    .stInfo {
        background: rgba(94, 129, 244, 0.1) !important;
        border-left: 4px solid #5e81f4 !important;
        color: #5e81f4 !important;
    }
    
    /* Dividers */
    hr {
        border-color: #2d3142 !important;
        margin: 2rem 0 !important;
    }

    /* ========================================
       SCROLLBAR - GECKOBOARD STYLE
       ======================================== */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }

    ::-webkit-scrollbar-track {
        background: #1a1d29;
    }

    ::-webkit-scrollbar-thumb {
        background: #3d4152;
        border-radius: 4px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: #4d5262;
    }

    </style>
    """


def get_navbar_html():
    """
    Retourne le HTML de base pour la navbar
    (sans les boutons Streamlit qui sont ajoutés après)
    
    Returns:
        tuple: (html_start, html_end) pour encadrer les boutons
    """
    start = """
    <div class="navbar-container">
        <div class="navbar-content">
            <div class="navbar-brand">📊 Olist Analytics</div>
            <div class="navbar-buttons" id="navbar-buttons-container">
    """
    
    end = """
            </div>
        </div>
    </div>
    """
    
    return start, end


def render_navbar(st, current_page="resume"):
    """
    Affiche la navbar complète avec les boutons de navigation
    
    Args:
        st: module streamlit
        current_page: nom de la page active (resume, geographique, produit, clients, recommandations)
    """
    
    # Wrapper avec classe navbar-buttons
    st.markdown('<div class="navbar-buttons">', unsafe_allow_html=True)
    
    # Créer les colonnes pour les boutons
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # Configuration des pages
    pages = [
        ("resume", "Résumé", col1, "accueil.py"),
        ("geographique", "Géographique", col2, "pages/2_geographique.py"),
        ("produit", "Produits", col3, "pages/3_produit.py"),
        ("clients", "Clients", col4, "pages/4_clients.py"),
        ("recommandations", "Recommandations", col5, "pages/5_recommandations.py")
    ]
    
    # Afficher les boutons
    for page_id, label, col, url in pages:
        with col:
            is_active = current_page == page_id
            # Wrapper avec classe pour styling CSS
            wrapper_class = "nav-active" if is_active else "nav-inactive"
            st.markdown(f'<div class="{wrapper_class}">', unsafe_allow_html=True)
            
            if st.button(label, key=f"nav_{page_id}", use_container_width=True):
                st.switch_page(url)
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Fermer le wrapper
    st.markdown('</div>', unsafe_allow_html=True)
