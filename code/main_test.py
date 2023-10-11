import os
import pandas as pd
import csv
from sorting_copy import activity_data
from data_reform import calculate_counts_and_avgs

BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "sample_result.csv")
os.makedirs(BASE_DIR, exist_ok=True)
IN_PATH = os.path.join(BASE_DIR, "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

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
    