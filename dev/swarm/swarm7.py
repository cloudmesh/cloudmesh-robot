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
        self.last_position = []
        self.last_angle = None
        self.done = False

    def distance_to_go(self, positions):
        x = positions[self.number][0]
        y = positions[self.number][1]
        d = math.sqrt(((x - self.endx) ** 2) + ((y - self.endy) ** 2))
        return d

    def find_vectors(self, positions):
        """
        finds the vectors that connect three points
        :param last_x: Number
        :param last_y: Number
        :param current_x: Number
        :param current_y: Number
        :param end_x: Number
        :param end_y: Number
        :return: List, List
        """
        current_x = positions[self.number][0]
        current_y = positions[self.number][1]
        last_x = self.last_position[0]
        last_y = self.last_position[1]
        end_x = self.endx
        end_y = self.endy
        v1 = [(current_x - last_x), (current_y - last_y)]
        v2 = [(end_x - current_x), (end_y - current_y)]
        return v1, v2

    def find_angle(self, x, y):
        """
        finds angle from the origin
        :param x: Number
        :param y: Number
        :return: Number
        """
        if x > 0:
            if y >= 0:
                return math.degrees(math.atan(y / x))
            elif y < 0:
                return 360 + math.degrees(math.atan(y / x))
        elif x < 0:
            return 180 + math.degrees(math.atan(y / x))
        elif x == 0:
            if y > 0:
                return 90
            elif y < 0:
                return 270

    def find_delta(self, v1, v2):
        """
        finds the angle between two vectors
        :param v1: List
        :param v2: List
        :return: Number
        """
        unit_factor1 = math.sqrt((v1[0] ** 2) + (v1[1] ** 2))
        unit_factor2 = math.sqrt((v2[0] ** 2) + (v2[1] ** 2))
        u1 = [(v1[0] / unit_factor1), (v1[1] / unit_factor1)]
        u2 = [(v2[0] / unit_factor2), (v2[1] / unit_factor2)]
        return math.degrees(math.acos((u1[0] * u2[0]) + (u1[1] * u2[1])))

    def turn_direction(self, angle1, angle2):
        """
        returns the direction that the robot must turn
        :param angle1: Number
        :param angle2: Number
        :return: String
        """
        if abs(angle2 - angle1) < 180:
            if angle2 < angle1:
                return "right"
            elif angle1 < angle2:
                return "left"
        else:
            if angle1 > angle2:
                return "left"
            elif angle2 > angle1:
                return "right"

    def align(self, positions):
        """
        turns robot in direction of final position
        :param positions: Dictionary
        :return: None
        """
        cx = positions[self.number][0]
        cy = positions[self.number][1]
        last_x = self.last_position[0]
        last_y = self.last_position[1]
        print('current position: ')
        print(cx, cy)
        print('last position: ')
        print(last_x, last_y)
        v1, v2 = self.find_vectors(positions)  # get vector positions
        delta_angle = int(self.find_delta(v1, v2))  # get angle change
        print('angle change: ')
        print(delta_angle)
        angle1 = int(self.find_angle(v1[0], v1[1]))  # get unit vector angles
        angle2 = int(self.find_angle(v2[0], v2[1]))
        print('absolute angles: ')
        print(angle1, angle2)
        direction = self.turn_direction(angle1, angle2)  # get turn direction
        if delta_angle > 10:
            print(direction)
            self.last_angle = angle2
            self.move(direction, delta_angle)  # turn robot
        else:
            print('on track')
            self.last_angle = angle1

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
            print('sending payload:', str({'SET': value}))
            payload = {'SET': value}
            print('payload sent')
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
            d = math.sqrt(((self.endx - x) ** 2) + ((self.endy - y) ** 2))
            if d < 30:
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

    def go_far(self, positions):
        max = 15
        print('robot not done')
        side = self.line_side(positions)
        print('side', side)
        d = self.distance(positions)
        print('distance:', str(d))
        if d > max:
            if side == "left":
                magnitude = -1
            elif side == "right":
                magnitude = 1
        else:
            if side == "left":
                magnitude = 0 - (d / max)
            elif side == "right":
                magnitude = d / max  # change maximum off line distance here
        offset = magnitude * 150
        left_duty = int(870 - offset)
        right_duty = int(870 + offset)
        print('left_duty:', str(left_duty))
        print('right_duty:', str(right_duty))
        self.move('set', str(right_duty) + '-' + str(left_duty))
        self.last_position = positions[self.number]

    def go_close(self, positions):
        self.align(positions)


    def run(self, positions):
        self.check_done(positions)
        d = self.distance_to_go(positions)
        if not self.done:
            # if far self.go_far(positions)
            # if close self.go_close(positions)
        else:
            pass


class RobotSwarm(object):

    def __init__(self, file):
        print('building')
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
            endy = endy.rstrip()
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
        print('built')

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
            A = 0 - m
            B = 1
            C = 0 - b
            robot.line = [A, B, C, m, b]
            print(str(robot.line))

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
        print('positions:', str(positions))
        for robot in self.robots:
            print('robot: ', str(robot.number))
            robot.run(positions)

    def pre_start(self):
        print('aligning robots')
        positions = self.get_positions()
        for robot in self.robots:
            robot.last_position = positions[robot.number]
            robot.move('forward', "0.3")
        positions = self.get_positions()
        for robot in self.robots:
            robot.align(positions)

    def run(self):
        self.pre_start()
        self.start()
        t0 = time.time()
        while not self.done:
            t = time.time() - t0
            print('time:', str(t))
            self.go()
            self.check_done()
        print('done')



hedge = MarvelmindHedge(tty='/dev/tty.usbmodem1421')
hedge.start()
time.sleep(2)
swarm = RobotSwarm('swarm.txt')
swarm.run()