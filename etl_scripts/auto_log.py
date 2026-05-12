import sqlite3
from datetime import datetime

# Connect to the Basel demo database
conn = sqlite3.connect(r"D:\project\etl-financial-risk\basel_demo.db")
cur = conn.cursor()

# Open the audit trail file in append mode
with open("validation_report.txt", "a") as report:
    # Add a header with timestamp for traceability
    report.write(f"\n--- Auto Log Run at {datetime.now()} ---\n")

    # Iterate through all records
    for row in cur.execute("SELECT Account_ID, Capital_Ratio, CET1_Ratio, LCR, Bucket FROM Capital_Adequacy"):
        acc, cap, cet1, lcr, bucket = row

        # Convert numeric fields safely
        try:
            cap = float(cap) if cap is not None else None
            cet1 = float(cet1) if cet1 is not None else None
            lcr = float(lcr) if lcr is not None else None
        except ValueError:
            report.write(f"{acc} - Invalid numeric format\n")
            continue

        # Always log the record first
        report.write(f"{acc} - Record checked (CET1={cet1}, Cap={cap}, LCR={lcr}, Bucket={bucket})\n")

        # Apply validity rules
        if cet1 is not None and cet1 < 4.5:
            report.write(f"{acc} - CET1 below 4.5 ({cet1})\n")
        if cap is not None and cap < 8:
            report.write(f"{acc} - Capital Ratio below 8 ({cap})\n")
        if lcr is not None and lcr < 100:
            report.write(f"{acc} - LCR below 100 ({lcr})\n")
        if str(bucket) not in ['1','2','3','4','5']:
            report.write(f"{acc} - Invalid bucket ({bucket})\n")

conn.close()
