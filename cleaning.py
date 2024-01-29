import pandas as pd

# Load the dataset
file_path = "C://Users//Vaishnavi//Desktop//Covid-19//WHO-COVID-19-global-data.csv"  # Replace with the path to your dataset
covid_data = pd.read_csv(file_path)

# Cleaning steps:

# 1. Convert 'Date_reported' to datetime
covid_data['Date_reported'] = pd.to_datetime(covid_data['Date_reported'])

# 2. Fill missing values or drop rows/columns with missing values
# Filling missing values in 'New_cases' and 'New_deaths' with 0, 
# and dropping rows where 'Country_code' or 'Country' is missing.
covid_data['New_cases'].fillna(0, inplace=True)
covid_data['New_deaths'].fillna(0, inplace=True)
covid_data.dropna(subset=['Country_code', 'Country'], inplace=True)

# 3. Handle negative values in 'New_cases' and 'New_deaths'
# Assuming negative values are data entry errors and setting them to 0
covid_data['New_cases'] = covid_data['New_cases'].apply(lambda x: max(x, 0))
covid_data['New_deaths'] = covid_data['New_deaths'].apply(lambda x: max(x, 0))

# 4. Optionally convert 'New_cases' and 'New_deaths' to integers
covid_data['New_cases'] = covid_data['New_cases'].astype(int)
covid_data['New_deaths'] = covid_data['New_deaths'].astype(int)

# Save the cleaned dataset
covid_data.to_csv("C://Users//Vaishnavi//Desktop//Covid-19//cleaned.csv", index=False)