import sqlite3
import csv
import logging

# Configure logging
logging.basicConfig(
    filename="validation_report.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_reference_dataset(path):
    """Load sample dataset into a dictionary keyed by Account_ID."""
    reference = {}
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            reference[row['Account_ID']] = row
    return reference

def main():
    # Connect to ETL database
    conn = sqlite3.connect(r"D:\project\etl-financial-risk\basel_demo.db")
    cur = conn.cursor()

    # Load sample dataset (CSV file)
    reference = load_reference_dataset(r"D:\project\etl-financial-risk\etl_scripts\Basel_Test_Dataset.csv")


    # Compare each record in Capital_Adequacy against reference dataset
    for row in cur.execute("SELECT Account_ID, Capital_Ratio, CET1_Ratio, LCR, Bucket FROM Capital_Adequacy"):
        acc, cap, cet1, lcr, bucket = row

        if acc in reference:
            ref = reference[acc]

            # Compare values
            mismatches = []
            if str(cap) != ref['Capital_Ratio']:
                mismatches.append(f"Capital_Ratio mismatch ({cap} vs {ref['Capital_Ratio']})")
            if str(cet1) != ref['CET1_Ratio']:
                mismatches.append(f"CET1_Ratio mismatch ({cet1} vs {ref['CET1_Ratio']})")
            if str(lcr) != ref['LCR']:
                mismatches.append(f"LCR mismatch ({lcr} vs {ref['LCR']})")
            if str(bucket) != ref['Bucket']:
                mismatches.append(f"Bucket mismatch ({bucket} vs {ref['Bucket']})")

            # Log mismatches
            if mismatches:
                logging.warning(f"{acc} - Deviations found: {', '.join(mismatches)}")
            else:
                logging.info(f"{acc} - Record reconciled successfully")

        else:
            logging.error(f"{acc} - Not found in reference dataset")

    conn.close()

if __name__ == "__main__":
    main()
