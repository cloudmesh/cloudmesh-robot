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

x = 100
y = 100
epsilon = 10

robot = MarvelmindHedge(tty='/dev/tty.usbmodemFD121')
ip = "10.0.1.118"
curdirection = 'XP'
robot.start()
while True:
    print (robot.position())
    time.sleep(0.5)
    robot.print_position()
    addr, cx, cy, cz, ts = robot.position()
    dx, dy = x - cx, y - cy

    # assume motion is horizontal or vertical only
    if abs(dx) >= epsilon:
        if dx > 0:
            if curdirection == 'XP':
                # move forward
                move(ip, "forward")
                time.sleep(0.2)
                move(ip, "stop")
    elif abs(dy) >= epsilon:
        if dy > 0:
            if curdirection == 'YP':
                # move forwrad
                move(ip, "forward")
                time.sleep(0.2)
                move(ip, "stop")
            elif curdirection == 'XP':
                # left turn 90 degree once
                move(ip, "left")
                time.sleep(0.5)
                move(ip, "stop")
                curdirection = 'YP'

    else:
        assert abs(dx) < epsilon and abs(dy) < epsilon
        robot.stop()
        break


