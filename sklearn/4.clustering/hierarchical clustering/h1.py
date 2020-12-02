import numpy as np
import matplotlib.pyplot as plt
X = np.array([[5,3],
    [10,15],
    [15,12],
    [24,10],
    [30,30],
    [85,70],
    [71,80],
    [60,78],
    [70,55],
    [80,91],])
print(X)

from sklearn.cluster import AgglomerativeClustering
cl=AgglomerativeClustering(n_clusters=4,affinity="euclidean",linkage="single")
cl.fit_predict(X)
label=cl.labels_

plt.scatter(X[:,0],X[:,1],c=label)
plt.show()

cl=AgglomerativeClustering(n_clusters=4,affinity="euclidean",linkage="complete")
cl.fit_predict(X)
label1=cl.labels_

plt.scatter(X[:,0],X[:,1],c=label1)
plt.show()

cl=AgglomerativeClustering(n_clusters=4,affinity="euclidean",linkage="average")
cl.fit_predict(X)
label2=cl.labels_

plt.scatter(X[:,0],X[:,1],c=label2)
plt.show()
