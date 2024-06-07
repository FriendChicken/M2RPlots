

import matplotlib.pyplot as plt
import numpy as np
a = 2
y = np.linspace(0,2,1000)
x = np.sqrt((a*y**2-y**3-y)/(y-a))
x = np.concatenate((-x,x), axis=0)
y = np.concatenate((y,y), axis=0)
plt.plot(x, y, label='I=' + str(a))
a = -2
y = np.linspace(-2,0,1000)
x = np.sqrt((a*y**2-y**3-y)/(y-a))
x = np.concatenate((-x,x), axis=0)
y = np.concatenate((y,y), axis=0)
plt.plot(x, y, label='I=' + str(a))
# Generate data
"""for i in range(-5,5):
    a = i
    x = np.linspace(-10,10,10000)
    y = np.sqrt((a*x**2-x**3+x)/(x-a))
    x = np.concatenate((x,x), axis=0)
    y = np.concatenate((-y,y), axis=0)
    plt.plot(x, y, label='R=' + str(a))"""
a = -3
x = np.linspace(-10,10,10000)
y = np.sqrt((a*x**2-x**3+x)/(x-a))
x = np.concatenate((x,x), axis=0)
y = np.concatenate((-y,y), axis=0)
plt.plot(x, y, label='R=' + str(a))
a = 0
x = np.linspace(-10,10,10000)
y = np.sqrt((a*x**2-x**3+x)/(x-a))
x = np.concatenate((x,x), axis=0)
y = np.concatenate((-y,y), axis=0)
plt.plot(x, y, label='C')
# Plotting multiple lines on a single plot
#plt.plot(x, y2, label='Cos(x)', color='r', linestyle='--')
  
# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Multiple Lines Plot')
 
# Displaying the legend and the plot
plt.legend()
plt.show()
