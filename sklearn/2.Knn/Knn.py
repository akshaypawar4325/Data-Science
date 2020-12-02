import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
a=pd.read_csv("kdata.csv")
x=a[['x','y']]
y=a['class']
sns.scatterplot(x="x",y="y",hue="class",data=a)
plt.show()


from sklearn.neighbors import KNeighborsClassifier

k=KNeighborsClassifier(n_neighbors=5)
k.fit(x,y)
ypred=k.predict([[6,6]])
print(ypred)


k=KNeighborsClassifier(n_neighbors=5,weights="distance")
k.fit(x,y)
pred=k.predict([[7,2]])
print(pred)
