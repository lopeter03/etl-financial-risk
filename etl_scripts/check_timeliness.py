import sqlite3
from datetime import datetime

# Connect to your demo database
conn = sqlite3.connect("D:/project/etl-financial-risk/basel_demo.db")
cursor = conn.cursor()

# Define reporting cutoff (e.g., only records from 2026 onwards are valid)
cutoff_date = datetime.strptime("2026-01-01", "%Y-%m-%d")

# Fetch all records
cursor.execute("SELECT Account_ID, Date FROM Capital_Adequacy")
rows = cursor.fetchall()

# Write report
with open("validation_report.txt", "w") as report:
    for account_id, date_str in rows:
        try:
            record_date = datetime.strptime(date_str, "%Y-%m-%d")
            if record_date < cutoff_date:
                report.write(f"{account_id} - Outdated record ({date_str})\n")
        except Exception as e:
            report.write(f"{account_id} - Invalid date format ({date_str})\n")

conn.close()
