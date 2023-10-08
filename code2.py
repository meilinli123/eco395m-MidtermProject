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