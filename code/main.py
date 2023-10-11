import os
import pandas as pd
import requests
import json
import csv
from decouple import config

BASE_DIR = "data"
CSV_PATH = os.path.join(BASE_DIR, "facilities.csv")
os.makedirs(BASE_DIR, exist_ok=True)
IN_PATH = os.path.join(BASE_DIR, "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

if __name__ == "__main__":
    # df = pd.read_csv(IN_PATH)
    df = pd.read_csv('data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "WY"]
    filtered_df = df[(df['LocationAbbr'].isin(pnw_states) & (df['GeographicLevel'] == 'State'))]

    # unique_values = filtered_df['LocationID'].unique()
    # print(unique_values)

    base_url = 'https://ridb.recreation.gov/api/v1/'
    endpoint = 'facilities'

    # Read the API key from the .env file
    api_key = config('api_key')
    # Use the API key in your code
    print(f"api_key: {api_key}")

    api_data = []
    for state in pnw_states:
        params = {'state': state, 'limit': 10, 'offset': 0} #set limit to 2
        response = requests.get(base_url+endpoint, params=params, headers={'apikey': api_key})
        response_json = response.json()
        # print(json.dumps(response_json, indent=4))
        facility_ids = []
        for key in response_json.get('RECDATA'):
            facility_ids.append(key.get('FacilityID'))
        api_data.append({'state': state, 'facility_ids': facility_ids})
    # print(api_data)

    activity_data = []
    for state_facility in api_data:
        for id in state_facility.get('facility_ids'):
            response = requests.get(f'{base_url}{endpoint}/{id}/activities', headers={'apikey': api_key})
            response_json = response.json().get('RECDATA')
            for key in response_json:
                activity_data.append({'state': state_facility.get('state'), 'facility_id': id, 'activity': key.get('ActivityName')})
    # print(activity_data)

    df_api = pd.DataFrame(activity_data)
    merged_df = pd.merge(filtered_df, df_api, left_on='LocationAbbr', right_on='state')
    print(merged_df)

    data = merged_df
    path = CSV_PATH
def write_data_to_csv(data, path):
    """Write the data to the CSV file.
    """
    with open(path, 'w', newline='') as csvfile:
        fieldnames = ["state", "facility_id", "activity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for index, row in data.iterrows():
            writer.writerow({
                "state": row["state"],
                "facility_id": row["facility_id"],
                "activity": row["activity"],
            })
write_data_to_csv(merged_df, CSV_PATH)
