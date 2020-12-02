import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a=pd.read_csv("data.csv")
b=a["x"]
c=a["y"]

##plt.plot(b,c,color="b",marker="*")
##plt.show()

fig=plt.figure()
ax=fig.gca(projection="3d")
ax.plot(b,c)
plt.show()
##ax = fig.add_subplot(111, projection='3d')
##ax.scatter(b,c,marker="^")


ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

plt.show()
