import sqlite3
import pandas as pd
import os
import gdown
import streamlit as st

DB_PATH = "olist.db"

@st.cache_resource

def ensure_database():
    if not os.path.exists(DB_PATH):
        url = "https://drive.google.com/uc?id=XXXXXXXXX"
        gdown.download(url, DB_PATH, quiet=False)
    return DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH, check_same_thread=False)

@st.cache_data
def load_table(table_name):
    conn = get_connection()
    return pd.read_sql(f"SELECT * FROM {table_name}", conn)

@st.cache_data
def run_query(query):
    conn = get_connection()
    return pd.read_sql(query, conn)
