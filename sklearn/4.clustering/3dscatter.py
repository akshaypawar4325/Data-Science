import numpy as np
import matplotlib.pyplot as plt
x=np.random.randint(0,100,200)
y=np.random.randint(0,100,200)
z=np.random.randint(0,100,200)
from mpl_toolkits.mplot3d import Axes3D
fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.scatter(x,y,z,marker="^")
plt.show()
