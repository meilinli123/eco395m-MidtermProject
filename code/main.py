import os
import pandas as pd
import csv
from activity_sorting import activity_data

BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "facilities.csv")
os.makedirs(BASE_DIR, exist_ok=True)
IN_PATH = os.path.join(BASE_DIR, "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

def write_data_to_csv(data, path):

    """Write the data to the CSV file."""

    with open(path, 'w', newline='') as csvfile:
        fieldnames = ["LocationAbbr", "Topic", "Data_Value", "Data_Value_Unit", "state", "facility_id", "activity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in data.iterrows():
            writer.writerow({
                "LocationAbbr": row["LocationAbbr"],
                "Topic": row["Topic"],
                "Data_Value": row["Data_Value"],
                "Data_Value_Unit": row["Data_Value_Unit"],
                "state": row["state"],
                "facility_id": row["facility_id"],
                "activity": row["activity"],
            })

if __name__ == "__main__":
    
    df = pd.read_csv('data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "WY"]
    filtered_df = df[(df['LocationAbbr'].isin(pnw_states) & (df['GeographicLevel'] == 'State'))]
    filtered_df.dropna(subset=['Data_Value'], inplace=True)

    data = activity_data
    path = CSV_PATH
    df_api = pd.DataFrame(data)
    
    merged_df = pd.merge(filtered_df, df_api, left_on='LocationAbbr', right_on='state')
    print(merged_df)

    write_data_to_csv(merged_df, CSV_PATH)