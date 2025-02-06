import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

# Display the first few rows of the DataFrame
print(df.head())

# Plot scatter plot of Temperature vs. Relative Humidity
plt.figure(figsize=(10, 6))
sns.scatterplot(x=df['RH'], y=df['Tamb'])
plt.title('Temperature vs. Relative Humidity')
plt.xlabel('Relative Humidity (%)')
plt.ylabel('Temperature (°C)')
plt.show()

