import pandas as pd

# Load data from the CSV file
csv_file = 'Project001_Northgate_OFFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Display the first few rows to check if the data loaded correctly
print(df.head())

# Perform additional analysis as needed
# For example, you can calculate the average Total Yards Gained
average_yards = df['Total Yards Gained'].mean()
print(f'Average Total Yards Gained: {average_yards} yards')
