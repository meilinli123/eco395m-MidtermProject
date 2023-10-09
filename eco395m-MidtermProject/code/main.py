import os
import pandas as pd


IN_PATH = os.path.join("data", "Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv")

if __name__ == "__main__":
    # df = pd.read_csv(IN_PATH)
    df = pd.read_csv('eco395m-MidtermProject/data/Heart_Disease_Mortality_Data_Among_US_Adults__35___by_State_Territory_and_County.csv')
    pnw_states = ["WA", "OR", "ID", "MT", "CA"]
    filtered_df = df[df['LocationAbbr'].isin(pnw_states)]
    # print(filtered_df)
    # unique_values = filtered_df['LocationID'].unique()
    # print(unique_values)