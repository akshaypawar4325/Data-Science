import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
rng=np.random.RandomState(1)


d=pd.DataFrame()

x=10*rng.rand(100)
y=2*x-5+rng.randn(100)





d["x"]=x
d['y']=y



plt.scatter(x,y,marker="^")


from sklearn.linear_model import LinearRegression

model=LinearRegression()

model.fit(x[:,np.newaxis],y)
xfit=np.linspace(0,10,1000)
yfit=model.predict(xfit[:,np.newaxis])

plt.scatter(x,y,)
plt.plot(xfit,yfit)


print(model.coef_)
print(model.intercept_)
