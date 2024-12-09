import pandas as pd
import numpy as np

df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

# Check for negative values
columns_to_check = ['GHI', 'DNI', 'DHI', 'ModA', 'ModB', 'WS', 'WSgust']

# Fill missing values using median
for column in columns_to_check:
    df[column].fillna(df[column].median())

#  Incorrect entries (negative values in GHI, DNI, DHI) by removing those rows
incorrect_entries = (df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)
df = df[~incorrect_entries]

# Save the cleaned data to a new CSV file
df.to_csv('clean_data.csv', index=False)

print("Cleaned data saved to cleaned_data.csv")
