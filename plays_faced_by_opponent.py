import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
csv_file = 'Project002_Northgate_DEFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Visualize Total Plays Faced by Opponent
plt.figure(figsize=(12, 6))
sns.barplot(x='Opponent School', y='Total Plays Faced', data=df, palette='pastel')
plt.title('Total Plays Faced by Opponent')
plt.xlabel('Opponent School')
plt.ylabel('Total Plays Faced')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility

plt.tight_layout()
plt.show()
