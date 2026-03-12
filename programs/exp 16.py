from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X=[[45,120,200],[50,130,210],[30,110,180],[35,115,190]]
y=["Good","Bad","Good","Good"]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)

pred=model.predict(X_test)
print("Accuracy:",accuracy_score(y_test,pred))
