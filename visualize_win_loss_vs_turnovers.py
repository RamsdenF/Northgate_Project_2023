import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
csv_file = 'Project001_Northgate_OFFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Visualize Win/Loss Outcome vs. Turnovers
plt.figure(figsize=(8, 6))

sns.countplot(x='Win/Loss', hue='Turnovers', data=df, palette='pastel')
plt.title('Win/Loss Outcome vs. Turnovers')
plt.xlabel('Win/Loss')
plt.ylabel('Count')

plt.show()
