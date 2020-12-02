import numpy as np
import pandas as pd

a=pd.read_csv("Svm_data.csv")
print(a)


x=a[["x","y"]]
y=a['class']

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)


from sklearn.svm import SVC
clf=SVC(kernel="NonLinear",C=0.001)
clf.fit(xtrain,ytrain)
ypred=clf.predict(xtest)
print("predict",ypred)


from sklearn.metrics import accuracy_score
acc=accuracy_score(ypred,ytest)
print(acc)






