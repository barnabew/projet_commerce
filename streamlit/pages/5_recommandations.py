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

# Section 1: Logistique
with st.expander("1. Logistique & Délais de Livraison", expanded=False):
    st.subheader("Problèmes identifiés")
    st.markdown(textes.reco_logistique_problemes)

    st.subheader("Recommandations")
    st.markdown(textes.reco_logistique_actions)

# Section 2: Produits
with st.expander("2. Produits & Assortiment", expanded=False):
    st.subheader("Problèmes identifiés")
    st.markdown(textes.reco_produits_problemes)

    st.subheader("Recommandations")
    st.markdown(textes.reco_produits_actions)

# Section 3: Géographie
with st.expander("3. Géographie & Expansion", expanded=False):
    st.subheader("Constat")
    st.markdown(textes.reco_geo_constat)

    st.subheader("Recommandations")
    st.markdown(textes.reco_geo_actions)

# Section 4: Clients
with st.expander("4. Clients & Comportement d'Achat", expanded=False):
    st.subheader("Observations clés")
    st.markdown(textes.reco_clients_observations)

    st.subheader("Recommandations")
    st.markdown(textes.reco_clients_actions)# Section 5: Priorités stratégiques
with st.expander("5. Priorités Stratégiques (Top 5)", expanded=True):
    st.markdown(textes.reco_priorites)

    st.success(textes.reco_conclusion)