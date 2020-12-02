##3.Logistic Regression on credit card data to predict whether it is fraud or not.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

a=pd.read_csv("creditcard.csv")

v22=a["V22"].mean()
a["V22"]=a["V22"].fillna(v22).astype(int)

v23=a["V23"].mean()
a["V23"]=a["V23"].fillna(v23).astype(int)

v24=a["V24"].mean()
a["V24"]=a["V24"].fillna(v24).astype(int)

v25=a["V25"].mean()
a["V25"]=a["V25"].fillna(v25).astype(int)

v26=a["V26"].mean()
a["V26"]=a["V26"].fillna(v26).astype(int)

v27=a["V27"].mean()
a["V27"]=a["V27"].fillna(v27).astype(int)

v28=a["V28"].mean()
a["V28"]=a["V28"].fillna(v28).astype(int)

amount=a["Amount"].mean()
a["Amount"]=a["Amount"].fillna(amount).astype(int)

Class=a["Class"].mean()
a["Class"]=a["Class"].fillna(Class).astype(int)

x=a.drop(columns=["Class","Amount"])
y=a["Amount"]

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


lr=LogisticRegression()
lr.fit(x_train,y_train)
y_pred=lr.predict(x_test)
print(y_pred)





