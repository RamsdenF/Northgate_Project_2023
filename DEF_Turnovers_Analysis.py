import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
csv_file = 'Project002_Northgate_DEFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Visualize Turnovers Forced in Wins vs. Losses
plt.figure(figsize=(8, 6))

sns.countplot(x='Turnovers Forced', hue='Win/Loss', data=df, palette='pastel')
plt.title('Turnovers Forced in Wins vs. Losses')
plt.xlabel('Turnovers Forced')
plt.ylabel('Count')

plt.show()
