from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from scipy.interpolate import griddata
import numpy as np

from pprint import pprint

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

x1, y1 = 0,0
x2,y2 = 0,1
x3,y3 = 1,0

scale = 10

def PHI1():
    x, y = np.meshgrid(np.linspace(0, 1, scale), np.linspace(0, 1, scale))
    z = ((y2-y3)*(x-x3)+(x3-x2)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3));
    return x, y, z

def PHI2():
    x, y = np.meshgrid(np.linspace(0, 1, scale), np.linspace(0, 1, scale))
    z = ((y3-y1)*(x-x3)+(x1-x3)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3));
    return x, y, z

def PHI3():
    x, y = np.meshgrid(np.linspace(0, 1, scale), np.linspace(0, 1, scale))
    l1 = ((y2-y3)*(x-x3)+(x3-x2)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3));
    l2 = ((y3-y1)*(x-x3)+(x1-x3)*(y-y3))/((y2-y3)*(x1-x3)+(x3-x2)*(y1-y3));
    return x, y, (1-l1-l2)

x, y, z = PHI1()
ax.plot_surface(x, y, z, color='b', alpha=0.7)
x, y, z = PHI2()
ax.plot_surface(x, y, z, color='g', alpha=0.7)

x, y, z = PHI3()
ax.plot_surface(x, y, z, color='r', alpha=0.7)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_zlim(0, 1)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
