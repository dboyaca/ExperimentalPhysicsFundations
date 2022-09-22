import numpy as np
import matplotlib.pyplot as plt
from math import log10
import pandas as pd

df=pd.read_excel('datosPendulo.xlsx')

def f(x):
   return log10(x)

# x-axis values
xh1=[0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 1.00]
print(xh1)
logxh1 = []

#Add the log1O of the x-axis values
for i in xh1:
    logxh1.append(f(i))

print(logxh1)
# y-axis values
yh = [df.iloc[0,1:].tolist(),
      df.iloc[1,1:].tolist(),
      df.iloc[2,1:].tolist(),
      df.iloc[3,1:].tolist(),
      df.iloc[4,1:].tolist(),
      df.iloc[5,1:].tolist(),
      df.iloc[6,1:].tolist(),
      df.iloc[7,1:].tolist(),
      df.iloc[8,1:].tolist(),
      df.iloc[9,1:].tolist()]

#Create an empty matrix with lists within it.
logyh = [[0 for i in range(len(yh[0]))] for i in range(len(yh))]

for i in range(0,10):
    for index, value in enumerate(yh[i]):
        logyh[i][index] = f(value)

#It worked perfectly
#print(logyh)

print(logyh)

#Finding the y-axis max and min value
max = logyh[0][0]
min = logyh[0][0]
for i in range(0,10):
    for j in range(0,10):
        if logyh[i][j] > max:
            max = logyh[i][j]
        
        if logyh[i][j] < min:
            min = logyh[i][j]


print("Maximo: " , max)
print("Minimo: " , min)

# plotting points as a scatter plot
h1 = plt.scatter(xh1, logyh[0], label= "star", color= "darkgreen",
            marker= "*", s=30)
h2 = plt.scatter(xh1, logyh[1], label= "x", color= "blue",
            marker= "x", s=30)
h3 = plt.scatter(xh1, logyh[2], label= "plus", color= "red",
            marker= "+", s=30)
h4 = plt.scatter(xh1, logyh[3], label= "square", color= "brown",
            marker= "s", s=30)
h5 = plt.scatter(xh1, logyh[4], label= "tri-up", color= "black",
            marker= "2", s=40)            
h6 = plt.scatter(xh1, logyh[5], label= "circle", color= "orange",
            marker= "o", s=20)            
h7 = plt.scatter(xh1, logyh[6], label= "triangle-up", color= "purple",
            marker= "^", s=20)            
h8 = plt.scatter(xh1, logyh[7], label= "diamond", color= "m",
            marker= "D", s=20)     
h9 = plt.scatter(xh1, logyh[8], label= "x", color= "c",
            marker= "x", s=30)     
h10 = plt.scatter(xh1, logyh[9], label= "tri-right", color= "red",
            marker= "4", s=40)          

# x-axis label
plt.xlabel('Longitud, l[m]')
plt.xticks(np.arange(0, 1.1, 0.1))
# frequency label
plt.ylabel('Log T')
#Set the intervals in which the graphic is presented
plt.yticks(np.arange(-0.7, 0.8, 0.1))

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
           loc='lower right',
           ncol=2,
           fontsize=8)
#plt.title('I-V Bombillo')

plt.grid(b=True, which='major', color='black', linestyle='-', linewidth="0.5")

plt.grid(b=True, which='minor', color='black', linestyle=':', linewidth="0.45")
plt.minorticks_on()



# function to show the plot
plt.show()