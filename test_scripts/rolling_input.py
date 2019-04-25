import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
from numpy import array, roll

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xar = array([1,2,3,4,5])

print(plt.get_backend())

def animate(xar):
    
    xar = roll(xar,1)
    ax1.clear()
    ax1.plot(xar)
    ax1.set_ylim([0,10])
    
ani = animation.FuncAnimation(fig, animate, interval=10)
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
plt.show()
