import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Sample dataset
data = {
    'income':[30000,50000,40000,60000,35000,70000],
    'credit_score':[600,750,680,800,650,820],
    'debt_ratio':[0.4,0.2,0.3,0.1,0.35,0.15],
    'employment_years':[2,5,3,8,4,10],
    'risk':['High','Low','High','Low','High','Low']
}

df = pd.DataFrame(data)

# Convert target to numeric
df['risk'] = df['risk'].map({'High':1,'Low':0})

# Features and target
X = df[['income','credit_score','debt_ratio','employment_years']]
y = df['risk']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# CART model
model = DecisionTreeClassifier()
model.fit(X_train,y_train)

# Prediction for new applicant
prediction = model.predict([[45000,700,0.25,4]])

print("Predicted Credit Risk:", prediction)
