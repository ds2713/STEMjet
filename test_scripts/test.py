import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

t = np.arange(0,3,0.1)

def updateValues(t):
    t = np.append(t, t[-1]+0.1)
    t = t[1:]
    s0 = np.sin(t*np.pi)
    return t, s0

ani = animation.FuncAnimation(fig, updateValues, t, interval=10)

plt.show()
