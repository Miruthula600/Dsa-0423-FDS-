import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample dataset
data = {
    'Customer_ID':[1,2,3,4,5,6,7,8],
    'Amount_Spent':[200,500,150,800,1200,300,700,1000],
    'Items_Purchased':[2,5,1,6,9,3,5,7]
}

df = pd.DataFrame(data)

# Selecting features
X = df[['Amount_Spent','Items_Purchased']]

# K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

print(df)

# Visualization
plt.scatter(df['Amount_Spent'], df['Items_Purchased'], c=df['Cluster'], cmap='viridis')
plt.xlabel("Amount Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation using K-Means")
plt.show()
