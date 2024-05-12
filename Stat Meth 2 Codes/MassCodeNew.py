import numpy as np
import seaborn as sns
import pandas as pd
import math
import statistics as sts
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
df=pd.read_excel("MassDat.xlsx")
u1 = df.loc[:,'u']
g1= df.loc[:,'g']
r1=df.loc[:,'r']
i1=df.loc[:,'i']
z1=df.loc[:,'z']
reds1=df.loc[:,'redshift']
IntensityList = []
for i in range(4983):
    IntensityList.append([u1[i], g1[i], r1[i], i1[i], z1[i]])

#print(IntensityList[200])
redlistpoints=[]
umean,gmean,rmean,imean,zmean=250,530,700,980,1800
for i in reds1:
    ured=umean/(1+i)
    gred=gmean/(1+i)
    rred=rmean/(1+i)
    ired=imean/(1+i)
    zred=zmean/(1+i)
    redlist=[ured,gred,rred,ired,zred]
    redlistpoints.append(redlist)

dist = []
for i in range(4983):
    dist.append(reds1[i]*(3*10**8)/72)



#print(redlistpoints[200], '\n')

IscoreList = []
def logIscore(redlistpoints, IntensityList):
    for i in range(4983):
        S = 0
        for j in range(5):
            if redlistpoints[i][j] < 400:
                S += 5*u1[i]
                
            elif (redlistpoints[i][j] >= 400) and (redlistpoints[i][j] < 595):
                S += 4*g1[i]

            elif (redlistpoints[i][j] >= 595) and (redlistpoints[i][j] < 700):
                S += 3*r1[i]

            elif (redlistpoints[i][j] >= 700) and (redlistpoints[i][j] < 800):
                S += 2*i1[i]

            else:
                S += z1[i]

        IscoreList.append(S/15)

logIscore(redlistpoints, IntensityList)
#print(IscoreList)

Mass = []
for i in range(4983):
    logM = (IscoreList[i]/IscoreList[0]*(-math.log10(dist[0])))+ math.log10(dist[i])
    Mass.append(10**logM)

#print(Mass)

df2 = pd.read_table("FinalData2.txt")
x1 = df2.loc[:,'x']
y1 = df2.loc[:,'y']
z1 = df2.loc[:,'z']


#center=[[-148188/2, -116932/2, 125808/2], [-179866/2, -133570/2, 16842/2], [-189366/2, -123086/2, -99026/2], [-138994/2, -67838/2, -165420/2], [-106588/2, -25146/2, -220526/2], [-92576/2, -95192/2, 165162/2], [-174980/2, 67246/2, -108338/2], [-89138/2, 153372/2, -49446/2], [-104482/2, 174496/2, 20206/2], [-79914/2, 138470/2, 94828/2], [-78114/2, 126436/2, 177872/2], [-28674/2, 50522/2, 206538/2]]
center=[[-99558.24379432251, -93816.9417305628, 92471.00725097724], [-139638.1602094458, -76421.12844215108, 24420.93814725363], [-141141.01277674694, -68340.22293990494, -49193.35727220487], [-55021.89437775478, -22252.747411751574, -50402.59687961611], [-93167.28236907773, -28804.136073316768, -129764.28532534826], [-58060.779088486895, -48908.37998737092, 34723.67462545727], [-130128.44883057548, 54205.711512838505, -82596.92903000841], [-18382.551592347263, -11321.146877634732, -1713.0423641561251], [-51618.033340700444, 142175.30326360065, -36366.159941158425], [17396.85710297639, 39949.73316516686, 29622.347291205995], [-47591.31799446712, 86163.33026459278, 112604.91970473301], [75458.48984021915, 94747.85190701825, 159561.28271223168]]
datavector=[]
center2=center

for i in range(len(x1)):
    datavector.append([x1[i],y1[i],z1[i]])

datavector.remove(datavector[20])
datavector.remove(datavector[212])
datavector.remove(datavector[344])
datavector.remove(datavector[523])
datavector.remove(datavector[623])
datavector.remove(datavector[642])
datavector.remove(datavector[833])
datavector.remove(datavector[1179])
datavector.remove(datavector[1181])
datavector.remove(datavector[1528])
datavector.remove(datavector[1563])
datavector.remove(datavector[2070])
datavector.remove(datavector[2078])
datavector.remove(datavector[2413])
datavector.remove(datavector[3767])
datavector.remove(datavector[4139])
datavector.remove(datavector[4453])

print(len(datavector))
def dist(a,b):
    return math.sqrt(math.pow((x1[a]-center[b][0]),2)+math.pow((y1[a]-center[b][1]),2)+math.pow((z1[a]-center[b][2]),2))

for s in range(1):
    clusteredpoints=[]
    for i in range (12):
        clusteredpoints.append([])
    for q in range(len(datavector)):
        l=[]
        for j in range (12):
            l.append(dist(q,j))
        ind=l.index(min(l))
        clusteredpoints[ind].append(datavector[q])
    for k in range(len(clusteredpoints)):
        for j in range(3):
            S = 0
            for List in clusteredpoints[k]:
                S += List[j]
            center[k][j] = S/len(clusteredpoints[k])

#print(len(datavector), len(Mass))



CoM = []
for k in range(12):
    num = np.array([0.0,0.0,0.0])
    denom = 0
    for j in range(len(clusteredpoints[k])):
        index = datavector.index(clusteredpoints[k][j])
        denom += Mass[index]
        num += Mass[index]*np.array(datavector[index])
    CoM.append(list(num/denom))


print(CoM)        
        
        
        




    

        
            
    
