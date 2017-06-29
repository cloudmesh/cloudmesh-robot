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



class PositioningSystem(object):

    def __init___(tty="/dev/...????"):
        pass

    def register (addr, name, kind='mobile'):
        self.beacon{
            'name' = name,
            'kind' = kind,
            'addr' = addr,
            }

    def lookup(addr):
        for i in self.beacon:
            if self.beacon[i][addr] == addr:
                return self.beacon[i]
        return None
            
    def get(name=None):
        if id is None:
            d = get all positions and put in dict or array not sure what works, you are expert
            return d
        else
            d = get all positions and put in dict or array not sure what works, you are expert
            return d[id]

    def reset():
        # set all positions to some vale within the fixedbecona
        pass

    def info(self, kind='mobile'):
        mobile, all, stationarty

        dependent on type returns info about the beacons
        not sure how to implement yet

    def count(self, type= ....)
        retusn number of beacons found


    def set_count(stationary, mobile)
        instead of probing the beacons hard code the set count
        so we can figure out if we have power isse

    def probe (id):
        similar to get but with more info get just gives xy
        
        


class RobotXY(object):

    
    def __init__(self, epsilon=2):
        # espilon ???
        self.epsilon = epsilon
        
    def to(self, x,y):
        """
        given position x y move to that position 
        x0,y0 = get durrent pos
        x1,x2 = x, y
        """
        pass


    def near(self, x,y, r):
        return diatsnace(x,y) <= r:


    def distance(self, x,y):
        """
        given x,y and my current position, how far away am i from x y

        use eucledian disatance e.g. pytagoras
        """

robot = RobotXY()

# x, y , rin cm
x = 10.0
y = 10.0
r = 2.0
robot.to(x,y)

if robot.neat (x, y, r):
    print ("YUHU IM THERE")



positons = PositionoingSystem()

positions.register("Hedge #15", "robi15")


x,y = positions.get("robi15")

    
### integrate whatever maces sense in the above.    



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

while robot.distance() > epsilon:
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
