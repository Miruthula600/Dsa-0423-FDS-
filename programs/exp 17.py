import pandas as pd
from sklearn.cluster import KMeans

# Sample dataset
data = {
    'Customer_ID':[1,2,3,4,5,6,7,8],
    'Amount_Spent':[200,500,150,800,1200,300,700,1000],
    'Visit_Frequency':[2,5,1,6,8,3,5,7]
}

df = pd.DataFrame(data)

# Selecting features
X = df[['Amount_Spent','Visit_Frequency']]

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X)

print(df)
