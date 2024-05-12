import seaborn as seaborn
import matplotlib.pyplot as plot
import numpy as np
import pandas as pd
import pyautogui as pgi
import pynput as pnt
df=pd.read_table("FinalData2.txt",sep="\t")
seaborn.set_style("darkgrid")

x1 = df.loc[:,'x']
y1 = df.loc[:,'y']
z1 = df.loc[:,'z']

plot.figure(figsize=(10, 10))
axes = plot.axes(projection="3d")
print(type(axes))
axes.scatter3D(x1, y1, z1)
axes.set_xlabel("x")
axes.set_ylabel("y")
axes.set_zlabel("z")

print(pgi.position())
plot.show()



