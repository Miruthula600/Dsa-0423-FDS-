import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Age':[25,30,35,40,28],
    'Income':[30000,40000,50000,60000,35000],
    'Spending':[200,300,400,500,250]
}

df = pd.DataFrame(data)

# Scatter plot
plt.scatter(df['Age'], df['Income'])
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Age vs Income")
plt.show()

# Scatter plot matrix
sns.pairplot(df)
plt.show()
