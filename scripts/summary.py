import pandas as pd
import numpy as np

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

# Calculate the mean for a specific column (replace 'column_name' with your actual column name) 
# mean_value = df['column_name'].mean()

# Drop the Timestamp column 
#    df.drop(columns=['Timestamp'])


# Calculate summary statistics
summary_stats = df.describe().transpose()

# Rename '50%' to 'median'
summary_stats.rename(columns={'50%': 'median'}, inplace=True)
mean_values = summary_stats['mean'] 
#   print("Mean values of the columns:") 
print(mean_values)
#   print(summary_stats)
#df.drop(columns=['Timestamp'], inplace=True)

# mean_value = df.mean()
# print(mean_value)
# Save the cleaned data to a new CSV file
#   df.to_csv('mean_value')
#   mean_value.to_csv('mean value.csv', index=False)
# Additional calculations (e.g., median)
# summary_stats['median'] = df.median()