

import requests

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # ! replace with your own API
base_url = 'https://ridb.recreation.gov/api/v1/facilities'

# List of states you want to retrieve data for
states = ['WA', 'OR', 'ID', 'MT', 'WY']

headers = {
    'apikey': api_key
}

all_facility_data = []

for state in states:
    query_parameters = {
        'state': [state],
        'limit': 1000,  # Set the limit to the maximum (1000)
        'offset': 0,  # Start with offset 0
    }

    while True:
        # Make the API request with the query parameters
        response = requests.get(base_url, params=query_parameters, headers=headers)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            recdata = data.get('RECDATA', [])

            # Append the data to the result list with state information
            for facility in recdata:
                facility['state'] = state  # Add 'state' key with state name
                all_facility_data.append(facility)

            # Check if there are more results
            total_count = data['METADATA']['RESULTS']['TOTAL_COUNT']
            current_count = data['METADATA']['RESULTS']['CURRENT_COUNT']
            if current_count < total_count:
                # Increment the offset to fetch the next chunk
                query_parameters['offset'] += 1000
            else:
                # All data for the current state has been retrieved
                break
        else:
            print(f"Request failed with status code: {response.status_code}")
            break

# Now, all_facility_data contains all the facility information with state information


# In[124]:


all_facility_data

# In[127]:


# double check data
len(all_facility_data)

# In[130]:


# double check data
onestate = []
for dictionary in all_facility_data:
    for key, value in dictionary.items():
        if key == 'state' and value == 'WY':  # ['WA', 'OR', 'ID', 'MT', 'WY']
            onestate.append(dictionary)

# In[132]:


# double check data
len(onestate)

# 499 Washington
# 866 Oregon
# 817 Idaho
# 551 Montana
# 993 Wyoming


# ### data extraction

# In[133]:


keys_to_keep = ['FacilityID', 'state']

subset_facility = []
for entry in all_facility_data:
    subset_entry = {}
    for key in keys_to_keep:
        subset_entry[key] = entry[key]
    subset_facility.append(subset_entry)

# In[134]:


print(subset_facility)

# In[135]:


facID_list = []
for pair in subset_facility:
    facID_list.append(pair['FacilityID'])

# In[136]:


facID_list  # Finalized list of facility IDs

# In[137]:


len(facID_list)  # 3726

# ### 2. activities by list of facility IDs

# In[149]:


# need to request activities by state (or will take too long to load)
# NOTE: this could be streamlined into a function rather than specifying by state separately
# NOTE: keep in mind you don't need to import packages every code cell, but this isn't clean yet

# ['WA', 'OR', 'ID', 'MT', 'WY']

wa_facID = []
for dictionary in subset_facility:
    for key, val in dictionary.items():
        if key == 'state' and val == 'WA':
            wa_facID.append(dictionary['FacilityID'])

# In[150]:


or_facID = []
for dictionary in subset_facility:
    for key, val in dictionary.items():
        if key == 'state' and val == 'OR':
            or_facID.append(dictionary['FacilityID'])

# In[151]:


id_facID = []
for dictionary in subset_facility:
    for key, val in dictionary.items():
        if key == 'state' and val == 'ID':
            id_facID.append(dictionary['FacilityID'])

# In[152]:


mt_facID = []
for dictionary in subset_facility:
    for key, val in dictionary.items():
        if key == 'state' and val == 'MT':
            mt_facID.append(dictionary['FacilityID'])

# In[153]:


wy_facID = []
for dictionary in subset_facility:
    for key, val in dictionary.items():
        if key == 'state' and val == 'WY':
            wy_facID.append(dictionary['FacilityID'])

# ### washington activities

# In[144]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = wa_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

wa_activities = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/activities'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        wa_activities.append(data)

# In[147]:


# for dictionary in wa_activities:
#    print(dictionary["METADATA"]['RESULTS']['TOTAL_COUNT'])

# max activities is 22, so within 50 limit

wa_activities

# In[159]:


# Initialize an empty list to store the results
waID_act = []

# Loop through each dictionary in wa_activities:
for facility_data in wa_activities:
    recdata = facility_data.get('RECDATA', [])

    # Extract 'FacilityID' and 'ActivityName' from RECDATA
    for activity_entry in recdata:
        facility_id = activity_entry.get('FacilityID', None)
        activity_name = activity_entry.get('ActivityName', None)

        # Create a dictionary if both 'FacilityID' and 'ActivityName' are available
        if facility_id is not None and activity_name is not None:
            result_dict = {
                'FacilityID': facility_id,
                'ActivityName': activity_name
            }
            waID_act.append(result_dict)

# In[160]:


waID_act


# In[163]:


def combine_activities(activity_data):  # use this function multiple times
    result = {}
    for entry in activity_data:
        facility_id = entry['FacilityID']
        activity_name = entry['ActivityName']

        if facility_id not in result:
            result[facility_id] = []

        result[facility_id].append(activity_name)

    return result


# In[164]:


WAact_final = combine_activities(waID_act)

# In[167]:


WAact_final  # keep in mind that some facilities are not present because they don't have activities

# ### oregon activities

# In[148]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = or_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

or_activities = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/activities'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        or_activities.append(data)

# In[155]:


# for dictionary in or_activities:
#    print(dictionary["METADATA"]['RESULTS']['TOTAL_COUNT'])

# max activities is 26, so within 50 limit

len(or_activities)

# In[172]:


# Initialize an empty list to store the results
orID_act = []

# Loop through each dictionary in wa_activities:
for facility_data in or_activities:
    recdata = facility_data.get('RECDATA', [])

    # Extract 'FacilityID' and 'ActivityName' from RECDATA
    for activity_entry in recdata:
        facility_id = activity_entry.get('FacilityID', None)
        activity_name = activity_entry.get('ActivityName', None)

        # Create a dictionary if both 'FacilityID' and 'ActivityName' are available
        if facility_id is not None and activity_name is not None:
            result_dict = {
                'FacilityID': facility_id,
                'ActivityName': activity_name
            }
            orID_act.append(result_dict)

# In[173]:


orID_act

# In[174]:


ORact_final = combine_activities(orID_act)

# In[175]:


ORact_final

# ### idaho activities

# In[156]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = id_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

id_activities = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/activities'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        id_activities.append(data)

# In[158]:


# for dictionary in id_activities:
#    print(dictionary["METADATA"]['RESULTS']['TOTAL_COUNT'])

# max activities is 16, so within 50 limit

len(id_activities)

# In[176]:


# Initialize an empty list to store the results
idID_act = []

# Loop through each dictionary in wa_activities:
for facility_data in id_activities:
    recdata = facility_data.get('RECDATA', [])

    # Extract 'FacilityID' and 'ActivityName' from RECDATA
    for activity_entry in recdata:
        facility_id = activity_entry.get('FacilityID', None)
        activity_name = activity_entry.get('ActivityName', None)

        # Create a dictionary if both 'FacilityID' and 'ActivityName' are available
        if facility_id is not None and activity_name is not None:
            result_dict = {
                'FacilityID': facility_id,
                'ActivityName': activity_name
            }
            idID_act.append(result_dict)

# In[177]:


idID_act

# In[178]:


IDact_final = combine_activities(idID_act)

# In[179]:


IDact_final

# ### montana activities

# In[161]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = mt_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

mt_activities = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/activities'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        mt_activities.append(data)

# In[180]:


# for dictionary in mt_activities:
#    print(dictionary["METADATA"]['RESULTS']['TOTAL_COUNT'])

# max activities is 26, so within 50 limit

len(mt_activities)

# In[181]:


# Initialize an empty list to store the results
mtID_act = []

# Loop through each dictionary in wa_activities:
for facility_data in mt_activities:
    recdata = facility_data.get('RECDATA', [])

    # Extract 'FacilityID' and 'ActivityName' from RECDATA
    for activity_entry in recdata:
        facility_id = activity_entry.get('FacilityID', None)
        activity_name = activity_entry.get('ActivityName', None)

        # Create a dictionary if both 'FacilityID' and 'ActivityName' are available
        if facility_id is not None and activity_name is not None:
            result_dict = {
                'FacilityID': facility_id,
                'ActivityName': activity_name
            }
            mtID_act.append(result_dict)

# In[182]:


mtID_act

# In[183]:


MTact_final = combine_activities(mtID_act)

# In[184]:


MTact_final

# ### wyoming activities

# In[169]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = wy_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

wy_activities = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/activities'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        wy_activities.append(data)

# In[171]:


# for dictionary in wy_activities:
#    print(dictionary["METADATA"]['RESULTS']['TOTAL_COUNT'])

# max activities is 27, so within 50 limit

len(wy_activities)

# In[185]:


# Initialize an empty list to store the results
wyID_act = []

# Loop through each dictionary in wa_activities:
for facility_data in wy_activities:
    recdata = facility_data.get('RECDATA', [])

    # Extract 'FacilityID' and 'ActivityName' from RECDATA
    for activity_entry in recdata:
        facility_id = activity_entry.get('FacilityID', None)
        activity_name = activity_entry.get('ActivityName', None)

        # Create a dictionary if both 'FacilityID' and 'ActivityName' are available
        if facility_id is not None and activity_name is not None:
            result_dict = {
                'FacilityID': facility_id,
                'ActivityName': activity_name
            }
            wyID_act.append(result_dict)

# In[189]:


wyID_act

# In[187]:


WYact_final = combine_activities(wyID_act)

# In[190]:


WYact_final

# ### 3. location of facility (longitude and latitude)

# In[224]:


selected_fields = []
for entry in all_facility_data:
    selected_entry = {
        'FacilityID': entry['FacilityID'],
        'FacilityLatitude': entry['FacilityLatitude'],
        'FacilityLongitude': entry['FacilityLongitude'],
        'OrgFacilityID': entry['OrgFacilityID'],
        'ParentOrgID': entry['ParentOrgID'],
        'ParentRecAreaID': entry['ParentRecAreaID']
    }
    selected_fields.append(selected_entry)

# In[227]:


selected_fields

# ### zipcode...

# ### washington

# In[192]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = wa_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

WAloc_list = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/facilityaddresses'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        WAloc_list.append(data)

# In[193]:


WAloc_list  # zipcode


# In[216]:


def extract_address_info(data):
    address_info_list = []  # List to store dictionaries containing extracted information

    # Iterate through the data list
    for entry in data:
        # Extract relevant information from each entry
        recdata = entry.get('RECDATA', [])[0]  # Assuming there is only one entry in RECDATA

        address_state_code = recdata.get('AddressStateCode', 'N/A')
        facility_id = recdata.get('FacilityID', 'N/A')
        postal_code = recdata.get('PostalCode', 'N/A')

        # Create a dictionary for the extracted information and append it to the list
        address_info_list.append({
            'AddressStateCode': address_state_code,
            'FacilityID': facility_id,
            'PostalCode': postal_code
        })

    return address_info_list


# In[217]:


WAzipcode = extract_address_info(WAloc_list)

# In[248]:


WAzipcode

# ### oregon

# In[194]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = or_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

ORloc_list = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/facilityaddresses'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        ORloc_list.append(data)

# In[195]:


ORloc_list  # zipcode

# In[219]:


ORzipcode = extract_address_info(ORloc_list)

# ### idaho

# In[196]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = id_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

IDloc_list = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/facilityaddresses'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        IDloc_list.append(data)

# In[197]:


IDloc_list  # zipcode

# In[220]:


IDzipcode = extract_address_info(IDloc_list)

# In[251]:


len(IDzipcode)

# ### montana

# In[198]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = mt_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

MTloc_list = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/facilityaddresses'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        MTloc_list.append(data)

# In[199]:


MTloc_list  # zipcode

# In[221]:


MTzipcode = extract_address_info(MTloc_list)

# In[252]:


len(MTzipcode)

# ### wyoming

# In[201]:


import requests

base_url = 'https://ridb.recreation.gov/api/v1/facilities/'

facility_ids = wy_facID

api_key = '4adb7c65-557b-483e-b06b-035223c1c5a2'  # !

WYloc_list = []

# Loop through each facility ID and make an API request
for facility_id in facility_ids:
    url = f'{base_url}{facility_id}/facilityaddresses'

    headers = {
        'apikey': api_key
    }

    response = requests.get(url, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse and work with the response data for the current facility
        data = response.json()
        # Process and print the data as needed for this facility

        WYloc_list.append(data)

# In[202]:


WYloc_list  # zipcode

# In[223]:


WYzipcode = extract_address_info(WYloc_list)

# In[253]:


len(WYzipcode)

# ### 4. combine data

# In[ ]:


# summarize variables stored:

# subset_facility: list of dictionaries showing facility ID and state

# WAact_final: dictionary where key is facility ID and values are list of activities (keep in mind some facilities no activities )
# ORact_final
# IDact_final
# MTact_final
# WYact_final

# selected_fields: list of dictionaries showing facility ID, longitude, latitutde, and some other variables

# WAzipcode: list of dictionaries showing facility ID, postal code, and another variable
# ORzipcode
# IDzipcode
# MTzipcode
# WYzipcode


# In[256]:


ALL_activities = {**WAact_final, **ORact_final, **IDact_final, **MTact_final, **WYact_final}

# In[243]:


ALL_zipcodes = (WAzipcode + ORzipcode + IDzipcode + MTzipcode + WYzipcode)

# In[242]:


import pandas as pd

df1 = pd.DataFrame(subset_facility)

# In[254]:


df2 = pd.DataFrame(ALL_zipcodes)

# In[258]:


df3 = pd.DataFrame(ALL_activities.items(), columns=['FacilityID', 'Activities'])

# In[262]:


combdf1 = df1.merge(df2, on='FacilityID', how='left')  # facilityID, state, addressstatecode, postal code

# In[266]:


combdf2 = combdf1.merge(df3, on='FacilityID', how='left')

# In[269]:


df4 = pd.DataFrame(selected_fields)

# In[3]:


combdf3 = combdf2.merge(df4, on='FacilityID', how='left')

# In[2]:


combdf3

# In[274]:


# char_list = ['WA', 'OR', 'ID', 'MT', 'WY']
# filtered_combdf3 = combdf3[combdf3['AddressStateCode'].isin(char_list)]


# In[1]:

combdf3.to_csv('rec_dataset.csv', index=False)


# In[ ]:

# next steps, create a dictionary of types of activities
# next steps, create a dictionary of zipcodes to county
#then merge into one table
#then run alaysis and are good

