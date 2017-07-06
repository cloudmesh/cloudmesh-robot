from marvelmind import MarvelmindHedge
from time import sleep
import matplotlib.pyplot as plt
import sys
import numpy
from threading import Thread

n = [0] * 9
x = [0.0] * 9
y = [0.0] * 9
z = [0.0] * 9
for i in range (0,len(n)):
  n[i] = i+1


print ("III",n)

# sys.exit(1)

def update_position():

    plt.scatter(x,y)
    for i, txt in enumerate(n):
       plt.annotate(txt, (x[i-1],y[i-1]))
    plt.draw()    

def update_line():

    xdata = numpy.append(plt.gca().lines[0].get_xdata(), plt.gca().lines[1].get_xdata())
    ydata = numpy.append(plt.gca().lines[0].get_ydata(), plt.gca().lines[1].get_ydata())

    pos = hedge.position()
    new_x = pos[1]
    new_y = pos[2]
    plt.gca().lines[0].set_xdata(xdata[-29:])
    plt.gca().lines[0].set_ydata(ydata[-29:])
    
    plt.gca().lines[1].set_xdata([new_x])
    plt.gca().lines[1].set_ydata([new_y])
    
    plt.draw()    


def printThread():
    while True:
        try:
            sleep(3)
            pos = hedge.position()
            print (pos) # get last position and print
            name = pos[0] 
            x[name-1] = pos[1] 
            y[name-1] = pos[2] 
            z[name-1] = pos[3] 
            
        except KeyboardInterrupt:
            hedge.stop()  # stop and close serial port
            sys.exit()


def main():
    
    #create plot
    global fig
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot([],[], 'ro')
    ax.grid(True)
    bx = fig.add_subplot(111)
    bx.plot([],[], 'bo')
    plt.axis('equal')
    axes = plt.gca()
    axes.set_xlim([-500,500])
    axes.set_ylim([-500,500])
    
    global hedge
    hedge = MarvelmindHedge(tty = "/dev/tty.usbmodem1411", 
                            recieveDataCallback=update_position) 
    # create MarvelmindHedge thread
    hedge.start()
    
    plotThread = Thread(target=printThread) # create and start console out thread
    plotThread.start()
    
    plt.show()
    
main()
