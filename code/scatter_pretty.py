import os
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "sample_result.csv")
data = pd.read_csv(CSV_PATH)

x = data['Mortality']
y_camping = data['CAMPING']
y_fishing = data['FISHING']
y_hiking = data['HIKING']

plt.figure(figsize=(10, 6))

plt.scatter(x, y_camping, label='Camping', color='dodgerblue', marker='o', s=60)
plt.scatter(x, y_fishing, label='Fishing', color='limegreen', marker='s', s=60)
plt.scatter(x, y_hiking, label='Hiking', color='tomato', marker='^', s=60)

plt.xlabel('Mortality')
plt.ylabel('Participation Rate')
plt.title('Scatter Plot of Mortality vs Participation Rates')

plt.legend(loc='best')
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhspan(0, max(y_camping, y_fishing, y_hiking), facecolor='lightgray')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['bottom'].set_linewidth(0.5)
plt.gca().spines['left'].set_linewidth(0.5)

plt.show()
