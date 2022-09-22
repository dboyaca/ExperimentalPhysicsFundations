import numpy as np
import matplotlib.pyplot as plt
from math import e
import pandas as pd

df=pd.read_excel('datosPendulo.xlsx')
def f(x):
   return 240*(e**(0.13*x))
xh1=df.iloc[:,0]
print(xh1)
xh1=xh1.to_list()
#xh1.remove(0)
# x-axis values
# xh1 = [5,13,20,28,45]

# y-axis values
yh1    = df.iloc[0:,1].tolist()
yh2    = df.iloc[0:,2].tolist()
yh3    = df.iloc[0:,3].tolist()
yh4    = df.iloc[0:,4].tolist()
yh5    = df.iloc[0:,5].tolist()
yh6    = df.iloc[0:,6].tolist()
yh7    = df.iloc[0:,7].tolist()
yh8    = df.iloc[0:,8].tolist()
yh9    = df.iloc[0:,9].tolist()
yh10   = df.iloc[0:,10].tolist()
# plotting points as a scatter plot
h1 = plt.scatter(xh1, yh1, label= "star", color= "darkgreen",
            marker= "*", s=30)
h2 = plt.scatter(xh1, yh2, label= "x", color= "blue",
            marker= "x", s=30)
h3 = plt.scatter(xh1, yh3, label= "plus", color= "red",
            marker= "+", s=30)
h4 = plt.scatter(xh1, yh4, label= "square", color= "brown",
            marker= "s", s=20)
h5 = plt.scatter(xh1, yh5, label= "tri-up", color= "black",
            marker= "2", s=40)            
h6 = plt.scatter(xh1, yh6, label= "circle", color= "orange",
            marker= "o", s=20)    
h7 = plt.scatter(xh1, yh7, label= "triangle_up", color= "purple",
            marker= "^", s=20)     
h8 = plt.scatter(xh1, yh8, label= "diamond", color= "m",
            marker= "D", s=20)     
h9 = plt.scatter(xh1, yh9, label= "x", color= "c",
            marker= "x", s=30)     
h10 = plt.scatter(xh1, yh10, label= "tri-right", color= "red",
            marker= "4", s=40)     



# x-axis label
plt.xlabel('Gravedad, g[m/s2]')
plt.xticks(np.arange(0, 27.5, 2.5))
# frequency label
plt.ylabel('Periodo, T[s]')
#Set the intervals in which the graphic is presented
plt.yticks(np.arange(0, 4.5, 0.5))

# plot title

plt.legend((h1, h2, h3, h4, h5, h6, h7, h8, h9, h10),
           ('l1   = (0.10±0.01)m', 
            'l2   = (0.20±0.01)m', 
            'l3   = (0.30±0.01)m', 
            'l4   = (o.40±0.01)m', 
            'l5   = (0.50±0.01)m', 
            'l6   = (0.60±0.01)m', 
            'l7   = (0.70±0.01)m', 
            'l8   = (0.80±0.01)m', 
            'l9   = (0.90±0.01)m', 
            'l10  = (1.00±0.01)m'),
           scatterpoints=1,
           loc='upper right',
           ncol=1,
           fontsize=8)
#plt.title('I-V Bombillo')

plt.grid(b=True, which='major', color='black', linestyle='-', linewidth="0.5")

plt.grid(b=True, which='minor', color='black', linestyle=':', linewidth="0.45")
plt.minorticks_on()



# function to show the plot
plt.show()