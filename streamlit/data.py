import os
import requests
import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "olist.db"

@st.cache_resource
def ensure_database():
    """Télécharge la DB depuis HuggingFace si absente."""
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) < 5000000:
        st.warning("📥 Downloading olist.db from HuggingFace…")

        url = "https://huggingface.co/datasets/showbave/olist-db/resolve/main/olist.db"
        r = requests.get(url)
        open(DB_PATH, "wb").write(r.content)

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
