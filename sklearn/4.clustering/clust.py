import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import numpy as np
##plt.style.use("seaborn-whitegrid")
a={'X':[0.1,0.15,0.08,0.16,0.2,0.25,0.24,0.3],'Y':[0.6,0.71,0.9,0.85,0.3,0.5,0.1,0.2]}

b=pd.DataFrame(a)
print(b)

p1=b["X"].values
p2=b['Y'].values

X=np.array(list(zip(p1,p2)))

sns.scatterplot(x="X",y="Y",data=b)

from sklearn.cluster import KMeans
c=KMeans(n_clusters=2)
c.fit(X)
labels=c.labels_
print(labels)

new_cen=c.cluster_centers_
print(new_cen)
print(new_cen[0])
print()


plt.scatter(b['X'],b['Y'],c=labels)
plt.scatter(new_cen[0][0],new_cen[0][1],marker='*',color='r')
plt.scatter(new_cen[1][0],new_cen[1][1],marker='*',color='b')
plt.show()


