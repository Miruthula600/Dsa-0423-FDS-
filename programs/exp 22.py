import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Sample dataset
data = {
    'age':[25,30,35,40,28,32],
    'income':[30000,40000,50000,60000,35000,45000],
    'browsing_duration':[5,10,8,15,6,12],
    'device_type':['mobile','desktop','mobile','desktop','mobile','desktop'],
    'purchase':['No','Yes','Yes','Yes','No','Yes']
}

df = pd.DataFrame(data)

# Convert categorical values
df['device_type'] = df['device_type'].map({'mobile':0,'desktop':1})
df['purchase'] = df['purchase'].map({'No':0,'Yes':1})

# Features and target
X = df[['age','income','browsing_duration','device_type']]
y = df['purchase']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# Decision Tree model
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Predict new customer
prediction = model.predict([[29,38000,7,0]])

print("Will the customer purchase? :", prediction)
