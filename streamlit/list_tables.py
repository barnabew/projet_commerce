import sqlite3
conn = sqlite3.connect('olist.db')
cursor = conn.cursor()
tables = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print("Tables disponibles:")
for t in tables:
    print(f"  - {t[0]}")
conn.close()
