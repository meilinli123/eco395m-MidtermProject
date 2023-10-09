import os
import pandas as pd
import requests
import json
import geopy
from geopy.geocoders import Nominatim, Photon

#pt 1. to get state info based on longitude and Latitude from the rec website:

import requests

def get_country(lat, lon):
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en&zoom=5'
    try:
        result = requests.get(url=url)
        result_json = result.json()
        return result_json['display_name']
    except:
        return None


#pt 2. ingest Heart Disease Data

IN_PATH = os.path.join("data", "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

if __name__ == "__main__":
    # df = pd.read_csv(IN_PATH)
    df = pd.read_csv('../data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "CA"]
    filtered_df = df[df['LocationAbbr'].isin(pnw_states)]
    # print(filtered_df)
    # unique_values = filtered_df['LocationID'].unique()
    # print(unique_values)

#pt3. ingest recreational data

    base_url = 'https://ridb.recreation.gov/api/v1/'
    endpoint = 'facilities'
    api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'
    params = {'state': pnw_states, 'limit': 5, 'offset': 0}
    response = requests.get(base_url+endpoint, params=params, headers={'apikey': api_key})
    response_json = response.json()
    df_recdata = pd.DataFrame(response_json["RECDATA"])

    print(df_recdata.columns)
    print(df_recdata["GEOJSON"][2])
    #print(response_json["METADATA"]["RESULTS"]["CURRENT_COUNT"])
    #print(json.dumps(response_json, indent=4)["METADATA"]["RESULTS"]["CURRENT_COUNT"])

    print(get_country(33,-96)) #this is just an example I entered - it prints Texas, US


#pt 4. create new col - states based on long and lat - merge two data frames on like col


def get_state(location):
    lat, lon = map(float, location.strip('()').split(', '))
    url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&accept-language=en&zoom=5'
    try:
        result = requests.get(url=url)
        result_json = result.json()
        address = result_json.get('address', {})
        state = address.get('state', None)
        return state
    except:
        return None

#Applying the get_state function to create a 'State' column in both dataframes
df['State'] = df['Location 1'].apply(lambda location: get_state(location))
df_recdata['State'] = df_recdata.apply(lambda row: get_state(row['FacilityLatitude'], row['FacilityLongitude']), axis=1)

# Now that both dataframes have a 'State' column based on latitude and longitude Merge the two dataframes based on 'State' column
merged_df = pd.merge(df, df_recdata, on='State', how='inner')

print(merged_df.head())
merged_df.to_csv('merged_data.csv', index=False)