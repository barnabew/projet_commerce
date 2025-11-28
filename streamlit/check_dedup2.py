import requests
import sqlite3
import os

DB_PATH = "olist.db"
DB_URL = "https://huggingface.co/datasets/showbave/olist-db/resolve/main/olist.db"

# Télécharger si nécessaire
if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) < 5000000:
    print("Téléchargement de la base de données...")
    r = requests.get(DB_URL)
    open(DB_PATH, "wb").write(r.content)
    print("✓ Base téléchargée\n")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

print("=== ANALYSE DÉDUPLICATION CLIENT ===\n")

# Lister les tables
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables disponibles:")
for t in tables:
    print(f"  - {t[0]}")
print()

# Trouver la table customers
customer_tables = [t[0] for t in tables if 'customer' in t[0].lower()]
if not customer_tables:
    print("Aucune table customers trouvée!")
    conn.close()
    exit()

customer_table = customer_tables[0]
print(f"Utilisation de la table: {customer_table}\n")

# 1. Comparer customer_id vs customer_unique_id
cursor.execute(f"""
SELECT 
    COUNT(DISTINCT customer_id) as nb_customer_id,
    COUNT(DISTINCT customer_unique_id) as nb_customer_unique_id
FROM {customer_table}
""")
result = cursor.fetchone()
print(f"1. Nombre d'IDs distincts :")
print(f"   customer_id: {result[0]}")
print(f"   customer_unique_id: {result[1]}")
print(f"   Différence: {result[0] - result[1]}\n")

# Trouver la table orders
order_tables = [t[0] for t in tables if 'order' in t[0].lower() and 'item' not in t[0].lower()]
if not order_tables:
    print("Aucune table orders trouvée!")
    conn.close()
    exit()

order_table = order_tables[0]
print(f"Utilisation de la table: {order_table}\n")

# 2. Taux one-shot SANS déduplication (customer_id)
cursor.execute(f"""
SELECT
    SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) AS one_time,
    COUNT(*) AS total_clients
FROM (
    SELECT customer_id, COUNT(*) AS cnt
    FROM {order_table}
    GROUP BY customer_id
)
""")
result = cursor.fetchone()
pct_without = round(result[0] * 100 / result[1], 2)
print(f"2. Taux one-shot SANS déduplication (customer_id): {pct_without}%")
print(f"   One-time: {result[0]}, Total: {result[1]}\n")

# 3. Taux one-shot AVEC déduplication (customer_unique_id)
cursor.execute(f"""
SELECT
    SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) AS one_time,
    COUNT(*) AS total_clients
FROM (
    SELECT customer_unique_id, COUNT(*) AS cnt
    FROM {order_table} o
    JOIN {customer_table} c ON o.customer_id = c.customer_id
    GROUP BY customer_unique_id
)
""")
result = cursor.fetchone()
pct_with = round(result[0] * 100 / result[1], 2)
print(f"3. Taux one-shot AVEC déduplication (customer_unique_id): {pct_with}%")
print(f"   One-time: {result[0]}, Total: {result[1]}\n")

print("=== CONCLUSION ===")
diff = pct_without - pct_with
print(f"Différence: {diff}%")
if abs(diff) < 1:
    print("✓ La déduplication fonctionne bien, le 97% est réel")
else:
    print(f"⚠ PROBLÈME ! Le vrai taux serait {pct_with}% au lieu de {pct_without}%")
    print(f"⚠ Il y a probablement des doublons de clients non détectés")

conn.close()
