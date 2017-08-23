import math
import requests
from marvelmind import MarvelmindHedge
import time


class Robot(object):

    def __init__(self, number, ip, endx, endy):
        self.number = int(number)
        self.ip = str(ip)
        self.endx = int(endx)
        self.endy = int(endy)
        self.line = []
        self.done = False

    def move(self, direction, value=None):
        """
        sends move commands to server
        :param direction: String
        :param value: None or String
        """
        if direction == "stop":
            payload = {'STOP': 'ON'}
        elif direction == 'forward':
            payload = {'FORWARD': str(value)}
        elif direction == "set":
            payload = {'SET': value}
        else:
            print ("ERROR: unknown direction:", direction)

        try:
            headers = {'User-Agent': "Car"}
            r = requests.get('http://' + self.ip, headers=headers, params=payload)
        except Exception as e:
            print(type(e), e)

    def check_done(self, positions):
        if self.done:
            pass
        else:
            x = positions[self.number][0]
            y = positions[self.number][1]
            if abs(x - self.endx) < 20 and abs(y - self.endy) < 20:
                self.done = True
                self.move('stop')


    def distance(self, positions):
        x = positions[self.number][0]
        y = positions[self.number][1]
        num = abs((self.line[0] * x) + (self.line[1] * y) + self.line[2])
        denom = math.sqrt((self.line[0] ** 2) + (self.line[1] ** 2))
        d = num / denom
        return d

    def line_side(self, positions):
        x = positions[self.number][0]
        y = positions[self.number][1]
        yexp = (x * self.line[3]) + self.line[4]
        if y >= yexp:
            if self.line[4] > 0:
                return "left"
            else:
                return "right"
        else:
            if self.line[4] > 0:
                return "right"
            else:
                return "left"

    def run(self, positions):
        self.check_done(positions)
        if not self.done:
            side = self.line_side(positions)
            d = self.distance(positions)
            if d > 20:
                if side == "left":
                    magnitude = -1
                elif side == "right":
                    magnitude = 1
            else:
                if side == "left":
                    magnitude = 0 - (d / 20)
                elif side == "right":
                    magnitude = d / 20  # change maximum off line distance here
            offset = magnitude * 150
            left_duty = 870 - offset
            right_duty = 870 + offset
            self.move('set', str(left_duty) + '-' + str(right_duty))
        else:
            pass


class RobotSwarm(object):

    def __init__(self, file):
        self.file = file
        self.robots = []

        ###################
        #   Make Robots   #
        ###################
        f = open(self.file)
        lines = f.readlines()
        f.close()
        for line in lines:
            name, position = line.split(":")
            number, ip = name.split(" ")
            endx, endy = position.split(",")
            print(number, ip, endx, endy)
            self.robots.append(Robot(number, ip, endx, endy))
        ###################
        #   Robots Made   #
        ###################

        self.robot_numbers = []  # List of robot marvelmind hedge numbers
        for robot in self.robots:
            self.robot_numbers.append(robot.number)
        self.moving_robots = self.robot_numbers
        self.done = False

    def get_positions(self):
        """
        finds positions of all robots with optimal speed
        :return: Dictionary
        """
        print('get positions')
        positions = hedge.list_positions(self.moving_robots)
        return positions

    def start(self):
        print('swarm start')
        positions = self.get_positions()
        for robot in self.robots:
            x = positions[robot.number][0]
            y = positions[robot.number][1]
            m = ((robot.endy - y) / (robot.endx - x))
            b = robot.endy - (m * robot.endx)
            a = 0 - m
            b = 1
            c = (m * robot.endx) - robot.endy
            robot.line = [a, b, c, m, b]

    def check_done(self):
        print('check done')
        for robot in self.robots:
            if robot.done:
                self.done = True
            else:
                self.done = False
                break

    def go(self):
        print('go')
        positions = self.get_positions()
        for robot in self.robots:
            robot.run(positions)

    def run(self):
        self.start()
        t0 = time.time()
        while not self.done:
            t = time.time() - t0
            print('run:', str(t))
            self.go()
            self.check_done()
        print('done')



hedge = MarvelmindHedge(tty='/dev/tty.usbmodem1421')
hedge.start()
time.sleep(2)

