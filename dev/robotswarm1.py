import time

import requests

from dev.swarm.swarm import MarvelmindHedge

"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


def move(ip, direction, epsilon=0.0001):
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


x = 500 #destination
y = 500
epsilon = 5

robot = MarvelmindHedge(tty='/dev/tty.usbmodemFD121')
ip = "10.0.1.115"
curdirection = 'XP' #current direction

ad0, x0, y0, z0, t0 = robot.position() # initial position
m = (y - y0) / (x - x0) #slope of the ideal line
print(m)
b = y0 - (m * x0) #y intercept of the ideal line
print(b)
alpha = 90 #initial angle of correction
goingright = True
goingleft = True

robot.start()

while True:
        print (robot.position())
        time.sleep(0.5)
        robot.print_position()
        addr, cx, cy, cz, ts = robot.position() #current robot position
        dx, dy = x - cx, y - cy #distance between current position and final position
        x-exp = (cy - b) / m   #expected x value based on current y



        
        else:
            assert abs(dx) < epsilon and abs(dy) < epsilon
            robot.stop()
            break
