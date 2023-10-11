
import os
import pandas as pd
import requests
import json

IN_PATH = os.path.join("data", "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

if __name__ == "__main__":
    df = pd.read_csv(IN_PATH)
    #df = pd.read_csv('../data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "WY"]
    filtered_df = df[(df['LocationAbbr'].isin(pnw_states) & (df['GeographicLevel'] == 'State'))]

    # unique_values = filtered_df['LocationID'].unique()
    # print(unique_values)

    base_url = 'https://ridb.recreation.gov/api/v1/'
    endpoint = 'facilities'
    api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'
    api_data = []
    for state in pnw_states:
        params = {'state': state, 'limit': 1000, 'offset': 0} #set limit to 2
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
