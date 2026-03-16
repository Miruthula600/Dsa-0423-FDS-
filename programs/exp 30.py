import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("shoe_sales.csv")

# Frequency distribution
freq = df.groupby('shoe_size')['quantity'].sum()

print("Frequency Distribution:\n", freq)

# Bar chart
freq.plot(kind='bar')
plt.title("Shoe Size Distribution")
plt.xlabel("Shoe Size")
plt.ylabel("Quantity Sold")
plt.show()
