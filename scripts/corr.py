import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

# Display the first few rows of the DataFrame
# print(df.head())

# Calculate the correlation matrix
correlation_matrix = df[['DHI', 'DNI']].corr()

# Display the correlation matrix
print("Correlation Matrix:")
print(correlation_matrix)
