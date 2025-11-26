import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import run_query
import styles
import textes
import visuel
import queries

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="clients")

st.markdown(styles.render_section_header("Analyse Clients"), unsafe_allow_html=True)
st.markdown(textes.intro_clients)

# Section 1: Indicateurs clés
with st.expander("📊 Indicateurs clés des clients", expanded=True):
    df_kpi = run_query(queries.QUERY_CLIENT_KPI)

    pct_one_time = round(df_kpi["one_time"][0] * 100 / df_kpi["total_clients"][0], 2)

    avg_item = run_query(queries.QUERY_AVG_BASKET)["avg_item"][0]

    avg_score = run_query(queries.QUERY_AVG_REVIEW_SCORE)["avg"][0]

    col1, col2, col3 = st.columns(3)
    col1.metric("Clients one-time", f"{pct_one_time} %")
    col2.metric("Panier moyen (par article)", f"{avg_item} R$")
    col3.metric("Note moyenne", avg_score)

# Section 2: Catégories d'acquisition
with st.expander("🎯 Catégories qui attirent le plus de nouveaux clients", expanded=False):
    df_acq = run_query(queries.QUERY_ACQUISITION_CATEGORIES)

    fig_acq = px.bar(
        df_acq,
        x="category",
        y="first_order_count",
        title="Top 15 catégories (premier achat)",
        labels={"first_order_count": "Nouveaux clients"}
    )
    fig_acq.update_layout(
        xaxis_title="Catégorie",
        yaxis_title="Nombre de nouveaux clients"
    )
    visuel.apply_theme(fig_acq)
    st.plotly_chart(fig_acq, use_container_width=True)

    st.markdown(textes.insight_categories_acquisition)

# Section 3: Mauvaises premières expériences
with st.expander("❌ Catégories avec les pires premières expériences", expanded=False):
    df_bad = run_query(queries.QUERY_BAD_FIRST_EXPERIENCE)

    fig_bad = px.bar(
        df_bad,
        x="category",
        y="bad_review_rate",
        color="bad_review_rate",
        color_continuous_scale="Reds",
        title="Taux de mauvaises reviews (first-time buyers)",
        labels={"bad_review_rate": "% Bad Reviews"}
    )
    fig_bad.update_layout(
        xaxis_title="Catégorie",
        yaxis_title="% Bad Reviews"
    )
    visuel.apply_theme(fig_bad)
    st.plotly_chart(fig_bad, use_container_width=True)

    st.markdown(textes.insight_mauvaises_experiences)

# Section 4: Impact du délai
with st.expander("⏱️ Impact du délai sur la satisfaction des nouveaux clients", expanded=False):
    df_delay = run_query(queries.QUERY_DELAY_IMPACT_NEW_CLIENTS)

    colA, colB = st.columns(2)
    colA.metric("Délai moyen (first-time)", f"{df_delay['avg_delivery_days'][0]} jours")
    colB.metric("Note moyenne (first-time)", df_delay['avg_score'][0])

    st.markdown(textes.insight_impact_delai)

# Section 5: Recommandations
with st.expander("💡 Recommandations Business", expanded=False):
    st.markdown(textes.recommandations_clients)
