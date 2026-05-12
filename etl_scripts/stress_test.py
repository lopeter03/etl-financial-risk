import pandas as pd
import time

# Generate synthetic dataset
rows = 100000  # adjust to 100000 for FS15
data = {
    "Account_ID": [f"ACC{i}" for i in range(rows)],
    "CET1_Ratio": [4.5 + (i % 5) for i in range(rows)],
    "LCR": [90 + (i % 20) for i in range(rows)],
    "Capital_Ratio": [8 + (i % 3) for i in range(rows)],
    "Leverage": [4 + (i % 2) for i in range(rows)]
}
df = pd.DataFrame(data)

# Benchmark processing time
start = time.time()
df['Compliance'] = df['LCR'].apply(lambda x: 'Green' if x >= 100 else 'Red')
end = time.time()

print(f"Processed {rows} rows in {end-start:.2f} seconds")
