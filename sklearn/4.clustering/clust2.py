import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

a=sns.load_dataset("iris")
print(a)
x=a.drop(columns='species')
sns.scatterplot(x="sepal_length",y='sepal_width',data=a)
plt.show()
sns.scatterplot(x="petal_length",y='petal_width',data=a)
plt.show()
from sklearn.cluster import KMeans
c=KMeans(n_clusters=3)
c.fit(x)
labels=c.labels_
print(labels)

new_cen=c.cluster_centers_
print(new_cen)

print(new_cen[0][3])

plt.scatter(a["sepal_length"],a["sepal_width"],c=labels)
plt.scatter(a["petal_length"],a["petal_width"],c=labels)
plt.scatter(new_cen[0][0],new_cen[0][1],new_cen[0][2],new_cen[0][3],marker="*")
plt.scatter(new_cen[1][0],new_cen[1][1],new_cen[1][2],new_cen[1][3],marker="^")
plt.scatter(new_cen[2][0],new_cen[2][1],new_cen[2][2],new_cen[2][3],marker="*")
plt.show()


