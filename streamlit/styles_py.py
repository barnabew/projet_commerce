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
    Retourne le CSS personnalisé pour le dashboard
    
    Returns:
        str: Code CSS complet avec balises <style>
    """
    return """
    <style>
    
    /* ========================================
       BASE STYLES
       ======================================== */
    html, body, .stApp {
        background: linear-gradient(135deg, #0a1628 0%, #111d30 100%) !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* REMOVE SIDEBAR */
    section[data-testid="stSidebar"] { display: none !important; }
    div[data-testid="collapsedControl"] { display: none !important; }

    .block-container {
        padding-top: 1rem !important;
        max-width: 100% !important;
    }

    /* ========================================
       NAVBAR - HORIZONTAL LAYOUT
       ======================================== */
    .navbar-container {
        background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
        border-bottom: 2px solid rgba(77, 168, 255, 0.2);
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
        margin: -1rem -2rem 2.5rem -2rem;
        padding: 0;
    }

    .navbar-content {
        max-width: 1600px;
        margin: 0 auto;
        padding: 0 2rem;
        display: flex;
        align-items: center;
        gap: 0;
    }

    .navbar-brand {
        color: #4DA8FF;
        font-size: 20px;
        font-weight: 700;
        padding: 18px 24px 18px 0;
        letter-spacing: -0.5px;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        margin-right: 0;
        flex-shrink: 0;
    }

    .navbar-buttons {
        display: flex;
        flex: 1;
        gap: 0;
    }

    /* Style pour les colonnes Streamlit dans la navbar */
    .navbar-buttons [data-testid="column"] {
        flex: 1;
    }

    /* Masquer le style par défaut des boutons Streamlit */
    .navbar-buttons button {
        width: 100% !important;
        height: 100% !important;
        min-height: 54px !important;
        padding: 18px 16px !important;
        background: transparent !important;
        border: none !important;
        border-radius: 0 !important;
        color: #95adc7 !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        border-bottom: 3px solid transparent !important;
        transition: all 0.3s ease !important;
        box-shadow: none !important;
    }

    .navbar-buttons button:hover {
        background: rgba(77, 168, 255, 0.08) !important;
        color: #d4e3f5 !important;
        border-bottom-color: rgba(77, 168, 255, 0.3) !important;
    }

    .navbar-buttons button:focus,
    .navbar-buttons button:active {
        box-shadow: none !important;
        outline: none !important;
    }

    /* Bouton actif */
    .nav-active button {
        color: #ffffff !important;
        background: rgba(77, 168, 255, 0.12) !important;
        border-bottom-color: #4DA8FF !important;
        font-weight: 600 !important;
    }

    /* ========================================
       KPI CARDS
       ======================================== */
    .kpi-card {
        background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
        padding: 28px;
        border-radius: 12px;
        border: 1px solid rgba(77, 168, 255, 0.15);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        transition: all 0.3s ease;
    }

    .kpi-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 30px rgba(77, 168, 255, 0.15);
        border-color: rgba(77, 168, 255, 0.25);
    }

    .kpi-label {
        color: #95adc7;
        font-size: 13px;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .kpi-value {
        color: #ffffff;
        font-size: 34px;
        font-weight: 700;
        line-height: 1.2;
        letter-spacing: -0.5px;
    }

    /* ========================================
       CHART CONTAINERS
       ======================================== */
    .chart-container {
        background: linear-gradient(135deg, #162841 0%, #1a2f4a 100%);
        padding: 30px;
        border-radius: 12px;
        border: 1px solid rgba(77, 168, 255, 0.15);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
        transition: all 0.3s ease;
        min-height: 300px;
    }

    .chart-container:hover {
        box-shadow: 0 8px 30px rgba(77, 168, 255, 0.12);
        border-color: rgba(77, 168, 255, 0.22);
    }

    .chart-title {
        color: #ffffff;
        font-size: 18px;
        font-weight: 600;
        margin-bottom: 8px;
        letter-spacing: -0.3px;
    }

    .chart-subtitle {
        color: #95adc7;
        font-size: 14px;
        margin-bottom: 20px;
    }

    /* ========================================
       SECTION TITLE
       ======================================== */
    .section-header {
        color: #ffffff;
        font-size: 26px;
        font-weight: 700;
        margin: 40px 0 25px 0;
        letter-spacing: -0.5px;
        padding-left: 15px;
        border-left: 4px solid #4DA8FF;
    }

    /* ========================================
       SCROLLBAR
       ======================================== */
    ::-webkit-scrollbar {
        width: 10px;
        height: 10px;
    }

    ::-webkit-scrollbar-track {
        background: #0a1628;
    }

    ::-webkit-scrollbar-thumb {
        background: rgba(77, 168, 255, 0.3);
        border-radius: 5px;
    }

    ::-webkit-scrollbar-thumb:hover {
        background: rgba(77, 168, 255, 0.5);
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