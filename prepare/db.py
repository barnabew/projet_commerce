import os
import sqlite3
import pandas as pd

CSV_PATH = os.path.join("data", "db_commerce")
DB_PATH = "olist.db"

conn = sqlite3.connect(DB_PATH)

files = [f for f in os.listdir(CSV_PATH) if f.endswith(".csv")]

for file in files:
    df = pd.read_csv(os.path.join(CSV_PATH, file))
    table_name = file.replace(".csv", "")
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded table: {table_name}")


queries = [

    # Clean orders
    """
    DROP TABLE IF EXISTS clean_orders;
    CREATE TABLE clean_orders AS
    SELECT
        order_id,
        customer_id,
        order_status,
        datetime(order_purchase_timestamp) AS order_purchase_timestamp,
        datetime(order_approved_at) AS order_approved_at,
        datetime(order_delivered_carrier_date) AS order_delivered_carrier_date,
        datetime(order_delivered_customer_date) AS order_delivered_customer_date,
        datetime(order_estimated_delivery_date) AS order_estimated_delivery_date
    FROM olist_orders_dataset
    WHERE order_id IS NOT NULL;
    """,

    # Clean order_items
    """
    DROP TABLE IF EXISTS clean_order_items;
    CREATE TABLE clean_order_items AS
    SELECT
        order_id,
        order_item_id,
        product_id,
        seller_id,
        price,
        freight_value
    FROM olist_order_items_dataset
    WHERE price > 0 AND freight_value >= 0;
    """,

    # Clean products
    """
    DROP TABLE IF EXISTS clean_products;
    CREATE TABLE clean_products AS
    SELECT DISTINCT
        product_id,
        product_category_name,
        product_weight_g,
        product_length_cm,
        product_height_cm,
        product_width_cm
    FROM olist_products_dataset;
    """,

    # Clean customers
    """
    DROP TABLE IF EXISTS clean_customers;
    CREATE TABLE clean_customers AS
    SELECT DISTINCT
        customer_id,
        customer_unique_id,
        customer_city,
        customer_state
    FROM olist_customers_dataset;
    """,

    # Clean sellers
    """
    DROP TABLE IF EXISTS clean_sellers;
    CREATE TABLE clean_sellers AS
    SELECT DISTINCT
        seller_id,
        seller_city,
        seller_state
    FROM olist_sellers_dataset;
    """,

    # Clean reviews
    """
    DROP TABLE IF EXISTS clean_reviews;
    CREATE TABLE clean_reviews AS
    SELECT
        review_id,
        order_id,
        review_score,
        datetime(review_creation_date) AS review_creation_date,
        datetime(review_answer_timestamp) AS review_answer_timestamp
    FROM olist_order_reviews_dataset
    WHERE review_score BETWEEN 1 AND 5;
    """,

    # Clean payments
    """
    DROP TABLE IF EXISTS clean_payments;
    CREATE TABLE clean_payments AS
    SELECT
        order_id,
        payment_sequential,
        payment_type,
        payment_installments,
        payment_value
    FROM olist_order_payments_dataset
    WHERE payment_value > 0;
    """
]

for q in queries:
    conn.executescript(q)

conn.commit()


tables = pd.read_sql(
    "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name", conn
)

conn.close()
