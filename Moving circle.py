
import noise
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

plt.style.use('dark_background')

frames = 200
fig = plt.figure()
ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    angle = np.linspace(0, 2*np.pi, 1000)
    x = np.cos(angle) + noise.pnoise2(np.cos(i/frames * 2 * np.pi), np.sin(i/frames * 2 * np.pi))
    y = np.sin(angle) + noise.pnoise2(np.cos(i/frames * 2 * np.pi) + 1000, np.sin(i/frames * 2 * np.pi) + 1000)
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=frames, interval=1, blit=True)
plt.show()