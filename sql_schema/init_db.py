import sqlite3

conn = sqlite3.connect("../basel_demo.db")  # note: parent folder
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS balance_sheet (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    asset REAL,
    liability REAL,
    equity REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS rwa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    exposure REAL,
    risk_weight REAL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS revenue_expense (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    amount REAL,
    period DATE
);
""")

conn.commit()
conn.close()
print("Database initialized successfully.")
