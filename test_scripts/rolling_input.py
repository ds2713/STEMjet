import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

xar = [1,2,3,4,5]

print(plt.get_backend())

def animate(i):
    xar.append(input())
    ax1.clear()
    ax1.plot(xar)
    ax1.set_ylim([0,10])
    del xar[0]
    
ani = animation.FuncAnimation(fig, animate, interval=10)
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
plt.show()
