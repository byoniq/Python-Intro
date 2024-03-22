import pandas as pd
import json
import matplotlib.pyplot as plt

with open ('D:\Advanced Python\data.json') as f:
    data = json.load(f)
    df = pd.DataFrame(data)

 # Filter out rows with missing or NaN values
df_filtered = df.dropna(subset=['Country', 'Area_km2'])

# Sort the data by area in descending order
df_filtered = df_filtered.sort_values(by='Area_km2', ascending=False)

# Filter countries with area between 50,000 and 100,000 km2
df_filtered = df_filtered[(df_filtered['Area_km2'] >= 50000) & (df_filtered['Area_km2'] <= 100000)]

# Create a figure with a custom size
fig, ax = plt.subplots(figsize=(10, 6))

# Plot a horizontal bar chart
ax.barh(df_filtered['Country'], df_filtered['Area_km2'], color='skyblue')

# Set labels and title
ax.set_xlabel('Area (km²)', fontsize=12)
ax.set_ylabel('Country', fontsize=12)
ax.set_title('Countries with Area between 50,000 and 100,000 km²', fontsize=14)

# Rotate the y-axis labels for better visibility
plt.subplots_adjust(left=0.3)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Add grid and display the plot
ax.grid(axis='x', linestyle='--')
plt.tight_layout()
plt.show()