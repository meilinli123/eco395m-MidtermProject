
import os
import pandas as pd
import requests
import json

IN_PATH = os.path.join("data", "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

if __name__ == "__main__":
    # df = pd.read_csv(IN_PATH)
    df = pd.read_csv('../data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "CA"]
    filtered_df = df[df['LocationAbbr'].isin(pnw_states)]
    # print(filtered_df)
    #
    # unique_values = filtered_df['LocationID'].unique()
    #
    # # Print the unique values
    # print(unique_values)

    base_url = 'https://ridb.recreation.gov/api/v1/'
    endpoint = 'facilities'
    api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'
    api_data = []
    for state in pnw_states:
        params = {'state': state, 'limit': 1, 'offset': 0}
        response = requests.get(base_url+endpoint, params=params, headers={'apikey': api_key})
        response_json = response.json()
        # print(json.dumps(response_json, indent=4))
        api_data.append({state: response_json})
        # print('*****************')
    print(api_data)

