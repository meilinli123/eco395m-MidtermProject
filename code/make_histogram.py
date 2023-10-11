import os
import pandas as pd
import csv
import matplotlib.pyplot as plt
import numpy as np
from activity_sorting import activity_data
from data_reform_test import calculate_counts_and_avgs



BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "sample_result.csv")
os.makedirs(BASE_DIR, exist_ok=True)
IN_PATH = os.path.join(BASE_DIR, "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")
OUT_PATH = os.path.join(BASE_DIR, "histogram.png")

def make_histogram():
    de = pd.read_csv(CSV_PATH)
    data1 = de['CAMPING']
    data2 = de['FISHING']
    data3 = de['HIKING']
    data4 = de['Mortality']

    num_clusters = len(data1)
    cluster_width = 0.2

    x = np.arange(num_clusters)

    plt.bar(x - 1.5 * cluster_width, data1, width=cluster_width, label='CAMPING', color='blue')
    plt.bar(x - 0.5 * cluster_width, data2, width=cluster_width, label='FISHING', color='green')
    plt.bar(x + 0.5 * cluster_width, data3, width=cluster_width, label='HIKING', color='red')
    plt.bar(x + 1.5 * cluster_width, data4, width=cluster_width, label='Mortality', color='purple')

    x_labels = ['ID', 'MT', 'OR', 'WA', 'WY']
    plt.xticks(x, x_labels)

    plt.legend()

    # Add labels and title
    plt.title('Heart disease and outdoor activities')
    plt.xlabel('states')
    plt.ylabel('outdoor activities')

    # Show or save the chart
    plt.show()
    plt.savefig(OUT_PATH, format='png')

make_histogram()

if __name__ == "__main__":

    df = pd.read_csv('data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "WY"]
    filtered_df = df[(df['LocationAbbr'].isin(pnw_states) & (df['GeographicLevel'] == 'State'))]
    filtered_df.dropna(subset=['Data_Value'], inplace=True)

    state_population = {"ID": 1.939033,
                    "MT": 1.122867,
                    "OR": 4.240137,
                    "WA": 7.785786,
                    "WY": 0.581381}

    result_df = calculate_counts_and_avgs(activity_data, filtered_df, state_population)
    print(result_df)
    df_api = pd.DataFrame(result_df)

    df_api.to_csv(CSV_PATH, index=False)
