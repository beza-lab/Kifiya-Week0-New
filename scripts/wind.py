import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load your wind data from a CSV file (use sample data if not available)
try:
    df = pd.read_csv('D:/week 0 data/benin-malanville.csv')
    wind_speed = df['WS'].values
    wind_direction = df['WD'].values
except FileNotFoundError:
    np.random.seed(0)
    wind_speed = np.random.uniform(low=0, high=15, size=50)  # Wind speed in m/s
    wind_direction = np.random.uniform(low=0, high=360, size=50)  # Wind direction in degrees

# Create the radial bar plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, polar=True)

# Convert wind direction to radians
wind_direction_rad = np.deg2rad(wind_direction)

# Create bars for wind speed
bars = ax.bar(wind_direction_rad, wind_speed, width=np.deg2rad(10), bottom=0.0, color='blue', alpha=0.6)

# Set plot parameters
ax.set_theta_direction(-1)
ax.set_theta_offset(np.pi / 2.0)
ax.set_rlabel_position(180 / np.pi)

# Title and display
plt.title('Wind Analysis using Radial Bar Plot')
plt.show()
