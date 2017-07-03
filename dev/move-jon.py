import time
import requests
import os
from marvelmind import MarvelmindHedge

"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


def move(ip, direction):
    if direction == 'left':
        payload = {'LEFT': 'ON'}
    elif direction == 'right':
        payload = {'RIGHT': 'ON'}
    elif direction == 'stop':
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


filename = "moveto.txt"
f = open(filename)
lines = f.readlines()
f.close()

print ("LINES", lines)
fx = 100  # FINAL
fy = 100  # POSITION
finalerror = 10

robot = MarvelmindHedge(tty='/dev/tty.usbmodemFD121')
ip = "10.0.1.118"
curdirection = 'STOP'
robot.start()
addr0, x0, y0, z0, t0 = robot.position()


# Ideal Line
m = (fy - y0) / (fx - x0)
b = y0 - (x0 * m)


alpha = .1
epsilon = 4
going_left = True
going_right = True
on_track = 0

while True:
    print (robot.position())
    time.sleep(0.5)
    robot.print_position()
    addr, cx, cy, cz, ts = robot.position()
    dx, dy = fx - cx, fy - cy
    ex = (cy - b) / m
    displacement = cx - ex

    if abs(dx) < finalerror and abs(dy) < finalerror:
        robot.stop()
        break

    elif displacement < - epsilon:
        if going_left:
            if on_track == 0:
                on_track += 1
            elif on_track == 1:
                on_track += 1
            else:
                alpha -= .05
            move(ip, "right")
            going_left = False
            going_right = True
            time.sleep(alpha)
            move(ip, "forward")
        elif going_right:
            on_track = 0
            move(ip, "right")
            alpha += .1
            time.sleep(alpha)
            move(ip, "forward")

    elif displacement > epsilon:
        if going_right:
            if on_track == 0:
                on_track += 1
            elif on_track == 1:
                on_track += 1
            else:
                alpha -= .05
            move(ip, "left")
            going_left = True
            going_right = False
            time.sleep(alpha)
            move(ip, "forward")
        elif going_left:
            on_track = 0
            move(ip, "left")
            alpha += .1
            time.sleep(alpha)
            move(ip, "forward")

    time.sleep(.3)


#    if abs(dx) >= epsilon:
#        if dx > 0:
#            if curdirection == 'XP':
                # move forward
#                move(ip, "forward")
#                time.sleep(0.2)
#                move(ip, "stop")
#    elif abs(dy) >= epsilon:
#        if dy > 0:
#            if curdirection == 'YP':
                # move forwrad
#                move(ip, "forward")
#                time.sleep(0.2)
#                move(ip, "stop")
#            elif curdirection == 'XP':
                # left turn 90 degree once
#                move(ip, "left")
#                time.sleep(0.5)
#                move(ip, "stop")
#                curdirection = 'YP'

#    else:
#        assert abs(dx) < epsilon and abs(dy) < epsilon
#        robot.stop()
#        break