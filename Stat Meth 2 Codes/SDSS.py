import pandas as pd
import math
df = pd.read_table("SDSSdat.csv", sep = ",")
#print(df)
#print(df.loc[:,"V"]/72)
'''L = []
for i in df.loc[:,"V"]:
    L.append(float(i))

print(L)'''
#File = open("Shapley_galaxy.txt", 'r')
#print(File.read())
#File.close()

df["r"] = df.loc[:,"redshift"]*3*10**5
df["t"] = (math.pi)/2 - df.loc[:,"dec"]
df["p"] = (math.pi)/180*(df.loc[:,"ra"])
L = []
for i in df.loc[:,"t"]:
    L.append(math.cos(i))

df["cost"] = L


L2 = []
for i in df.loc[:,"t"]:
    L2.append(math.sin(i))

df["sint"] = L2

L3 = []
for i in df.loc[:,"p"]:
    L3.append(math.sin(i))

df["sinp"] = L3

L4 = []
for i in df.loc[:,"p"]:
    L4.append(math.cos(i))

df["cosp"] = L4


L5 = []
for i in range(5000):
    L5.append(df.loc[:, "sint"][i]*df.loc[:,"cosp"][i]*df.loc[:,"r"][i])
df["x"] = L5

L6 = []
for i in range(5000):
    L6.append(df.loc[:, "sint"][i]*df.loc[:,"sinp"][i]*df.loc[:,"r"][i])
df["y"] = L6


L1 = []
for i in range(5000):
    L1.append(df.loc[:,"cost"][i]*df.loc[:,"r"][i])

df["z"] = L1
print(df)


dat = pd.DataFrame(df)
dat.to_csv("FinalData2.txt", sep = '\t')

