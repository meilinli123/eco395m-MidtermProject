import os
import pandas as pd 
import requests
import json 

base_url = 'https://ridb.recreation.gov/api/v1/'
endpoint = 'facilities'
config_path = os.path.join("code", "config.json")
with open(config_path) as f:
    config = json.load(f)
api_key = config['api_key']
pnw_states = ["WA", "OR", "ID", "MT", "WY"]

"""scrape the api data from recreation.gov and sort out the variables we need: each individual facility id and their 
corresponding activities, along with their state codes."""

api_data = []
activity_data = []

for state in pnw_states:
    params = {'state': state, 'limit': 100, 'offset': 0} 
    response = requests.get(base_url+endpoint, params=params, headers={'apikey': api_key})
    response_json = response.json()
    
    facility_ids = []
    for key in response_json.get('RECDATA'):
        facility_ids.append(key.get('FacilityID'))
    api_data.append({'state': state, 'facility_ids': facility_ids})
    

for state_facility in api_data:
    for id in state_facility.get('facility_ids'):
        response = requests.get(f'{base_url}{endpoint}/{id}/activities', headers={'apikey': api_key})
        response_json = response.json().get('RECDATA')
        for key in response_json:
            activity_data.append({'state': state_facility.get('state'), 'facility_id': id, 'activity': key.get('ActivityName')})

    
