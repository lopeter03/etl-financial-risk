import sqlite3
import logging

# Configure logging to file
logging.basicConfig(
    filename="validation_report.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def safe_float(value, acc, field_name):
    """Try to convert to float, log error if corrupted."""
    try:
        return float(value) if value is not None else None
    except (ValueError, TypeError):
        logging.error(f"{acc} - Corrupted {field_name} value ({value})")
        return None

def main():
    conn = sqlite3.connect(r"D:\project\etl-financial-risk\basel_demo.db")
    cur = conn.cursor()

    for row in cur.execute("SELECT Account_ID, Capital_Ratio, CET1_Ratio, LCR, Bucket FROM Capital_Adequacy"):
        acc, cap, cet1, lcr, bucket = row

        # Convert safely with error handling
        cap = safe_float(cap, acc, "Capital_Ratio")
        cet1 = safe_float(cet1, acc, "CET1_Ratio")
        lcr = safe_float(lcr, acc, "LCR")

        # Skip record if corrupted values detected
        if cap is None or cet1 is None or lcr is None:
            logging.warning(f"{acc} - Record skipped due to corrupted values")
            continue

        # Apply validity rules
        if cet1 < 4.5:
            logging.info(f"{acc} - CET1 below 4.5 ({cet1})")
        if cap < 8:
            logging.info(f"{acc} - Capital Ratio below 8 ({cap})")
        if lcr < 100:
            logging.info(f"{acc} - LCR below 100 ({lcr})")
        if str(bucket) not in ['1','2','3','4','5']:
            logging.info(f"{acc} - Invalid bucket ({bucket})")

    conn.close()

if __name__ == "__main__":
    main()
