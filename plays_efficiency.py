import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load offensive and defensive data
offense_df = pd.read_csv('Project001_Northgate_OFFSeasonData_22-23.csv')
defense_df = pd.read_csv('Project002_Northgate_DEFSeasonData_22-23.csv')

# Merge data on the 'Date' column
merged_df = pd.merge(offense_df, defense_df, on='Date', how='inner')

# Check the column names in the merged dataframe
print(merged_df.columns)

# If 'Opponent School' is not present, check for any differences in column names

# Calculate total plays per game for offense and defense
merged_df['Total Plays Per Game (Offense)'] = merged_df['Total OFF Plays Run']
merged_df['Total Plays Per Game (Defense)'] = merged_df['Total Plays Faced']

# Visualize total plays per game for offense and defense
plt.figure(figsize=(12, 6))

sns.lineplot(x='Opponent School_x', y='Total Plays Per Game (Offense)', data=merged_df, label='Offense', marker='o')
sns.lineplot(x='Opponent School_x', y='Total Plays Per Game (Defense)', data=merged_df, label='Defense', marker='o')

plt.title('Total Plays Per Game for Offense and Defense')
plt.xlabel('Opponent School')
plt.ylabel('Total Plays Per Game')
plt.xticks(rotation=45, ha='right')  # Adjust rotation for better readability
plt.legend()

plt.show()





