import pandas as pd

"""count the number of activities which we are interested in for each state, and normalized them by dividing the 
corresponding population; calculate the average heart disease mortality for each state."""

def calculate_counts_and_avgs(activity_data, mortality_data, state_populations):
   
    activity_df = pd.DataFrame(activity_data)

    activities_of_interest = ['CAMPING', 'FISHING', 'HIKING']

    counts = {state: {activity: 0 for activity in activities_of_interest} for state in state_populations}
    avg_mortality = {state: 0 for state in state_populations}

    for _, row in activity_df.iterrows():
        state = row['state']
        activity = row['activity']

        if activity in activities_of_interest:
            counts[state][activity] += 1

    for state in state_populations:
        total_mortality = mortality_data[mortality_data['LocationAbbr'] == state]['Data_Value'].mean()
        avg_mortality[state] = total_mortality

    for state in state_populations:
        population = state_populations[state]
        for activity in activities_of_interest:
            counts[state][activity] /= population

    result_df = pd.DataFrame({
        'state': list(state_populations.keys()),
        'CAMPING': [counts[state]['CAMPING'] for state in state_populations],
        'FISHING': [counts[state]['FISHING'] for state in state_populations],
        'HIKING': [counts[state]['HIKING'] for state in state_populations],
        'Mortality': [avg_mortality[state] for state in state_populations]
    })

    return result_df

