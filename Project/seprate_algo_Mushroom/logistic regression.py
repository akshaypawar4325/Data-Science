import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("mushrooms.csv")

X=df.drop(columns="class")
y=df["class"]

from sklearn.preprocessing import LabelEncoder
## X variable label Encoder
lex=LabelEncoder()
for i in X:
    X[i]=lex.fit_transform(X[i])

## y label Encoder
ley=LabelEncoder()
y=ley.fit_transform(y)

X=pd.get_dummies(X,columns=X.columns,drop_first=True)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(X,y,test_size=0.25)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
xtrain = sc.fit_transform(xtrain)
xtest = sc.transform(xtest)

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
xtrain = pca.fit_transform(xtrain)
xtest = pca.transform(xtest)

from sklearn.linear_model import LogisticRegression
lr=LogisticRegression(solver="lbfgs",max_iter=1000)
lr.fit(xtrain,ytrain)
ypred=lr.predict(xtest)
print(ypred)

from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
acc=accuracy_score(ytest,ypred)
print(acc)

cm=confusion_matrix(ytest,ypred)
print()
print(cm)

cr=classification_report(ytest,ypred)
print(cr)





                            
