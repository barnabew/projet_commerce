import streamlit as st

st.set_page_config(layout="wide")

# -------------------------------
# DASHBOARD DARK GECKOBOARD
# -------------------------------
st.markdown("""
<style>

    /* Remove Streamlit padding */
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 100% !important;
    }

    /* Background color full screen */
    body {
        background-color: #0E1A2B;
    }

    .stApp {
        background-color: #0E1A2B;
    }

    /* Title */
    h1, h2, h3, h4, h5 {
        color: white !important;
        font-weight: 600;
    }

    /* KPI cards like Geckoboard */
    .card {
        background-color: #152B44;
        padding: 25px;
        border-radius: 12px;
        margin: 10px;
        text-align: left;
        border: 1px solid rgba(255,255,255,0.05);
    }

    .card h2 {
        font-size: 28px;
        color: white;
        margin: 0;
        padding: 0;
    }

    .card p {
        color: #8CA3C1;
        margin: 0;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)

# Titel
st.markdown("<h1 style='text-align:center;'>📊 OLIST DASHBOARD — Résumé</h1>", unsafe_allow_html=True)

# -------------------------------
# KPI ROW
# -------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("<div class='card'><p>Revenue</p><h2>R$ 15.6M</h2></div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'><p>Commandes</p><h2>99 441</h2></div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='card'><p>Note moyenne</p><h2>4.19 / 5</h2></div>", unsafe_allow_html=True)

with col4:
    st.markdown("<div class='card'><p>Délai moyen</p><h2>12.5 jours</h2></div>", unsafe_allow_html=True)

# -------------------------------
# GRID 2×2 FOR GRAPHS
# -------------------------------
c1, c2 = st.columns(2)
c3, c4 = st.columns(2)

with c1:
    st.markdown("<div class='card'><h3>Graphique 1</h3></div>", unsafe_allow_html=True)

with c2:
    st.markdown("<div class='card'><h3>Graphique 2</h3></div>", unsafe_allow_html=True)

with c3:
    st.markdown("<div class='card'><h3>Graphique 3</h3></div>", unsafe_allow_html=True)

with c4:
    st.markdown("<div class='card'><h3>Graphique 4</h3></div>", unsafe_allow_html=True)
