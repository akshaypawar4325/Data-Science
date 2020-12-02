import pandas as pd
import numpy as np
a=pd.Series([1,2,3,4])
print(a)
b=pd.Series([1,2,3,4],index=(10,20,30,40))
print(b)
print(a[2])
print()
c=pd.Series({"a":1,"b":2,"c":3})
print(c)
print(c["b"])
print()
print()
d=pd.Series(3,index=(1,2,3,4,5))
print(d)
print()
print()



