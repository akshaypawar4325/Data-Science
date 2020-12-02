import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.random.randint(0,50,200)
y=np.random.randint(0,50,200)

plt.plot(x,y,color="r",marker="*")

plt.scatter(x,y)
plt.show()


d=pd.DataFrame()
d["x"]=x
d["y"]=y
d.to_csv("data.csv")
print(d)

