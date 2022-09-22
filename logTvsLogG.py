import numpy as np
import matplotlib.pyplot as plt
from math import log10
import pandas as pd

df=pd.read_excel('datosPendulo.xlsx')

def f(x):
   return log10(x)

# x-axis values
xh1=df.iloc[:,0]
xh1=xh1.to_list()
print(xh1)
logxh1 = []

#Add the log1O of the x-axis values
for i in xh1:
    logxh1.append(f(i))

print(logxh1)
# y-axis values
yh = [df.iloc[0:,1].tolist(),
      df.iloc[0:,2].tolist(),
      df.iloc[0:,3].tolist(),
      df.iloc[0:,4].tolist(),
      df.iloc[0:,5].tolist(),
      df.iloc[0:,6].tolist(),
      df.iloc[0:,7].tolist(),
      df.iloc[0:,8].tolist(),
      df.iloc[0:,9].tolist(),
      df.iloc[0:,10].tolist()]

#Create an empty matrix with lists within it.
logyh = [[0 for i in range(len(yh[0]))] for i in range(len(yh))]

for i in range(0,10):
    for index, value in enumerate(yh[i]):
        logyh[i][index] = f(value)

#It worked perfectly
#print(logyh)

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
h1 = plt.scatter(logxh1, logyh[0], label= "star", color= "darkgreen",
            marker= "*", s=30)
h2 = plt.scatter(logxh1, logyh[1], label= "x", color= "blue",
            marker= "x", s=30)
h3 = plt.scatter(logxh1, logyh[2], label= "plus", color= "red",
            marker= "+", s=30)
h4 = plt.scatter(logxh1, logyh[3], label= "square", color= "brown",
            marker= "s", s=30)
h5 = plt.scatter(logxh1, logyh[4], label= "tri-up", color= "black",
            marker= "2", s=40)            
h6 = plt.scatter(logxh1, logyh[5], label= "circle", color= "orange",
            marker= "o", s=20)            
h7 = plt.scatter(logxh1, logyh[6], label= "triangle-up", color= "purple",
            marker= "^", s=20)            
h8 = plt.scatter(logxh1, logyh[7], label= "diamond", color= "m",
            marker= "D", s=20)     
h9 = plt.scatter(logxh1, logyh[8], label= "x", color= "c",
            marker= "x", s=30)     
h10 = plt.scatter(logxh1, logyh[9], label= "tri-right", color= "red",
            marker= "4", s=40)          

# x-axis label
plt.xlabel('Log g')
plt.xticks(np.arange(0.3, 1.6, 0.1))
# frequency label
plt.ylabel('Log T')
#Set the intervals in which the graphic is presented
plt.yticks(np.arange(-0.5, 1.1, 0.1))

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