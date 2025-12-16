import streamlit as st
import styles
import textes

# Configuration de la page
st.set_page_config(**styles.get_page_config())

# Application du CSS personnalisé
st.markdown(styles.get_custom_css(), unsafe_allow_html=True)

# Navbar
styles.render_navbar(st, current_page="recommandations")

st.markdown(textes.intro_recommandations)

# Section 1: Optimisation par type de magasin
with st.expander("1. Optimisation par Type de Magasin", expanded=True):
    st.subheader("Constats clés")
    st.markdown(textes.reco_magasins_constats)

    st.subheader("Recommandations")
    st.markdown(textes.reco_magasins_actions)

# Section 2: Assortiment départemental
with st.expander("2. Stratégie d'Assortiment Départemental", expanded=False):
    st.subheader("Observations")
    st.markdown(textes.reco_departements_observations)

    st.subheader("Recommandations")
    st.markdown(textes.reco_departements_actions)

# Section 3: Saisonnalité
with st.expander("3. Exploitation de la Saisonnalité", expanded=False):
    st.subheader("Patterns identifiés")
    st.markdown(textes.reco_saisonnalite_patterns)

    st.subheader("Recommandations")
    st.markdown(textes.reco_saisonnalite_actions)

# Section 4: Promotions
with st.expander("4. Stratégie Promotionnelle", expanded=False):
    st.subheader("Constats")
    st.markdown(textes.reco_promotions_constats)

    st.subheader("Recommandations")
    st.markdown(textes.reco_promotions_actions)

# Section 5: Priorités stratégiques
with st.expander("5. Priorités Stratégiques (Top 5)", expanded=True):
    st.markdown(textes.reco_priorites)

    st.success(textes.reco_conclusion)