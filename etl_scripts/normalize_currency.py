import sqlite3

conn = sqlite3.connect("D:/project/etl-financial-risk/basel_demo.db")
cursor = conn.cursor()

currency_map = {
    "usd": "USD",
    "us dollars": "USD",
    "hkd": "HKD",
    "hk$": "HKD"
}

cursor.execute("SELECT Account_ID, Currency FROM Capital_Adequacy")
rows = cursor.fetchall()

with open("validation_report.txt", "w") as report:
    for account_id, currency in rows:
        original_currency = currency.strip()
        normalized_currency = currency_map.get(original_currency.lower(), original_currency)
        if original_currency.lower() != normalized_currency.lower():
            report.write(f"{account_id} - Currency normalized ({original_currency} → {normalized_currency})\n")

conn.close()
