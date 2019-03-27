"""
A simple example of an animated plot
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

#xar = [0]*10

t = np.arange(0, 6, 0.1)

s0 = np.sin(t)
s1 = np.sin(2*t)


def animate(i):
    
    t = t[1:]
    t = np.append(t, t[-1]+0.1)
    s0 = np.sin(t)
    s1 = np.sin(2*t)
    
    plt.plot(t, s0, t, s1)
    #xar.append(10*np.random.rand(1)[0])
    #ax1.clear()
    #ax1.plot(xar)
    del xar[0]
    
    
ani = animation.FuncAnimation(fig, animate, interval=2)
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
plt.show()
