import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("stockmarket.csv",usecols=[5,6,7,8,9,10,17,19,20,21,
                                          22,24,25,26,27,30,31,32,33,
                                          34,35,39,40,41,42,43,44,45,
                                          46,49,50,51,52,53,54,55,56,
                                          57,58,59])


print(df.info())
