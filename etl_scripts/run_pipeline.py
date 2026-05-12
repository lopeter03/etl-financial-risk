import sqlite3
import pandas as pd

conn = sqlite3.connect("../basel_demo.db")  # parent folder

balance = pd.read_sql("SELECT * FROM balance_sheet", conn)
rwa = pd.read_sql("SELECT * FROM rwa", conn)
revexp = pd.read_sql("SELECT * FROM revenue_expense", conn)

print("Balance Sheet:\n", balance)
print("RWA:\n", rwa)
print("Revenue/Expense:\n", revexp)

conn.close()
