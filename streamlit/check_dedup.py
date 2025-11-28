import sqlite3

conn = sqlite3.connect('olist.db')
cursor = conn.cursor()

print("=== ANALYSE DÉDUPLICATION CLIENT ===\n")

# 1. Comparer customer_id vs customer_unique_id
cursor.execute("""
SELECT 
    COUNT(DISTINCT customer_id) as nb_customer_id,
    COUNT(DISTINCT customer_unique_id) as nb_customer_unique_id
FROM clean_customers
""")
result = cursor.fetchone()
print(f"1. Nombre d'IDs distincts :")
print(f"   customer_id: {result[0]}")
print(f"   customer_unique_id: {result[1]}")
print(f"   Différence: {result[0] - result[1]}\n")

# 2. Combien de customer_unique_id ont plusieurs customer_id ?
cursor.execute("""
SELECT COUNT(*) FROM (
    SELECT customer_unique_id
    FROM clean_customers
    GROUP BY customer_unique_id
    HAVING COUNT(DISTINCT customer_id) > 1
)
""")
nb_duplicates = cursor.fetchone()[0]
print(f"2. Nombre de customer_unique_id avec plusieurs customer_id: {nb_duplicates}\n")

# 3. Taux one-shot SANS déduplication (customer_id)
cursor.execute("""
SELECT
    SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) AS one_time,
    COUNT(*) AS total_clients
FROM (
    SELECT customer_id, COUNT(*) AS cnt
    FROM clean_orders
    GROUP BY customer_id
)
""")
result = cursor.fetchone()
pct_without = round(result[0] * 100 / result[1], 2)
print(f"3. Taux one-shot SANS déduplication (customer_id): {pct_without}%")
print(f"   One-time: {result[0]}, Total: {result[1]}\n")

# 4. Taux one-shot AVEC déduplication (customer_unique_id)
cursor.execute("""
SELECT
    SUM(CASE WHEN cnt = 1 THEN 1 ELSE 0 END) AS one_time,
    COUNT(*) AS total_clients
FROM (
    SELECT customer_unique_id, COUNT(*) AS cnt
    FROM clean_orders o
    JOIN clean_customers c ON o.customer_id = c.customer_id
    GROUP BY customer_unique_id
)
""")
result = cursor.fetchone()
pct_with = round(result[0] * 100 / result[1], 2)
print(f"4. Taux one-shot AVEC déduplication (customer_unique_id): {pct_with}%")
print(f"   One-time: {result[0]}, Total: {result[1]}\n")

print("=== CONCLUSION ===")
diff = pct_without - pct_with
print(f"Différence: {diff}%")
if abs(diff) < 1:
    print("✓ La déduplication fonctionne bien, le 97% est réel")
else:
    print(f"⚠ Problème ! Le vrai taux serait {pct_with}% au lieu de {pct_without}%")

conn.close()
