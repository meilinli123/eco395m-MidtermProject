import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "sample_result.csv")
data = pd.read_csv(CSV_PATH)

# Define a color map for each state
states = data['state'].unique()
num_states = len(states)
colors = plt.cm.rainbow(np.linspace(0, 1, num_states))

# Create a dictionary to map states to colors
state_color_map = {state: color for state, color in zip(states, colors)}

# Extract the relevant columns for the scatter plot
x = data['Mortality']
y_camping = data['CAMPING']  
y_fishing = data['FISHING']  
y_hiking = data['HIKING']  

# Create the scatter plot
plt.figure(figsize=(10, 6))

# Scatter plot for each state with unique color
for state in states:
    indices = data['state'] == state
    plt.scatter(x[indices], y_camping[indices], label=f'Camping - {state}', color=state_color_map[state])
    plt.scatter(x[indices], y_fishing[indices], label=f'Fishing - {state}', color=state_color_map[state])
    plt.scatter(x[indices], y_hiking[indices], label=f'Hiking - {state}', color=state_color_map[state])

plt.xlabel('Mortality')
plt.ylabel('Participation Rate')
plt.title('Scatter Plot of Mortality vs Participation Rates (by State)')
plt.legend()
plt.grid(True)

OUT_PATH = os.path.join(BASE_DIR, "scatter_plot.png")

plt.savefig(OUT_PATH, format='png')

plt.show()
