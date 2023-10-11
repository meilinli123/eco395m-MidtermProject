import os
import pandas as pd
import requests
import json

# Define input path for the CSV file containing heart disease mortality data
IN_PATH = os.path.join('eco395m-MidtermProject', 'data', 'Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')

def fetch_ridb_facility_data(states, api_key):
    base_url = 'https://ridb.recreation.gov/api/v1/'
    endpoint = 'facilities'
    
    api_data = []

    for state in states:
        try:
            # Set up parameters for the API request
            params = {'state': state, 'limit': 1000, 'offset': 0}
            response = requests.get(base_url + endpoint, params=params, headers={'apikey': api_key})

            if response.status_code == 200:
                response_json = response.json()
                facility_ids = [entry.get('FacilityID') for entry in response_json.get('RECDATA')]
                api_data.append({'state': state, 'facility_ids': facility_ids})
            else:
                print(f"Failed to fetch data for state {state}. Status Code: {response.status_code}")
        except Exception as e:
            print(f"An error occurred while fetching data for state {state}: {str(e)}")

    return api_data

def fetch_ridb_activity_data(api_data, api_key):
    base_url = 'https://ridb.recreation.gov/api/v1/'
    endpoint = 'facilities'

    activity_data = []

    for state_facility in api_data:
        for facility_id in state_facility.get('facility_ids'):
            try:
                response = requests.get(f'{base_url}{endpoint}/{facility_id}/activities', headers={'apikey': api_key})

                if response.status_code == 200:
                    response_json = response.json().get('RECDATA')
                    for entry in response_json:
                        activity_data.append({'state': state_facility.get('state'), 'facility_id': facility_id, 'activity': entry.get('ActivityName')})
                else:
                    print(f"Failed to fetch activity data for facility {facility_id}. Status Code: {response.status_code}")
            except Exception as e:
                print(f"An error occurred while fetching activity data for facility {facility_id}: {str(e)}")

    return activity_data

if __name__ == "__main__":
    try:
        # Read the heart disease mortality data from the CSV file
        df = pd.read_csv(IN_PATH)

        # Define the Pacific Northwest (PNW) states
        pnw_states = ["WA", "OR", "ID", "MT", "WY"]

        # Filter the heart disease data for PNW states and state level
        filtered_df = df[(df['LocationAbbr'].isin(pnw_states) & (df['GeographicLevel'] == 'State'))]

        # Define RIDB API key
        api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'

        # Fetch facility data from RIDB API
        api_data = fetch_ridb_facility_data(pnw_states, api_key)

        # Fetch activity data from RIDB API
        activity_data = fetch_ridb_activity_data(api_data, api_key)

        # Create a DataFrame from the activity data
        df_api = pd.DataFrame(activity_data)

        # Merge the filtered heart disease data with facility activity data
        merged_df = pd.merge(filtered_df, df_api, left_on='LocationAbbr', right_on='state')

        # Print the merged DataFrame
        print(merged_df)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

