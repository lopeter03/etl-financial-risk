import sqlite3

conn = sqlite3.connect("../basel_demo.db")  # note: parent folder
cursor = conn.cursor()

cursor.execute("INSERT INTO balance_sheet(asset, liability, equity) VALUES (1000000, 800000, 200000)")
cursor.execute("INSERT INTO rwa(exposure, risk_weight) VALUES (500000, 0.5)")
cursor.execute("INSERT INTO revenue_expense(category, amount, period) VALUES ('Revenue', 120000, '2026-01-01')")
cursor.execute("INSERT INTO revenue_expense(category, amount, period) VALUES ('Expense', 80000, '2026-01-01')")

conn.commit()
conn.close()
print("Sample data loaded successfully.")
