"""
styles.py
Gestion des styles CSS pour le dashboard Retail Analytics
"""

def get_page_config():
    """Configuration de base pour toutes les pages"""
    return {
        "page_title": "Retail Analytics Dashboard",
        "layout": "wide",
        "initial_sidebar_state": "collapsed"
    }


def get_custom_css():
    """Retourne tout le CSS personnalisé pour le dashboard"""
    return """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #ffffff;
    }
    
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 95%;
    }
    
    /* Navbar */
    .navbar {
        background: rgba(0,0,0,0.8);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem 2rem;
        margin: 0 0 2rem 0;
        border: 1px solid rgba(255,255,255,0.1);
    }
    
    .navbar-brand {
        color: #ffffff !important;
        font-size: 1.5rem;
        font-weight: 700;
        margin-right: 2rem;
    }
    
    .navbar-nav {
        display: flex;
        gap: 0.5rem;
    }
    
    .nav-link {
        color: rgba(255,255,255,0.7) !important;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        transition: all 0.3s ease;
        text-decoration: none;
        font-weight: 500;
    }
    
    .nav-link:hover, .nav-link.active {
        color: #ffffff !important;
        background: rgba(255,255,255,0.1);
    }
    
    /* KPI Cards */
    .kpi-card {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .kpi-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.3);
    }
    
    .kpi-value {
        font-size: 2rem;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 0.5rem;
    }
    
    .kpi-label {
        font-size: 0.9rem;
        color: rgba(255,255,255,0.8);
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 500;
    }
    
    /* Section Headers */
    .section-header {
        background: linear-gradient(90deg, #FF6B6B 0%, #4ECDC4 100%);
        background-clip: text;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        text-align: center;
    }
    
    /* Streamlit Components */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.1);
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 10px;
    }
    
    .stSlider > div > div {
        background: rgba(255,255,255,0.1);
    }
    
    .stExpander {
        border: 1px solid rgba(255,255,255,0.2);
        border-radius: 10px;
        background: rgba(255,255,255,0.05);
    }
    
    /* Plotly Charts */
    .js-plotly-plot {
        border-radius: 15px;
        overflow: hidden;
    }
    
    /* Metrics */
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
        border: 1px solid rgba(255,255,255,0.2);
        padding: 1rem;
        border-radius: 10px;
        backdrop-filter: blur(10px);
    }
    
    div[data-testid="metric-container"] label {
        color: rgba(255,255,255,0.8) !important;
    }
    
    div[data-testid="metric-container"] div {
        color: #ffffff !important;
    }
    </style>
    """


def get_navbar_html():
    """Retourne le HTML de la navbar"""
    return """
    <div class="navbar">
        <span class="navbar-brand">🏪 Retail Analytics</span>
        <div class="navbar-nav">
            <a href="/" class="nav-link" id="nav-resume">📊 Résumé</a>
            <a href="/magasins" class="nav-link" id="nav-magasins">🏬 Magasins</a>
            <a href="/departements" class="nav-link" id="nav-departements">📦 Départements</a>
            <a href="/temporel" class="nav-link" id="nav-temporel">📈 Temporel</a>
            <a href="/recommandations" class="nav-link" id="nav-recommandations">💡 Recommandations</a>
        </div>
    </div>
    """


def render_kpi_card(label, value):
    """Génère une carte KPI"""
    return f"""
    <div class="kpi-card">
        <div class="kpi-value">{value}</div>
        <div class="kpi-label">{label}</div>
    </div>
    """


def render_chart_container(title, subtitle):
    """Génère un conteneur de graphique"""
    return f"""
    <div class="chart-container">
        <h3 class="chart-title">{title}</h3>
        <p class="chart-subtitle">{subtitle}</p>
    </div>
    """


def render_section_header(title):
    """Génère un en-tête de section"""
    return f'<h1 class="section-header">{title}</h1>'


def render_navbar(st, current_page="resume"):
    """Affiche la navbar avec la page courante mise en évidence"""
    navbar_html = get_navbar_html()
    st.markdown(navbar_html, unsafe_allow_html=True)
    
    # JavaScript pour mettre en évidence la page courante
    st.markdown(f"""
    <script>
        document.getElementById('nav-{current_page}').classList.add('active');
    </script>
    """, unsafe_allow_html=True)