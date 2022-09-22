import numpy as np
import matplotlib.pyplot as plt
from math import e
import pandas as pd

df=pd.read_excel('datosPendulo.xlsx')

xh1=[0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
#xh1.remove(0)
# x-axis values
# xh1 = [5,13,20,28,45]

# y-axis values
yh1    = df.iloc[0,1:].tolist()
yh2    = df.iloc[1,1:].tolist()
yh3    = df.iloc[2,1:].tolist()
yh4    = df.iloc[3,1:].tolist()
yh5    = df.iloc[4,1:].tolist()
yh6    = df.iloc[5,1:].tolist()
yh7    = df.iloc[6,1:].tolist()
yh8    = df.iloc[7,1:].tolist()
yh9    = df.iloc[8,1:].tolist()
yh10   = df.iloc[9,1:].tolist()

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
plt.xlabel('Longitud, l[m]')
plt.xticks(np.arange(0, 1.1, 0.1))
# frequency label
plt.ylabel('Periodo, T[s]')
#Set the intervals in which the graphic is presented
plt.yticks(np.arange(0.0, 4.8, 0.4))

# plot title

plt.legend((h1, h2, h3, h4, h5, h6, h7, h8, h9, h10),
           ('g1   = (2.50±0.01) m/s²', 
            'g2   = (5.00±0.01) m/s²', 
            'g3   = (7.50±0.01) m/s²', 
            'g4   = (10.00±0.01) m/s²', 
            'g5   = (12.50±0.01) m/s²', 
            'g6   = (15.00±0.01) m/s²', 
            'g7   = (17.50±0.01) m/s²', 
            'g8   = (20.00±0.01) m/s²', 
            'g9   = (22.50±0.01) m/s²', 
            'g10  = (25.00±0.01) m/s²'),
           scatterpoints=1,
           loc='upper left',
           ncol=1,
           fontsize=8)
#plt.title('I-V Bombillo')

plt.grid(b=True, which='major', color='black', linestyle='-', linewidth="0.5")

plt.grid(b=True, which='minor', color='black', linestyle=':', linewidth="0.45")
plt.minorticks_on()



# function to show the plot
plt.show()