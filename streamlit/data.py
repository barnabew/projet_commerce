import sqlite3
import pandas as pd
import streamlit as st
import requests
import os

DB_PATH = "olist.db"
DB_URL = "https://huggingface.co/datasets/showbave/olist-db/resolve/main/olist.db"


@st.cache_resource
def download_database_once():
    """Télécharge la DB une seule fois par session Streamlit."""
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) < 5000000:
        with st.spinner("📥 Downloading olist.db from HuggingFace…"):
            r = requests.get(DB_URL)
            open(DB_PATH, "wb").write(r.content)
        st.success("✔ Database downloaded")

    return True


def get_connection():
    # Télécharge la DB si nécessaire (une seule fois grâce au cache)
    download_database_once()
    return sqlite3.connect(DB_PATH)


def run_query(query):
    conn = get_connection()
    df = pd.read_sql(query, conn)
    conn.close()
    return df


@st.cache_data
def load_table(table_name):
    conn = get_connection()
    df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
    conn.close()
    return df
