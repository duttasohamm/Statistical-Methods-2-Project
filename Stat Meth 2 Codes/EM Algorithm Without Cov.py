import numpy as np
import seaborn as sns
import pandas as pd
import math
import statistics as sts
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
df=pd.read_table("FinalData2.txt",sep="\t")
x1 = df.loc[:,'x']
y1 = df.loc[:,'y']
z1 = df.loc[:,'z']
sns.set_style("darkgrid")
plottingpoints=[]
abscenter=[0,0,0]
center=[[-99558.24379432251, -93816.9417305628, 92471.00725097724], [-139638.1602094458, -76421.12844215108, 24420.93814725363], [-141141.01277674694, -68340.22293990494, -49193.35727220487], [-55021.89437775478, -22252.747411751574, -50402.59687961611], [-93167.28236907773, -28804.136073316768, -129764.28532534826], [-58060.779088486895, -48908.37998737092, 34723.67462545727], [-130128.44883057548, 54205.711512838505, -82596.92903000841], [-18382.551592347263, -11321.146877634732, -1713.0423641561251], [-51618.033340700444, 142175.30326360065, -36366.159941158425], [17396.85710297639, 39949.73316516686, 29622.347291205995], [-47591.31799446712, 86163.33026459278, 112604.91970473301], [75458.48984021915, 94747.85190701825, 159561.28271223168]]
#center=[[-99366.44103458102, -93642.66644365144, 92482.275989936], [-139638.1602094458, -76421.12844215108, 24420.93814725363], [-141264.61409687152, -68451.03944485965, -49251.99683841817], [-55157.459610070226, -22287.5944160047, -50349.73607691404], [-93167.28236907773, -28804.136073316768, -129764.28532534826], [-57869.49841130178, -48630.257541957646, 34219.97297255214], [-130128.44883057548, 54205.711512838505, -82596.92903000841], [-18320.074683410254, -11276.64450640096, -1764.6400684611567], [-51618.033340700444, 142175.30326360065, -36366.159941158425], [17396.85710297639, 39949.73316516686, 29622.347291205995], [-47591.31799446712, 86163.33026459278, 112604.91970473301], [75458.48984021915, 94747.85190701825, 159561.28271223168]]
#center=[[-148188/2, -116932/2, 125808/2], [-179866/2, -133570/2, 16842/2], [-189366/2, -123086/2, -99026/2], [-138994/2, -67838/2, -165420/2], [-106588/2, -25146/2, -220526/2], [-92576/2, -95192/2, 165162/2], [-174980/2, 67246/2, -108338/2], [-89138/2, 153372/2, -49446/2], [-104482/2, 174496/2, 20206/2], [-79914/2, 138470/2, 94828/2], [-78114/2, 126436/2, 177872/2], [-28674/2, 50522/2, 206538/2]]
datavector=[]
center2=center

for i in range(len(x1)):
    datavector.append([x1[i],y1[i],z1[i]])

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
    plottingpoints=clusteredpoints
    for k in range(len(clusteredpoints)):
        for j in range(3):
            S = 0
            for List in clusteredpoints[k]:
                S += List[j]
            center[k][j] = S/len(clusteredpoints[k])
    #print(center)
df2=pd.DataFrame(plottingpoints[0])
#print(df2)
plt.figure(figsize=(4,4))
axes=plt.axes(projection="3d")
#print(type(axes))
axes.scatter3D(df2[0],df2[1],df2[2],s=1,c="b")
M1 = np.cov(np.transpose(df2))
#print(np.cov(np.transpose(df2)))

df3=pd.DataFrame(plottingpoints[1])
#print(df2)
axes.scatter3D(df3[0],df3[1],df3[2],s=1,c="springgreen")
M2 = np.cov(np.transpose(df3))
#print(np.cov(np.transpose(df3)))

df4=pd.DataFrame(plottingpoints[2])
#print(df2)
axes.scatter3D(df4[0],df4[1],df4[2],s=1,c="r")
M3 = np.cov(np.transpose(df4))
#print(np.cov(np.transpose(df4)))

df5=pd.DataFrame(plottingpoints[3])
#print(df2)
axes.scatter3D(df5[0],df5[1],df5[2],s=1,c="turquoise")
M4 = np.cov(np.transpose(df5))
#print(np.cov(np.transpose(df5)))

df6=pd.DataFrame(plottingpoints[4])
#print(df2)
axes.scatter3D(df6[0],df6[1],df6[2],s=1,c="purple")
M5 = np.cov(np.transpose(df6))
#print(np.cov(np.transpose(df6)))

df7=pd.DataFrame(plottingpoints[5])
#print(df2)
axes.scatter3D(df7[0],df7[1],df7[2],s=1,c="yellow")
M6 = np.cov(np.transpose(df7))
#print(np.cov(np.transpose(df7)))

df21=pd.DataFrame(plottingpoints[6])
#print(df2)
axes.scatter3D(df21[0],df21[1],df21[2],s=1,c="orange")
M7 = np.cov(np.transpose(df21))
#print(np.cov(np.transpose(df21)))

df20=pd.DataFrame(plottingpoints[7])
#print(df2)
axes.scatter3D(df20[0],df20[1],df20[2],s=1,c="hotpink")
M8 = np.cov(np.transpose(df20))
#print(np.cov(np.transpose(df20)))

df8=pd.DataFrame(plottingpoints[8])
#print(df2)
axes.scatter3D(df8[0],df8[1],df8[2],s=1,c="olivedrab")
M9 = np.cov(np.transpose(df20))
#print(np.cov(np.transpose(df20)))

df9=pd.DataFrame(plottingpoints[9])
#print(df2)
axes.scatter3D(df9[0],df9[1],df9[2],s=1,c="cornflowerblue")
M10 = np.cov(np.transpose(df9))
#print(np.cov(np.transpose(df9)))

df10=pd.DataFrame(plottingpoints[10])
#print(df2)
axes.scatter3D(df10[0],df10[1],df10[2],s=1,c="brown")
M11 = np.cov(np.transpose(df10))
#print(np.cov(np.transpose(df10)))

df11=pd.DataFrame(plottingpoints[11])
#print(df2)
axes.scatter3D(df11[0],df11[1],df11[2],s=1,c="orchid")
M12 = np.cov(np.transpose(df11))
#print(np.cov(np.transpose(df11)))


'''
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
axes.scatter3D(center[0][0],center[0][1],center[0][2],s=50,color='black')
plt.show()
'''

import numpy as np
import math
import pandas as pd


K=12
#12 clusters have been formed just through visual inspection.
pilist=[]
for i in range(12):
    pilist.append(1/12)
sigma=np.identity(3)

matL = [M1/100000000, M2/100000000, M3/100000000, M4/100000000, M5/100000000, M6/100000000, M7/100000000, M8/100000000, M9/100000000, M10/100000000, M11/100000000, M12/100000000]
   
mu2=[]
mu=[[-9.95582437943225, -9.38169417305628, 9.247100725097724], [-13.96381602094458, -7.642112844215108, 2.442093814725363], [-14.114101277674694, -6.834022293990494, -4.919335727220487], [-5.5021894377754785, -2.2252747411751574, -5.040259687961611], [-9.316728236907773, -2.880413607331677, -12.976428532534825], [-5.80607790884869, -4.8908379987370925, 3.4723674625457273], [-13.012844883057548, 5.42057115128385, -8.259692903000841], [-1.8382551592347263, -1.1321146877634731, -0.17130423641561252], [-5.161803334070044, 14.217530326360066, -3.6366159941158425], [1.739685710297639, 3.9949733165166856, 2.9622347291205995], [-4.759131799446712, 8.616333026459278, 11.260491970473302], [7.545848984021915, 9.474785190701825, 15.956128271223168]]
#mu=[[-148188/2, -116932/2, 125808/2], [-179866/2, -133570/2, 16842/2], [-189366/2, -123086/2, -99026/2], [-138994/2, -67838/2, -165420/2], [-106588/2, -25146/2, -220526/2], [-92576/2, -95192/2, 165162/2], [-174980/2, 67246/2, -108338/2], [-89138/2, 153372/2, -49446/2], [-104482/2, 174496/2, 20206/2], [-79914/2, 138470/2, 94828/2], [-78114/2, 126436/2, 177872/2], [-28674/2, 50522/2, 206538/2]]

df=pd.read_table("FinalData2.txt",sep="\t")
x1 = df.loc[:,'x']/10000
y1 = df.loc[:,'y']/10000
z1 = df.loc[:,'z']/10000

datavector=[]
for i in range(len(x1)):
    datavector.append([x1[i],y1[i],z1[i]])
    
for i in range(50):
    
    log_likelihood=0
    for n in range(5000):
        s=0
        for k in range(12):
            factor =((math.pow(2*math.pi,3/2)*(np.linalg.det(matL[k])))**0.5)
            diff = [(x-y) for x,y in zip(datavector[n],mu[k])]
            exponent = -0.5 * (np.transpose(diff) @(np.linalg.inv(matL[k]))@diff)
            s+=(pilist[k] * np.exp(exponent) / factor)
        log_likelihood+=np.log(s)
    print('#', i+1)
    print(log_likelihood, '\n')

    
    def R(n,k):
        factor =((math.pow(2*math.pi,3/2)*(np.linalg.det(matL[k])))**0.5)
        diff = [(x-y) for x,y in zip(datavector[n],mu[k])]
        exponent = -0.5 * (np.transpose(diff) @(np.linalg.inv(matL[k]))@diff)
        num=pilist[k]* np.exp(exponent) /factor
        S1 = 0
        for j in range(12):
            factor =((math.pow(2*math.pi,3/2)*(np.linalg.det(matL[j])))**0.5)
            diff = [(x-y) for x,y in zip(datavector[n],mu[j])]
            exponent = -0.5 * (np.transpose(diff) @(np.linalg.inv(matL[j]))@diff)
            denom = pilist[j]*np.exp(exponent) / factor
            S1+=denom
        return num/S1

    
    N_k = []        
    for k in range(12):
        S2 = 0
        for n in range(len(datavector)):
            S2+= R(n,k)
        N_k.append(S2)
        
    mu_new = []
    for k in range(12):
        num1 = 0
        for n in range(len(datavector)):
            alpha = R(n,k)*np.array(datavector[n])
            num1+=alpha
        mu_new.append(num1/N_k[k])
    
    
    '''matL_new = []
    for k in range(12):
        num2 = 0
        for n in range(len(datavector)):
            beta = R(n,k)*np.outer((np.array(datavector[n])- np.array(mu[k])),(np.transpose(np.array(datavector[n])- np.array(mu[k]))))
            #print(k ,'.', n)
            num2+=beta
        matL_new.append(num2/N_k[k])
    print(matL_new, '\n')''' 
        

    for k  in range(12):
        pilist[k] = N_k[k]/len(datavector)
    #print(pilist)

    mu = mu_new
    #matL = matL_new

print(mu, '\n')
print(matL, '\n')
print(pilist)
    
     



