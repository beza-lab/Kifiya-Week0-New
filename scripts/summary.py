import pandas as pd

# Load the CSV
df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

# Calculate summary
summary_stats = df.describe()

summary_stats.to_csv('summarydata.csv', index=False)

print("Summary data saved to summarydata.csv")


print(summary_stats)