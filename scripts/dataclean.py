import pandas as pd
import numpy as np

# Read the CSV file into a DataFrame 

df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

 # Check for missing values 
#  missing_values = df.isnull().sum()

# Print the count of missing values in each column 
#   print("Missing values in each column:")
#   print(missing_values)

negative_values = (df['GHI'] < 0) | (df['DNI'] < 0) | (df['DHI'] < 0)
print("Negative values in each column:")
neg = df[negative_values]
print(neg)