###############This is to read in the recreational data

import requests as requests

import pip
import requests
import pandas as pd

#this comes from the https://ridb.recreation.gov/docs#/Activities/getActivities site -->under "Activities" --> first one under attributes

# Define the RIDB API endpoint and parameters
base_url = "https://ridb.recreation.gov/api/v1/"
endpoint = "facilities"
api_key = "4adb7c65-557b-483e-b06b-035223c1c5a2"  # Replace with your RIDB API key

# Define query parameters (modify as needed)
params = {
    "state": "",  # Initialize state as an empty string
    "limit": 1000,  # Limit the number of results
    "offset": 0,
}
# Setting limit to 100 means you will receive up to 100 facilities in each response from the API. If you expect there to be more facilities in each state and you want to retrieve more of them in each request, you can increase this number. However, be aware that very large values might result in slower responses, 1000 seems to take awhile
#The appropriate values for "limit" depend on your specific use case and the volume of data you expect to retrieve. If you're unsure about the number of facilities in each state, you can experiment with different values for "limit" to find an appropriate balance between the number of API requests and the amount of data retrieved in each request.


# Define the headers with your API key
headers = {
    "accept": "application/json",
    "apikey": api_key,
}

# Define list of PNW states
pnw_states = ["WA", "OR", "ID", "MT", "CA"]  # Pacific Northwest states - better to do a region because if were looking at activities, want those activities to be generally practised across the same range of states - popularoty in sports differs across states but I argue regions are similar

# Initialize an empty list to store the results
all_data = []

# Loop through each PNW state and make API requests
for state in pnw_states:
    # Update the state parameter in the query
    params["state"] = state

    # Make the API request
    response = requests.get(f"{base_url}{endpoint}", params=params, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        # Append the data for the current state to the result list
        all_data.append(data)
    else:
        print(f"Error for state {state}: {response.status_code}")

# Now 'all_data' contains a list of JSON responses for each PNW state
print(all_data)


################# this is the link to view the recreational data JSON<--

#json converter?

################# this is to read in the medical data

# Define the path to your CSV file
csv_file_path = "C:/Users/mache/OneDrive/Desktop/UTA/Py/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv"

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Display the first few rows of the DataFrame to verify the data
print(df.head())

# Display basic information about the DataFrame
print(df.info())

# Display summary statistics for numerical columns
print(df.describe())



#just look at the popular states - favorite 5 - and activities - fishing and
#count #facilties and #of fishing sites and / by population - faciltiy per capita
#1 branch - commit 5 times - after all commit thierstuff- look at code together and then merge - one one branch
#merge should be after the final review - wont do anything to commit - need to pull it after each meaningful commit
#put final code into main