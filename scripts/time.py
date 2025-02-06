import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame 
df = pd.read_csv('D:/week 0 data/benin-malanville.csv') 
# Display the first few rows of the DataFrame 



#    print(df.head())

plt.figure(figsize=(12, 6)) 
# df['GHI'].plot(kind='bar', label='GHI')
plt.plot(df['GHI'], label='GHI') 
plt.title('Time Series Plot') 
plt.xlabel('Date') 
plt.ylabel('GHI') 
plt.legend() 
plt.show()