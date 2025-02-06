import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('D:/week 0 data/benin-malanville.csv')

correlation_matrix = df[['DHI', 'DNI']].corr()

# Plot the heatmap 
plt.figure(figsize=(10, 8)) 
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5) 
plt.title('Correlation Matrix Heatmap') 
plt.show()