# This program uses the pyplot module to plot a set of 
# numbers (obtained from y1=x**2-x+3) and a function 

import numpy as np
import matplotlib.pyplot as plt

# Define the array of independent variable values
x=np.linspace(-10,10,20)
# Define the array of dependent variable values
y1=np.array([113.0,92.0027700831,73.2216066482, \
56.6565096953,42.3074792244,30.1745152355,20.2576177285, \
12.5567867036,7.07202216066,3.80332409972,2.75069252078,  \
3.91412742382,7.29362880886,12.8891966759,20.7008310249, \
30.728531856,42.972299169,57.432132964,74.108033241,93.0],float)

# Define the second array using a mathematical function 
y2=0.05*x**3+20

print "x=", x

# Plot both arrays 
plt.plot(x,y1)
plt.plot(x,y2)
plt.title ('An example of a plot')
plt.show()