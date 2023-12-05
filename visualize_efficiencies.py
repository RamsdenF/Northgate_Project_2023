import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from the CSV file
csv_file = 'Project001_Northgate_OFFSeasonData_22-23.csv'
df = pd.read_csv(csv_file)

# Visualize 3rd Down Efficiency in Wins vs. Losses
plt.figure(figsize=(12, 6))

# Bar chart for 3rd Down Efficiency in Wins
plt.subplot(1, 2, 1)
sns.barplot(x='Win/Loss', y='3rd Down Efficiency', data=df, palette='coolwarm')
plt.title('3rd Down Efficiency in Wins')

# Bar chart for 3rd Down Efficiency in Losses
plt.subplot(1, 2, 2)
sns.barplot(x='Win/Loss', y='3rd Down Efficiency', data=df[df['Win/Loss'] == 'Loss'], palette='coolwarm')
plt.title('3rd Down Efficiency in Losses')

plt.tight_layout()
plt.show()

# Visualize 4th Down Efficiency in Wins vs. Losses
plt.figure(figsize=(12, 6))

# Bar chart for 4th Down Efficiency in Wins
plt.subplot(1, 2, 1)
sns.barplot(x='Win/Loss', y='4th Down Efficiency', data=df, palette='viridis')
plt.title('4th Down Efficiency in Wins')

# Bar chart for 4th Down Efficiency in Losses
plt.subplot(1, 2, 2)
sns.barplot(x='Win/Loss', y='4th Down Efficiency', data=df[df['Win/Loss'] == 'Loss'], palette='viridis')
plt.title('4th Down Efficiency in Losses')

plt.tight_layout()
plt.show()

# Visualize 1st Downs Gained in Wins vs. Losses
plt.figure(figsize=(12, 6))

# Bar chart for 1st Downs Gained in Wins
plt.subplot(1, 2, 1)
sns.barplot(x='Win/Loss', y='First Downs Acquired', data=df, palette='pastel')
plt.title('1st Downs Gained in Wins')

# Bar chart for 1st Downs Gained in Losses
plt.subplot(1, 2, 2)
sns.barplot(x='Win/Loss', y='First Downs Acquired', data=df[df['Win/Loss'] == 'Loss'], palette='pastel')
plt.title('1st Downs Gained in Losses')

plt.tight_layout()
plt.show()
