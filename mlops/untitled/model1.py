from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd


##load dataset
iris=load_iris()
X=iris.data
y=iris.target
##split data
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=42,test_size=0.5)
##bulild model
clf=RandomForestClassifier(n_estimators=10)
clf.fit(X_train,y_train)
##test
predicted=clf.predict(X_test)
###check accuracy
print(accuracy_score(predicted,y_test))


###Pickle : a python object can be stored as binary file so that we can load it later
import pickle
with open('/home/harsh/PycharmProjects/untitled/rf.pkl','wb') as model_pkl:
    pickle.dump(clf,model_pkl  )



