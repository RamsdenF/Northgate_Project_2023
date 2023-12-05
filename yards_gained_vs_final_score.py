import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
csv_file = 'Project001_Northgate_OFFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Calculate Points Per Game
df['Points Per Game'] = df.apply(lambda row: int(row['Final Score'].split('-')[0]) if row['Win/Loss'] == 'Win' else int(row['Final Score'].split('-')[1]), axis=1)

# Visualize Total Yards Gained and Points Per Game
plt.figure(figsize=(12, 6))

# Bar chart for Total Yards Gained
plt.subplot(1, 2, 1)
sns.barplot(x='Opponent School', y='Total Yards Gained', data=df, palette='viridis')
plt.title('Total Yards Gained by Opponent')
plt.xticks(rotation=45, ha='right')

# Line chart for Points Per Game
plt.subplot(1, 2, 2)
sns.lineplot(x='Opponent School', y='Points Per Game', data=df, marker='o', color='orange')
plt.title('Points Per Game by Opponent')
plt.xticks(rotation=45, ha='right')

plt.tight_layout()
plt.show()


