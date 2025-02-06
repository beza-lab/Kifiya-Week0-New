import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file into a DataFrame
df = pd.read_csv('D:/week 0 data/benin-malanville.csv')
# Set the figure size 
plt.figure(figsize=(15, 10)) 
# Create histogram for GHI 
plt.subplot(2, 3, 1) 
plt.hist(df['GHI'], bins=30, edgecolor='black') 
plt.title('Histogram of GHI') 
plt.xlabel('GHI') 
plt.ylabel
plt.tight_layout() 
plt.show()