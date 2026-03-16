import pandas as pd
import matplotlib.pyplot as plt

# Read CSV file
df = pd.read_csv("players.csv")

# Top 5 players with highest goals
top_goals = df.sort_values(by="Goals", ascending=False).head(5)
print("Top 5 Goal Scorers:\n", top_goals[['Name','Goals']])

# Top 5 highest salaries
top_salary = df.sort_values(by="Salary", ascending=False).head(5)
print("\nTop 5 Highest Salaries:\n", top_salary[['Name','Salary']])

# Average age
avg_age = df['Age'].mean()
print("\nAverage Age:", avg_age)

# Players above average age
above_avg = df[df['Age'] > avg_age]
print("\nPlayers Above Average Age:\n", above_avg[['Name','Age']])

# Position distribution
position_counts = df['Position'].value_counts()

# Bar chart
position_counts.plot(kind='bar')
plt.title("Distribution of Players by Position")
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.show()
