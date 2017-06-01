import time
import requests
import os
"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


def move(ip, direction, x, y, epsilon=0.0001):
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

    while True:
        cx, cy = robot.position()
        dx, dy = x - cx, y - cy

        # assume motion is horizontal or vertical only
        if abs(dx) >= epsilon
            # move left/right
            for ip in ips:
                move(ip, direction)
            time.sleep(duration)
            for ip in ips:
                move(ip, "stop")
            pass

        elif abs(dy) >= epsilon:
            # move up/down
            for ip in ips:
                move(ip, direction)
            time.sleep(duration)
            for ip in ips:
            move(ip, "stop")
            pass
        else:
            assert abs(dx) < epsilon and abs(dy) < epsilon
            robot.stop()
            break
