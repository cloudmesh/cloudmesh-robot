import time
import requests
import os
from marvelmind import MarvelmindHedge
import cm
"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


def cm.move(ip, direction, epsilon=0.0001):
    if direction == 'left':
        payload = {'LEFT': 'ON'}
    elif direction == 'right':
        payload = {'RIGHT': 'ON'}
    elif  direction == 'stop':
        payload = {'STOP': 'ON'}
    elif direction == 'forward':
        payload = {'FORWARD': 'ON'}
    elif direction == 'backward':
        payload = {'BACK': 'ON'}
    else:
        print ("ERROR: unkown direction:", direction)
    try:
        headers = {'User-Agent': "Car"}
        r = requests.get('http://' + ip, headers=headers, params=payload)
    except Exception as e:
        print (type(e), e)



        
    """
    Param:
    =====

    robot: instance of marvelmind.MarvelmindHedge"
    x: float: x-coordinate of target
    y: float: y-coordinate of target
    epsilon: float: threshold for distance to target
    """

#filename="move.txt"
#f = open(filename)
#lines = f.readlines()
#f.close()


#print ("LINES", lines)


x = #destination
y =
epsilon = 2

robot = MarvelmindHedge(tty='/dev/tty.usbmodemFD121')
ip = "10.0.1.115"
curdirection = 'XP' #current direction


def moveto(x,y):

    given position x y move to that position 
    x0,y0 = get durrent pos
    x1,x2 = x, y

    .....

def closeto(x,y, r):
    return diatsnace(x,y) <= r:


def distance(x,y):

    given x,y and my current position, how far away am i from x y

    use eucledian disatance e.g. pytagoras
    





adO, xO, yO, zO, tO = robot.position() # initial position
m = (y - y0) / (x - x0) #slope of the ideal line
print(m)
b = y0 - (m * x0) #y intercept of the ideal line
print(b)

ex = (cy - b) / m   #expected x value based on current y
alpha = 45 #initial angle of correction
dx, dy = x - cx, y - cy #distance between current position and final position

goingright = True
goingleft = True

robot.start()

while True:
        print (robot.position())
        Go forward
        time.sleep(0.5)
        print (robot. position)
        addr, cx, cy, cz, ts = robot.position() #current robot position
        if (cx-ex) < -epsilon and goingleft = True
            turn RIGHT alpha #robot going too far left
            print (robot.position())
            go forward
            time.sleep(0.5)
            goingleft = False #robot now faces right
            goingright = True
            robot.stop()
            
        print (robot.position())
        addr, cx, cy, cz, ts = robot.position() #current robot position
        if (cx-ex) < -epsilon and goingright = True
            turn RIGHT alpha #robot going too far left
            print (robot.position())
            go forward
            time.sleep(0.5)
            goingleft = False #robot now faces right
            goingright = True
            robot.stop()

        print (robot.position())
        addr, cx, cy, cz, ts = robot.position() #current robot position
        if (cx-ex) > epsilon and goingleft = True
            turn LEFT alpha #robot going too far right
            print (robot.position())
            go forward
            time.sleep(0.5)
            goingleft = True #robot now faces left
            goingright = False
            robot.stop()
            
        print (robot.position())
        addr, cx, cy, cz, ts = robot.position() #current robot position
        if (cx-ex) > epsilon and goingright = True
            turn LEFT alpha #robot going too far right
            print (robot.position())
            go forward
            time.sleep(0.5)
            goingleft = True #robot now faces left
            goingright = False
            robot.stop()



        
        else:
            assert abs(cx-x) > -epsilon and (xc-x) < epsilon #am I in this box?
            assert (yc - y) >-epsilon and (yc-y) < epsilon
            robot.stop()
            break
