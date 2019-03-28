
import noise
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


numframes = 1000
numpoints = 50
color_data = np.random.random((numframes, numpoints))
x, y, c = np.random.random((3, numpoints))

fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
mat, = ax.plot(x, y, 'o')

def animate(i):
    X = [-2]
    Y = [-2+4*i/numframes]
    for j in range(numpoints):
        x = np.cos(2*np.pi*i/numframes + j * 2*np.pi/numpoints) \
            + noise.pnoise3(np.cos(2*np.pi*i/numframes), 2*numframes*j + np.cos(i/numframes * 2 * np.pi), 2*numframes*j + np.sin(i/numframes * 2 * np.pi))
        y = np.sin(2*np.pi*i/numframes + j * 2*np.pi/numpoints) \
            + noise.pnoise3(np.sin(2*np.pi*i/numframes), -2*numframes*j - np.cos(i/numframes * 2 * np.pi), -2*numframes*j - np.sin(i/numframes * 2 * np.pi))
        
        X.append(x)
        Y.append(y)
    mat.set_data(X, Y)
    return mat,

anim = animation.FuncAnimation(fig, animate, frames=numframes, interval=20, blit=True)
plt.show()