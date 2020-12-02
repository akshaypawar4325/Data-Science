import pandas as pd
'''
d=pd.DataFrame()
d["roll"]=[1,2,3]
d["name"]=["abc","def","ghi"]
print(d)
print(d["roll"][2])
'''
d=pd.DataFrame()
r=[]
n=[]
m=[]
cnt=int(input("Add: "))
for i in range(cnt):
    name=input("Enter the name:")
    roll=int(input("Enter the roll no:"))
    marks=int(input("Enter the marks:"))
    n.append(name)
    r.append(roll)
    m.append(marks)
d["roll"]=r
d["name"]=n
d["marks"]=m
print(d)
d.to_csv("data.csv")
