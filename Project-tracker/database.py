# database.py
import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT,
            price REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_price(product_name, price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO price_history (product_name, price) VALUES (?, ?)",
        (product_name, price)
    )
    conn.commit()
    conn.close()
    print(f"[DB] Saved: {product_name} → ₹{price}")

def get_price_history(product_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT price, timestamp FROM price_history WHERE product_name = ? ORDER BY timestamp",
        (product_name,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows