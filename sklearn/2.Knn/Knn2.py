'''import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
a=pd.read_csv("shirt.csv")
x=a[['Height','Weight']]
y=a['T-ShirtSize']
sns.scatterplot(x="Height",y="Weight",hue="T-ShirtSize",data=a)
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



'''
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
a=pd.read_csv("shirt.csv")

x=a[["Height","Weight"]]
y=a["T-ShirtSize"]

kn=KNeighborsClassifier(n_neighbors=10)
kn.fit(x,y)
y_pred=kn.predict([[170,68]])
print(y_pred)

'''



















