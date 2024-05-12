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
#center=[[-99713.28215159984, -90883.1735397092, 87109.9907030909], [-58759.39266878655, -46132.209893170904, 26028.614919248168], [-135683.63228865725, -77821.8541605901, 22105.223987026286], [-135161.41433525953, -66661.56863780983, -47370.803253497776], [-85561.89371112228, -27831.526993067906, -120331.07895913493], [-15253.558246251196, -14832.71649000177, 6928.504235901593], [-123397.98423054666, 52849.059593719634, -77247.64593357837], [-21843.5328142922, -7602.996154189389, -19477.46270949845], [-68360.80627576819, 139617.008083661, -28859.033186933106], [4056.7084672940773, 21914.693528275857, 18895.48849111634], [-49158.26208869404, 83195.34755934135, 118671.03333809458], [39286.605300545794, 63152.91956741533, 51785.6199145091]]
#center=[[-99558.24379432251, -93816.9417305628, 92471.00725097724], [-139638.1602094458, -76421.12844215108, 24420.93814725363], [-141141.01277674694, -68340.22293990494, -49193.35727220487], [-55021.89437775478, -22252.747411751574, -50402.59687961611], [-93167.28236907773, -28804.136073316768, -129764.28532534826], [-58060.779088486895, -48908.37998737092, 34723.67462545727], [-130128.44883057548, 54205.711512838505, -82596.92903000841], [-18382.551592347263, -11321.146877634732, -1713.0423641561251], [-51618.033340700444, 142175.30326360065, -36366.159941158425], [17396.85710297639, 39949.73316516686, 29622.347291205995], [-47591.31799446712, 86163.33026459278, 112604.91970473301], [75458.48984021915, 94747.85190701825, 159561.28271223168]]
#center=[[-99366.44103458102, -93642.66644365144, 92482.275989936], [-139638.1602094458, -76421.12844215108, 24420.93814725363], [-141264.61409687152, -68451.03944485965, -49251.99683841817], [-55157.459610070226, -22287.5944160047, -50349.73607691404], [-93167.28236907773, -28804.136073316768, -129764.28532534826], [-57869.49841130178, -48630.257541957646, 34219.97297255214], [-130128.44883057548, 54205.711512838505, -82596.92903000841], [-18320.074683410254, -11276.64450640096, -1764.6400684611567], [-51618.033340700444, 142175.30326360065, -36366.159941158425], [17396.85710297639, 39949.73316516686, 29622.347291205995], [-47591.31799446712, 86163.33026459278, 112604.91970473301], [75458.48984021915, 94747.85190701825, 159561.28271223168]]
center=[[-148188/2, -116932/2, 125808/2], [-179866/2, -133570/2, 16842/2], [-189366/2, -123086/2, -99026/2], [-138994/2, -67838/2, -165420/2], [-106588/2, -25146/2, -220526/2], [-92576/2, -95192/2, 165162/2], [-174980/2, 67246/2, -108338/2], [-89138/2, 153372/2, -49446/2], [-104482/2, 174496/2, 20206/2], [-79914/2, 138470/2, 94828/2], [-78114/2, 126436/2, 177872/2], [-28674/2, 50522/2, 206538/2]]
datavector=[]
center2=center

for i in range(len(x1)):
    datavector.append([x1[i],y1[i],z1[i]])

def dist(a,b):
    return math.sqrt(math.pow((x1[a]-center[b][0]),2)+math.pow((y1[a]-center[b][1]),2)+math.pow((z1[a]-center[b][2]),2))

for s in range(50):
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
            S = []
            for List in clusteredpoints[k]:
                S.append(List[j])
            center[k][j] = sts.median(S)
    print(center)
df2=pd.DataFrame(plottingpoints[0])
#print(df2)
plt.figure(figsize=(4,4))
axes=plt.axes(projection="3d")
print(type(axes))
axes.scatter3D(df2[0],df2[1],df2[2],s=1,c="b")
#print(np.cov(np.transpose(df2)))

df3=pd.DataFrame(plottingpoints[1])
#print(df2)
axes.scatter3D(df3[0],df3[1],df3[2],s=1,c="springgreen")
#print(np.cov(np.transpose(df3)))

df4=pd.DataFrame(plottingpoints[2])
#print(df2)
axes.scatter3D(df4[0],df4[1],df4[2],s=1,c="r")
#print(np.cov(np.transpose(df4)))

df5=pd.DataFrame(plottingpoints[3])
#print(df2)
axes.scatter3D(df5[0],df5[1],df5[2],s=1,c="turquoise")
#print(np.cov(np.transpose(df5)))

df6=pd.DataFrame(plottingpoints[4])
#print(df2)
axes.scatter3D(df6[0],df6[1],df6[2],s=1,c="purple")
#print(np.cov(np.transpose(df6)))

df7=pd.DataFrame(plottingpoints[5])
#print(df2)
axes.scatter3D(df7[0],df7[1],df7[2],s=1,c="yellow")
#print(np.cov(np.transpose(df7)))

df21=pd.DataFrame(plottingpoints[6])
#print(df2)
axes.scatter3D(df21[0],df21[1],df21[2],s=1,c="orange")
#print(np.cov(np.transpose(df21)))

df20=pd.DataFrame(plottingpoints[7])
#print(df2)
axes.scatter3D(df20[0],df20[1],df20[2],s=1,c="hotpink")
#print(np.cov(np.transpose(df20)))

df8=pd.DataFrame(plottingpoints[8])
#print(df2)
axes.scatter3D(df8[0],df8[1],df8[2],s=1,c="olivedrab")
#print(np.cov(np.transpose(df8)))

df9=pd.DataFrame(plottingpoints[9])
#print(df2)
axes.scatter3D(df9[0],df9[1],df9[2],s=1,c="cornflowerblue")
#print(np.cov(np.transpose(df9)))

df10=pd.DataFrame(plottingpoints[10])
#print(df2)
axes.scatter3D(df10[0],df10[1],df10[2],s=1,c="brown")
#print(np.cov(np.transpose(df10)))

df11=pd.DataFrame(plottingpoints[11])
#print(df2)
axes.scatter3D(df11[0],df11[1],df11[2],s=1,c="orchid")
#print(np.cov(np.transpose(df11)))



axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
plt.show()

