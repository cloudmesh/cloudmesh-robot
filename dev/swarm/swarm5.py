import math
import requests
from marvelmind import MarvelmindHedge
import time


class Robot(object):

    def __init__(self, number, ip, final_x, final_y, epsilon=10, last_angle=90):
        self.number = int(number)
        self.ip = str(ip)
        self.fx = int(final_x)
        self.fy = int(final_y)
        self.epsilon = int(epsilon)
        self.addr, self.last_x, self.last_y, self.last_z, self.last_t = hedge.number_position(self.number)
        self.cx, self.cy = self.last_x, self.last_y
        self.done = False
        self.mode = "far"
        self.last_angle = int(last_angle)
        self.turn_mode = True
        self.A = None
        self.B = None
        self.C = None
        self.m = None
        self.b = None

    def update(self, positions):
        """
        finds robot position in a dictionary of marvelmind hedge positions
        :param positions: Dictionary
        :return: None
        """
        self.last_x = self.cx
        self.last_y = self.cy
        self.cx = positions[self.number][0]
        self.cy = positions[self.number][1]
        if self.mode == "far":
            if math.sqrt(((self.fx - self.cx) ** 2) + (self.fy - self.cy) ** 2) < 50:
                self.mode = "close"
            else:
                pass
        else:
            pass

    def find_vectors(self, last_x, last_y, current_x, current_y, end_x, end_y):
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

    def move(self, direction, value=None):
        """
        sends move commands to server
        :param direction: String
        :param value: None or Number
        """
        if direction == "right":
            print('turning right')
            print(value)
            payload = {'TURN': str(-value)}
        elif direction == "left":
            print('turning left')
            print(value)
            payload = {'TURN': str(value)}
        elif direction == "forward":
            payload = {'FORWARD': str(value)}
        elif direction == "stop":
            payload = {'STOP': 'ON'}
        elif direction == "backward":
            payload = {'BACKWARD': 'ON'}
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
        cx = positions[self.number][0]
        cy = positions[self.number][1]
        if abs(cx - self.fx) < self.epsilon and abs(cy - self.fy) < self.epsilon:
            self.done = True

    def turn(self, positions):
        """
        turns robot in direction of final position
        :param positions: Dictionary
        :return: None
        """
        print('current position: ')
        print(self.cx, self.cy)
        print('last position: ')
        print(self.last_x, self.last_y)
        v1, v2 = self.find_vectors(self.last_x, self.last_y, self.cx, self.cy, self.fx, self.fy)  # get vector positions
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

    def when_done(self):
        """
        turns robot perpendicular to x axis
        :return: None
        """
        print('done?', self.done)
        print('final turn')
        v1, v2 = self.find_vectors(self.last_x, self.last_y, self.cx, self.cy, self.cx, 0)
        delta_angle = int(self.find_delta(v1, v2))
        angle1 = int(self.find_angle(v1[0], v1[1]))  # get unit vector angles
        angle2 = int(self.find_angle(v2[0], v2[1]))
        print(angle1, angle2)
        direction = self.turn_direction(angle1, angle2)
        self.move(direction, delta_angle)

    def go(self):
        """

        :return:
        """
        if not self.done:
            distance = int(math.sqrt(((self.cx - self.fx) ** 2) + ((self.cy - self.fy) ** 2)))
            if distance > 50:
                self.move('forward', 1)
            elif 20 <= distance <= 50:
                self.move('forward', .5)
            elif distance < 20:
                self.move('forward', .3)

    def first_step(self):
        """
        steps a robot forward and orients it toward final destination
        :return: None
        """
        self.move('forward', .5)

    def move_close(self, positions):
        """
        moves robot in small bursts
        :param positions: Dictionary
        :return: None
        """
        if abs(self.fx - self.cx) < 10 and abs(self.fy - self.cy) < 10:
            self.done = True
        else:
            if self.turn_mode:
                self.turn_mode = False
                self.turn(positions)
            else:
                self.turn_mode = True
                self.move('forward', .4)

    def set_line(self):
        """
        sets a line from current position to end position
        :return: None
        """
        self.m = ((self.fy - self.cy) / (self.fx - self.cx))
        self.b = self.fy - (self.m * self.fx)
        self.A = 0 - self.m
        self.B = 1
        self.C = (self.m * self.fx) - self.fy

    def line_distance(self):
        """
        finds distance between current position and ideal line
        :return: Number
        """
        d = (abs(((0 - self.m) * self.cx) + self.cy + (self.m * self.fx) - self.fy) / math.sqrt((self.m ** 2) + 1))
        return d

    def line_side(self):
        """
        finds whether the robot is to the left or right of ideal line
        :return: String
        """
        yexp = (self.cx * self.m) + self.b
        if self.cy > yexp:
            if self.m > 0:
                return "left"
            else:
                return "right"
        else:
            if self.m > 0:
                return "right"
            else:
                return "left"

    def move_far(self, positions):
        """
        moves robot continuously
        :param positions: Dictionary
        :return: None
        """
        side = self.line_side()
        d = self.line_distance()
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
        self.move('set', str(left_duty) + ':' + str(right_duty))

    def run(self, positions):
        """
        moves robot in accordance with current and final positions
        :param positions: Dictionary
        :return: None
        """
        if self.done:
            pass
        elif self.mode == "far":
            self.update(positions)
            self.move_far(positions)
        else:
            self.update(positions)
            self.move_close(positions)



class RobotSwarm(object):

    def __init__(self, file):
        """
        creates a swarm of robots connected to Marvelmind
        :param file: String
        """
        self.file = file  # File containing robot information
        self.done = False  # Are all robots in final positions
        self.robots = []  # List of swarm robots
        filename = self.file
        f = open(filename)
        lines = f.readlines()
        f.close()
        for line in lines:
            name, position = line.split(":")
            number, ip = name.split(" ")
            endx, endy = position.split(",")
            print(number, ip, endx, endy)
            self.robots.append(Robot(number, ip, endx, endy))
        self.hedge_numbers = []  # List of robot marvelmind hedge numbers
        for robot in self.robots:
            self.hedge_numbers.append(robot.number)
        self.moving_hedge_numbers = self.hedge_numbers

    def check_done(self):
        """
        checks the values of self.done for each robot in the swarm
        :return: Boolean
        """
        for robot in self.robots:
            if not robot.done:
                self.done = False
                break
            else:
                self.done = True
                try:
                    self.moving_hedge_numbers.remove(robot.number)
                except ValueError:
                    continue

    def get_positions(self):
        """
        finds positions of all robots with optimal speed
        :return: Dictionary
        """
        positions = hedge.list_positions(self.moving_hedge_numbers)
        return positions

    def update_robots(self):
        """
        updates robots with current positions
        :return: None
        """
        positions = self.get_positions()
        for robot in self.robots:
            robot.update(positions)

    def start(self):
        """
        starts robots, turns toward end positions, finds ideal lines
        :return: None
        """
        for robot in self.robots:
            robot.first_step()
        time.sleep(.5)
        positions = self.get_positions()
        for robot in self.robots:
            robot.update(positions)
        for robot in self.robots:
            robot.turn(positions)
        for robot in self.robots:
            robot.set_line()

    def run(self):
        """
        runs robot swarm to final positions
        :return: None
        """
        self.start()
        while not self.done:
            print('positions asked')
            positions = self.get_positions()  # marvelmind chokes speed
            print('positions:', positions)
            for robot in self.robots:
                print(robot, 'running')
                robot.run(positions)  # web requests choke speed
                print(robot, 'run')
            self.check_done()
        for robot in self.robots:
            robot.when_done()
        print('SWARM DONE!')



hedge = MarvelmindHedge('/dev/tty.usbmodem1421')
hedge.start()
time.sleep(2)
swarm = RobotSwarm('swarm.txt')
swarm.run()
