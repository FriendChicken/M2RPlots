import numpy as np
from matplotlib import pyplot as plt

# generate data
x = np.r_[0:100:30j]
y = np.r_[0:1:20j]
X, Y = np.meshgrid(x, y)
Z = X*np.exp(1j*Y) # some arbitrary complex data

# plot it
def plotit(z, title):
    plt.figure()
    cs = plt.contour(X,Y,z) # contour() accepts complex values
    plt.clabel(cs, inline=1, fontsize=10) # add labels to contours
    plt.title(title)
    plt.savefig(title+'.png')

plotit(Z, 'real')
plotit(Z.real, 'explicit real')
plotit(Z.imag, 'imagenary')

plt.show()
