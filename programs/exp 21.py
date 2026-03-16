import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Sample dataset
data = {
    'weight':[150,170,140,130,160,180],
    'color':['red','orange','yellow','yellow','red','orange'],
    'texture':['smooth','rough','smooth','smooth','smooth','rough'],
    'type':['apple','orange','banana','banana','apple','orange']
}

df = pd.DataFrame(data)

# Convert categorical values to numeric
df['color'] = df['color'].map({'red':0,'orange':1,'yellow':2})
df['texture'] = df['texture'].map({'smooth':0,'rough':1})
df['type'] = df['type'].map({'apple':0,'orange':1,'banana':2})

# Features and target
X = df[['weight','color','texture']]
y = df['type']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# kNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

# Predict unknown fruit
prediction = model.predict([[155,0,0]])
print("Predicted Fruit Type:", prediction)
