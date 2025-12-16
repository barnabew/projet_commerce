import sqlite3
import pandas as pd
import streamlit as st
import os

DB_PATH = "retail.db"

def get_connection():
    """Retourne une connexion à la base de données retail"""
    if not os.path.exists(DB_PATH):
        st.error(f"Base de données {DB_PATH} non trouvée. Veuillez d'abord exécuter le notebook pour créer la base.")
        st.stop()
    
    return sqlite3.connect(DB_PATH)


@st.cache_data(ttl=3600)  # Cache pendant 1 heure
def run_query(query):
    """Exécute une requête SQL et retourne un DataFrame"""
    conn = get_connection()
    try:
        df = pd.read_sql(query, conn)
        return df
    except Exception as e:
        st.error(f"Erreur lors de l'exécution de la requête: {e}")
        return pd.DataFrame()
    finally:
        conn.close()


@st.cache_data(ttl=3600)  # Cache pendant 1 heure
def load_table(table_name):
    """Charge une table complète"""
    conn = get_connection()
    try:
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        return df
    except Exception as e:
        st.error(f"Erreur lors du chargement de la table {table_name}: {e}")
        return pd.DataFrame()
    finally:
        conn.close()


def check_database():
    """Vérifie l'existence et la validité de la base de données"""
    if not os.path.exists(DB_PATH):
        return False, "Base de données non trouvée"
    
    try:
        conn = get_connection()
        tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'", conn)
        required_tables = ['sales', 'stores', 'features']
        
        missing_tables = [table for table in required_tables if table not in tables['name'].values]
        
        conn.close()
        
        if missing_tables:
            return False, f"Tables manquantes: {missing_tables}"
        
        return True, "Base de données OK"
    
    except Exception as e:
        return False, f"Erreur de connexion: {e}"