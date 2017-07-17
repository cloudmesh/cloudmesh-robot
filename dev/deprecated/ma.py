import requests
import time
from marvelmind import MarvelmindHedge

# TO BE RUN WITH NEWCAR4 ON CAR

def set_line(x0, y0, fx, fy):
    slope = (fy - y0) / (fx - x0)
    intercept = y0 - (x0 * slope)
    return slope, intercept

class DrivingRobot(object):

    def __init__(self, number, ip, final_x, final_y, alpha=45, epsilon=4):
        self.number = number
        self.ip = ip
        self.alpha = alpha
        self.epsilon = epsilon
        self.going_left = True
        self.going_right = True
        self.on_track = 0
        self.fx = final_x
        self.fy = final_y
        self.done = False

    def robot_start(self):
        self.addr, self.x0, self.y0, self.z0, self.t0 = hedgeswarm.number_position(self.number)
        self.m, self.b = set_line(self.x0, self.y0, self.fx, self.fy)

    def xexp(self, y):
        ex = (y - self.b) / self.m
        return ex

    def move(self, direction, value=None):

        if direction == "turn":
            payload = {'TURN': str(value)}
        elif direction == "forward":
            payload = {'FORWARD': str(value)}
        elif direction == "stop":
            payload = {'STOP': 'ON'}
        elif direction == "backward":
            payload = {'BACKWARD': 'ON'}
        else:
            print ("ERROR: unknown direction:", direction)

        try:
            headers = {'User-Agent': "Car"}
            r = requests.get('http://' + self.ip, headers=headers, params=payload)
        except Exception as e:
            print(type(e), e)

    def turn(self):
        a, cx, cy, cz, ct = hedgeswarm.number_position(self.number)
        ex = self.xexp(cy)
        if abs(cx - self.fx) < self.epsilon and abs(cy - self.fy) < self.epsilon:
            self.done = True
        if (cx - ex) < - self.epsilon:
            if self.going_left:
                self.move('turn', self.alpha)
                self.going_left = True
                self.going_right = False
                self.on_track += 1
                if self.on_track > 2:
                    self.alpha -= 5
            elif not self.going_left:
                self.alpha += 10
                self.move('turn', self.alpha)
                self.on_track = 0
        elif (cx - ex) > self.epsilon:
            if self.going_right:
                self.move('turn', - self.alpha)
                self.going_left = False
                self.going_right = True
                self.on_track += 1
                if self.on_track > 2:
                    self.alpha -= 5
            elif not self.going_right:
                self.alpha += 10
                self.move('turn', self.alpha)
                self.on_track = 0
        time.sleep(.2)

    def run(self):
        while not self.done:
            self.move('forward', 1)
            time.sleep(.2)
            self.turn()

def make_robot(robot):
    name, position = robot.split(":")
    number, ip = name.split(" ")
    endx, endy = position.split(",")
    return number, ip, endx, endy

filename = "ma.txt"
f = open(filename)
lines = f.readlines()
f.close()

robot_list = []
for line in lines:
    n, ip, ex, ey = make_robot(line)
    robot_list.append(DrivingRobot(n, ip, ex, ey))
print(robot_list)

hedgeswarm = MarvelmindHedge(tty='/dev/tty.usbmodem1421')






