from math import sqrt
from marvelmind import MarvelmindHedge

import time
port = "/dev/tty.usbmodem1451"



hedge = MarvelmindHedge(port)
hedge.start()
time.sleep(2)
print ("starting")


dmin = 700
dmax = 1023
dd = dmax - dmin
base_speed = 800

#100 - rm faster + base speed
#- 100 lm faster + base speed


def duty_offset(distance):
    global base_speed
    offset = distance * 10
    return base_speed + offset

right = base_speed
left = base_speed



def distance (x1,y1, x2, y2, x0, y0):
    return round(((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / sqrt ((y2-y1)**2+(x2-x1)**2), 2)


#def distance (x1,y1, x2, y2, x0, y0):
#    return round(abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1) / sqrt ((y2-y1)**2+(x2-x1)**2),2)

def get_pos ():
    # query marvelmind and get position if no position is avilable wait till you get one
    global hedge
    addr, x, y, z, t = hedge.number_position(4)
    x = round(x, 2)
    y = round(y, 2)
    return x, y


x1, y1 = get_pos()
x2 = 100
y2 = 100

while True:
    x0, y0 = get_pos()
    d = distance(x1, y1, x2, y2, x0, y0)
    o = duty_offset(d)
    if d > 0:
        speed_r = base_speed
        speed_l = o

    elif d < 0:
        speed_r = o
        speed_l = base_speed

    elif d == 0:
        speed_l = base_speed
        speed_r = base_speed


    print (x1, y1, x2, y2, x0, y0)
    print (d, o, speed_l, speed_r)

    time.sleep(0.1)
