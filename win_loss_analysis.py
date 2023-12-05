import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
csv_file = 'Project001_Northgate_OFFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Visualize Total Yards Gained in Wins vs. Losses
plt.figure(figsize=(12, 6))

# Bar chart for Total Yards Gained in Wins
plt.subplot(1, 2, 1)
sns.barplot(x='Win/Loss', y='Total Yards Gained', data=df[df['Win/Loss'] == 'Win'], color='skyblue')
plt.title('Total Yards Gained in Wins')

# Bar chart for Total Yards Gained in Losses
plt.subplot(1, 2, 2)
sns.barplot(x='Win/Loss', y='Total Yards Gained', data=df[df['Win/Loss'] == 'Loss'], color='salmon')
plt.title('Total Yards Gained in Losses')

plt.tight_layout()
plt.show()

# Visualize Turnovers in Wins vs. Losses
plt.figure(figsize=(8, 6))

sns.countplot(x='Turnovers', hue='Win/Loss', data=df, palette='pastel')
plt.title('Turnovers in Wins vs. Losses')
plt.xlabel('Turnovers')
plt.ylabel('Count')

plt.show()
