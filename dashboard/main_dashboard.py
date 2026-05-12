import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("basel_ratios.csv")

# Add compliance flags
df['Compliance'] = df['Ratio'].apply(lambda x: 'Green' if x >= 100 else 'Red')

# Print table
print(df[['RatioName','Ratio','Compliance']])

# Plot bar chart
plt.bar(df['RatioName'], df['Ratio'],
        color=['green' if c == 'Green' else 'red' for c in df['Compliance']])
plt.axhline(y=100, color='black', linestyle='--', label='Threshold')
plt.legend()
plt.title("Basel III Ratios Dashboard")
plt.show()
