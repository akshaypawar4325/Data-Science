import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("stockmarket.csv")

for i in df:
    
    df[i]=df[i].fillna(0)

x=df.drop(columns=["Share","Category","Sector","RM","Up",'Yearly Gainner',
                   '27th Dec', '1st Feb', '1st March',
                   '1st April', 'TB',"Corr","Corre",'Annual Growth', 'Year End',
                   'Y oY PAT', "LQ>0.5(4q's)", 'PAT Growth','FaceValue',
                   'New Listing', 'PE High Price High', 'Future',
                   'Cap Category'])
"""
Index(['Last Traded Price', 'Percentage Change', 'High Price', 'Low Price',
       '% High Movt', '% Low movt', 'RH', 'PeRatio', 'New Pe', 'W52_High',
       'latest', 'Annual_Pat', 'Cum PAT 3 Quarter', 'Pat Jump',
       'Mar_17_ReportedPAT', 'Dec_16_ReportedPAT', 'Sep_16_ReportedPAT',
       'Jun_16_ReportedPAT', 'Mar_16_ReportedPAT', 'Dec_15_ReportedPAT',
       'PeRatio.1', 'ResultDate', 'Mar_17_Inst_no_of_shares',
       'Dec_16_Inst_no_of_shares', 'Int/ Incr/ Decr', 'Pledge',
       'DividendYield', 'DERatio', 'FB', 'Mar_17_Eps_Before',
       'Dec_16_Eps_Before', 'Sep_16_Eps_Before', 'Jun_16_Eps_Before',
       'Mar_16_Eps_Before', 'Dec_15_Eps_Before', 'Annual_Eps', 'Volume',
       'MarketCap', 'Annual_Pat.1', 'EquityCapital'],
      dtype='object')
"""



y=df["FaceValue"]


plt.scatter(x,y)
plt.show()

from sklearn.model_selection import train_test_split

xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)



