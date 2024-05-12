#IMPORTING NECESSARY LIBRARIES
import numpy as np
import seaborn as sns
import pandas as pd
import math
import statistics as sts
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df=pd.read_table("FinalData2.txt",sep="\t")  #TAKING THE DATASET AS INPUT

#STORING THE 3D COORDINATES
x1 = df.loc[:,'x']
y1 = df.loc[:,'y']
z1 = df.loc[:,'z']
sns.set_style("darkgrid")
datavector=[]
for i in range(len(x1)):
    datavector.append([x1[i],y1[i],z1[i]])

core=[]     #STORES THE COORDINATES OF THE CORE POINTS
border=[]   #STORES THE COORDINATES OF THE BORDER POINTS
noise=[]    #STORES THE COORDINATES OF THE NOISE POINTS
clusteredpoints=[]    #STORES ALL THE CLUSTERS
noncluspoints=[]      #STORES THOSE POINTS WHICH ARE NOT A PART OF ANY CLUSTER
data=datavector

#CALCULATING DISTANCE BETWEEN ANY TWO POINTS
def distance(a,b):
    return math.sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)

#RETURNS THE COORDINATES OF GALAXIES WHICH ARE WITHIN AN EPSILON DISTANCE FROM THE CURRENT GALAXY
def spherecheck(eps,v,MinPts):    #eps ---> EPSILON; MinPts ---> MINIMUM NUMBER OF POINTS REQUIRED TO BE PRESENT TO CALL A DATA POINT, A CORE POINT
    l=[]
    for j in datavector:
        if distance(v,j)<eps:
            l.append(j)
    if len(l)==0:
        noise.append(v)
    elif len(l)>=MinPts:
        core.append(v)
    else:
        border.append(v)
    return l

#FORMS INDIVIDUAL CLUSTERS
def cluster_formation(vec,eps,MinPts,cluster):
    lis=spherecheck(eps,vec,MinPts)
    l=[]
    l.append(vec)   #STORES THe GALAXY COORDINATES WHICH HAVE ALREADY BEEN VISITED
    if len(lis)==0:
        noise.append(vec)
        return [],cluster  
    else:
        cluster.extend(lis)
        for k in cluster:
            if k not in l:
                cluster.extend(spherecheck(eps,k,MinPts))
                l.append(k)
        return l,cluster
#'cluster' STORES THE COORDINATES OF ALL GALAXIES IN A SPECIFIC CLUSTER

#CODE FOR THE MAIN ALGORITHM
def dbscan_algo(eps, MinPts):
    i = 0
    while i < len(data):
        clust = []    #STORES EACH INDIVIDUAL CLUSTER
        tup, clust = cluster_formation(data[i], eps, MinPts, clust)  #'tup' STORES COORDINATES OF GALAXIES ALREADY VISITED
        if tup == []:
            i += 1
            continue
        else:
            if len(clust)>=50:
                clusteredpoints.append(clust)
            else:
                for j in clust:
                    if j not in noncluspoints:
                        noncluspoints.append(j)
            for ele in tup:
                data.remove(ele)    #REMOVES THE GALAXY COORDINATES ALREADY VISITED
        if len(data) == 0:
            return True
    return False

#RUNNING THE ALGORITHM WITH eps=12000, MinPts=5
dbscan_algo(12000,5)         

#STORES ALL THE GALAXY COORDINATES WHICH ARE NOT A PART OF ANY CLUSTER
lis = []
for i in clusteredpoints:
    for j in noncluspoints:
        if j not in i and j not in lis:
            lis.append(j)


df_lis = pd.DataFrame(lis)


# PLOT
fig = plt.figure(figsize=(6, 6))
axes = fig.add_subplot(111, projection='3d')

df_cluster = pd.DataFrame(clusteredpoints[0])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='cyan')

df_cluster = pd.DataFrame(clusteredpoints[1])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='b')

df_cluster = pd.DataFrame(clusteredpoints[2])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='g')

df_cluster = pd.DataFrame(clusteredpoints[3])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='r')

df_cluster = pd.DataFrame(clusteredpoints[4])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='pink')

df_cluster = pd.DataFrame(clusteredpoints[5])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='purple')

df_cluster = pd.DataFrame(clusteredpoints[6])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='yellow')

df_cluster = pd.DataFrame(clusteredpoints[7])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='orange')

df_cluster = pd.DataFrame(clusteredpoints[8])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='magenta')

df_cluster = pd.DataFrame(clusteredpoints[9])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1,c='teal')

df_cluster = pd.DataFrame(clusteredpoints[10])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1, c='sienna')

df_cluster = pd.DataFrame(clusteredpoints[11])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1,c='orchid')

df_cluster = pd.DataFrame(clusteredpoints[12])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1,c='gray')

df_cluster = pd.DataFrame(clusteredpoints[13])
axes.scatter3D(df_cluster[0], df_cluster[1], df_cluster[2], s=1,c='olive')

axes.scatter3D(df_lis[0], df_lis[1], df_lis[2], s=1,c='black')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('z')
plt.show()









'''
d={'1': clusteredpoints[0], '2': clusteredpoints[1], '3': clusteredpoints[2],'4': clusteredpoints[3],'5': clusteredpoints[4],'6': clusteredpoints[5],'7': clusteredpoints[6],'8': clusteredpoints[7],'9': clusteredpoints[8], '10': clusteredpoints[9], '11': clusteredpoints[10], '12': clusteredpoints[11]}
lis=[]
for i in d.keys():
    for j in noncluspoints:
        if j not in d[i] and j not in lis:
            lis.append(j)
print(len(lis))

#PLOT

df2=pd.DataFrame(clusteredpoints[0])
#print(df2)
plt.figure(figsize=(6,6))
axes=plt.axes(projection="3d")
print(type(axes))
axes.scatter3D(df2[0],df2[1],df2[2],c="b")

df3=pd.DataFrame(clusteredpoints[1])
#print(df2)
axes.scatter3D(df3[0],df3[1],df3[2],c="g")

df4=pd.DataFrame(clusteredpoints[2])
#print(df2)
axes.scatter3D(df4[0],df4[1],df4[2],c="r")

df5=pd.DataFrame(clusteredpoints[3])
#print(df2)
axes.scatter3D(df5[0],df5[1],df5[2],c="pink")

df6=pd.DataFrame(clusteredpoints[4])
#print(df2)
axes.scatter3D(df6[0],df6[1],df6[2],c="purple")

df7=pd.DataFrame(clusteredpoints[5])
#print(df2)
axes.scatter3D(df7[0],df7[1],df7[2],c="yellow")

df21=pd.DataFrame(clusteredpoints[6])
#print(df2)
axes.scatter3D(df21[0],df21[1],df21[2],c="orange")

df20=pd.DataFrame(clusteredpoints[7])
#print(df2)
axes.scatter3D(df20[0],df20[1],df20[2],c="turquoise")

df8=pd.DataFrame(clusteredpoints[8])
#print(df2)
axes.scatter3D(df8[0],df8[1],df8[2],c="springgreen")

df9=pd.DataFrame(clusteredpoints[9])
#print(df2)
axes.scatter3D(df9[0],df9[1],df9[2],c="sienna")

df10=pd.DataFrame(clusteredpoints[10])
#print(df2)
axes.scatter3D(df10[0],df10[1],df10[2],c="black")

df11=pd.DataFrame(clusteredpoints[11])
#print(df2)
axes.scatter3D(df11[0],df11[1],df11[2],c="orchid")

df=pd.DataFrame(lis)
#print(df2)
axes.scatter3D(lis[0],lis[1],lis[2],c="black")


axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")
plt.show()




'''













