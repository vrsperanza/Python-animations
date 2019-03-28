
import noise
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


numframes = 100
numpoints = 10
color_data = np.random.random((numframes, numpoints))
x, y, c = np.random.random((3, numpoints))

fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
mat, = ax.plot(x, y, 'o')

def animate(i):
    X = []
    Y = []
    for j in range(numpoints):
        x = np.cos(2*np.pi*i/numframes + j * 2*np.pi/numpoints)
        y = np.sin(j * 2*np.pi/numpoints)
        
        X.append(x)
        Y.append(y)
    mat.set_data(X, Y)
    return mat,

anim = animation.FuncAnimation(fig, animate, frames=numframes, interval=1, blit=True)
plt.show()