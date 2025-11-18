import sqlite3
import pandas as pd
import streamlit as st
import gdown
import os

DB_PATH = "olist.db"


@st.cache_resource
def ensure_database():
    """Télécharge olist.db si absente ou trop petite (fichier vide)."""
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) < 5000000:
        st.warning("📥 Downloading olist.db from Google Drive…")

        url = "https://drive.google.com/uc?id=XXXXXXXXXXXX"  # <-- ton ID
        gdown.download(url, DB_PATH, quiet=False)

        st.success("✔ Database downloaded")

    return DB_PATH

def get_connection():
    ensure_database()
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
