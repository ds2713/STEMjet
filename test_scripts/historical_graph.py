import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#configure drawing
fig = plt.figure()
throttleGraph = fig.add_subplot(1,1,1)

#initialise data arrays
throttleDemand = np.array([0,2,4,3,1])
xdata = [0,0,0,0,0]

#function called at every interval
def animate(throttleDemand):
	#get the next value for throttleDemand
    xdata.append(throttleDemand)
    #clear the display
    throttleGraph.clear()
    #plot the array
    throttleGraph.plot(xdata)
    #set the y axis limits
    throttleGraph.set_ylim([0,10])
    #ensure the data array has only five entries
    if len(xdata)>5:
        del xdata[:1]
        
#animate function arguments: (figure to draw, function to call at each interval, argument, interval in ms)
ani = animation.FuncAnimation(fig, animate, throttleDemand, interval=100)

#show plot
plt.show()
