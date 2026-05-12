import csv

with open("Basel_Test_Dataset.csv", "r") as infile, open("validation_report.txt", "w") as report:
    reader = csv.DictReader(infile)
    for row in reader:
        dataset_value = float(row["Ledger_Value"])
        calculated_value = float(row["CET1_Ratio"]) * 100  # example formula
        if abs(dataset_value - calculated_value) > 0.5:
            report.write(f"{row['Account_ID']} - Ledger_Value mismatch (Dataset: {dataset_value}, Calculated: {calculated_value})\n")
