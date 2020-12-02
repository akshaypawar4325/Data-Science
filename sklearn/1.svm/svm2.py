Dont run this program at all time

'''
Don't Run this program 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
a=pd.read_csv("Svm_data.csv")

x=a[['x','y']]
y=a['y']

plt.scatter(x.x,x.y)

from sklearn.svm import SVC

clf=SVC(kernel="linear",C=0.001)
clf.fit(x,y)
ax=plt.gca()
xlim=ax.get_xlim()
ylim=ax.get_ylim()

xx=np.linspace(xlim[0],xlim[1],200)
yy=np.linspace(ylim[0],ylim[1],200)

YY,XX=np.meshgrid(yy,xx)
xy=np.vstack([XX.ravel(),YY.ravel()]).T
z=clf.decision_function(xy).reshape(XX.shape)


ax.contour(XX, YY, z, colors='r', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
b=ax.scatter(clf.support_vectors_[:, 0], clf.support_vectors_[:, 1], s=100, linewidth=1, facecolors='r')
plt.legend([b ], ["Support Vector"])
plt.show()
'''
