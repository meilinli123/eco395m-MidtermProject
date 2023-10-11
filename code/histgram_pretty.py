import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "sample_result.csv")
data = pd.read_csv(CSV_PATH)

activities_of_interest = ['CAMPING', 'FISHING', 'HIKING']
activity_colors = ['dodgerblue', 'limegreen', 'tomato']

unique_states = data['state'].unique()
x_positions = np.arange(len(unique_states))

plt.figure(figsize=(12, 8))
ax1 = plt.subplot(2, 1, 1)

for i, activity in enumerate(activities_of_interest):
    participation_rate = data[activity]
    ax1.bar(x_positions + i * 0.2 - 0.3, participation_rate, width=0.2, label=activity, color=activity_colors[i])

ax1.set_xlabel('State')
ax1.set_ylabel('Participation Rate')
ax1.set_title('Participation Rate of Activities by State')
ax1.set_xticks(x_positions - 0.2)
ax1.set_xticklabels(unique_states, rotation=45)  # Rotate state labels for better visibility

ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.5)  # Add grid lines with a dashed style and reduced opacity

ax2 = plt.subplot(2, 1, 2)

mortality_rate = data['Mortality']
ax2.bar(x_positions, mortality_rate, width=0.4, color='purple')

ax2.set_xlabel('State')
ax2.set_ylabel('Mortality Rate')
ax2.set_title('Mortality Rate by State')
ax2.set_xticks(x_positions)
ax2.set_xticklabels(unique_states, rotation=45)  # Rotate state labels for better visibility

ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig(os.path.join(BASE_DIR, "histogram2.png"))
plt.show()
