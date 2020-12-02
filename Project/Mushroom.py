import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("mushrooms.csv")
X=df.drop(columns="class")
y=df["class"]

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
## X variable label Encoder
lex=LabelEncoder()
for i in X:
    X[i]=lex.fit_transform(X[i])

## y label Encoder
ley=LabelEncoder()
y=ley.fit_transform(y)

X=pd.get_dummies(X,columns=X.columns,drop_first=True)
from sklearn.model_selection import train_test_split, GridSearchCV
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.25)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
xtrain = sc.fit_transform(xtrain)
xtest = sc.transform(xtest)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
xtrain = pca.fit_transform(xtrain)
xtest = pca.transform(xtest)



print("Decision Tree algorithm:--------------------------------------------")
from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(xtrain,ytrain)


print();print();print();print()

print("SVM algorithm:-----------------------------------")
from sklearn.svm import SVC
sv=SVC()
params={"SVC":[1,10,100,1000]}
sv_grid=GridSearchCV(sv,params,cv=5)
sv_grid.fit(xtrain,ytrain)
sv_best=sv_grid.best_estimator_
print(sv_grid.best_params)

print("Logistic algo:----------------------------------------------------------")
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(solver="lbfgs",max_iter=1000)
lr.fit(xtrain,ytrain)

print();print();print()
print("Random Forest:---------------------------------------------------------")

from sklearn.ensemble import RandomForestClassifier
rf=RandomForestClassifier()

params_rf={50,100,200}
rf_gs=GridSearchCV(rf,params_rf,cv=5)

rf_gs.fit(xtrain,ytrain)
rf_best=rf_gs.best_estimator_
print(rf_gs.best_params)






