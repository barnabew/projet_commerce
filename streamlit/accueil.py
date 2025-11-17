import streamlit as st
from ml import reg_lineaire, train_test
from data import chargement_nettoyage
from textes import intro
import pickle

st.set_page_config(
    page_title="Analyse et Prédiction du Churn Client",
    page_icon="📉",
    layout="wide"
)

st.title("Projet : Analyse businness e-commerce")
st.markdown(intro)

st.sidebar.success("Choisissez une page ci-dessus pour commencer.")
