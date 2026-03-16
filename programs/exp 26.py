import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Temperature':[30,32,28,35,33,31,29],
    'Rainfall':[100,80,120,60,70,90,110]
}

df = pd.DataFrame(data)

# Correlation
corr = df['Temperature'].corr(df['Rainfall'])
print("Correlation Coefficient:", corr)

# Scatter plot
plt.scatter(df['Temperature'], df['Rainfall'])
plt.xlabel("Temperature")
plt.ylabel("Rainfall")
plt.title("Temperature vs Rainfall")
plt.show()
