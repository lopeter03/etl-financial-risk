import sqlite3
import logging

# Configure logging
logging.basicConfig(
    filename="validation_report.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    conn = sqlite3.connect(r"D:\project\etl-financial-risk\basel_demo.db")
    cur = conn.cursor()

    # Valid bucket values
    valid_buckets = ['1','2','3','4','5']

    for row in cur.execute("SELECT Account_ID, Bucket FROM Capital_Adequacy"):
        acc, bucket = row

        if str(bucket) not in valid_buckets:
            logging.warning(f"{acc} - Misclassified bucket ({bucket}), corrected to 1")
            cur.execute("UPDATE Capital_Adequacy SET Bucket=? WHERE Account_ID=?", ('1', acc))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
