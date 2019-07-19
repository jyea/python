import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

directory = r'D:\recent\论文素材\总的内容'
os.chdir(directory)
file_path = os.path.join(directory, '站点汇总.xlsx' )
data = pd.read_excel(file_path, encoding='utf-8')

x = data['lambda']
#df.ix[0:2,[1,2]]	#第0行到第2行（包含第3行），第1列和第2列的数据
y = data.iloc[0:150,1:43]
print(y)
j = y.columns
#color=[1 0 0;0 1 0;0 0 1;0.5 1 1;1 1 0.5;1 0.5 1; 0 0 0.5; 0.5 0 0;0 0.5 0;1 0.5 0.5; 0.5 1 0.5;0.5 0.5 1;1 1 0;0 1 1;1 0 1];
color=[]
fig = plt.figure(figsize=(6,3))
i=0
#做渐变色折线图
for name in j:
    red_value = 1-(1/22)*i
    if red_value < 0:
        red_value = (0-red_value)*0.9
    
    green_value = 0+(1/22)*i
    if green_value >1:
        green_value = green_value - 1
        
    blue_value = 0+(1/22)*i
    if blue_value >1:
        blue_value = blue_value-1
    color.append([red_value, green_value, blue_value])
    plt.plot(x, y[name],c=color[i])
    i+=1

plt.show()
