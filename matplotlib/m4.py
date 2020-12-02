import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


a=pd.read_csv("data.csv")
b=a["x"]
c=a["y"]
plt.plot(b,c,color="b",marker="*")
plt.show()
print()


