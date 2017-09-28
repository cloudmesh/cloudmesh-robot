import math
import time

import requests

from mavelmind import MarvelmindHedge


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
        self.done_number = 0
        self.last_angle = int(last_angle)

    def update(self):
        return hedge.number_position(self.number)

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
        else:
            print ("ERROR: unknown direction:", direction)

        try:
            headers = {'User-Agent': "Car"}
            r = requests.get('http://' + self.ip, headers=headers, params=payload)
        except Exception as e:
            print(type(e), e)

    def check_done(self, cx, cy):
        if abs(cx - self.fx) < self.epsilon and abs(cy - self.fy) < self.epsilon:
            self.done = True

    def turn(self):
        """
        calculates turn angle and sends turn command to robot
        """
        self.last_x = self.cx
        self.last_y = self.cy
        addr, self.cx, self.cy, cz, ct = self.update()  # get current position
        self.check_done(self.cx, self.cy)
        if not self.done:
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
                self.move(direction, delta_angle)  # turn robot
                self.last_angle = angle2
            else:
                print('on track')
                self.last_angle = angle1
            print('turn done')
        else:
            print('done')

    def if_done(self):
        print('done?', self.done, self.done_number)
        if self.done and self.done_number < 1:
            print('final turn')
            v1, v2 = self.find_vectors(self.last_x, self.last_y, self.cx, self.cy, self.cx, 0)
            delta_angle = int(self.find_delta(v1, v2))
            angle1 = int(self.find_angle(v1[0], v1[1]))  # get unit vector angles
            angle2 = int(self.find_angle(v2[0], v2[1]))
            print(angle1, angle2)
            direction = self.turn_direction(angle1, angle2)
            self.move(direction, delta_angle)
            self.done_number += 1
        else:
            pass

    def go(self):
        if not self.done:
            distance = int(math.sqrt(((self.cx - self.fx) ** 2) + ((self.cy - self.fy) ** 2)))
            if distance > 50:
                self.move('forward', 1)
            elif 20 <= distance <= 50:
                self.move('forward', .5)
            elif distance < 20:
                self.move('forward', .3)


class RobotSwarm(object):

    def __init__(self, file):
        """
        creates a swarm of robots connected to Marvelmind
        :param file: String
        :param hedge: MarvelmindHedge
        """
        self.file = file
        self.done = False
        self.robots = []

    def make_robots(self):
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

    def check_done(self):
        for robot in self.robots:
            if not robot.done:
                self.done = False
                break
            else:
                self.done = True

    def crash_avoidance(self):
        avoided = False
        go_again = False
        while not avoided:
            print('checking trajectories...')
            for robot in self.robots:
                print('checking robot')
                if not robot.done:
                    print('robot is still moving')
                    m = math.tan((robot.last_angle * math.pi) / 180)
                    print('robot angle:', str(robot.last_angle))
                    b = robot.cy - (m * robot.cx)
                    b1 = b - (10 * math.sqrt(1 + (m ** 2)))
                    b2 = b + (10 * math.sqrt(1 + (m ** 2)))
                    print('line 1, y=' + str(m) + 'x +', str(b1))
                    print('robot line, y=' + str(m) + 'x +', str(b))
                    print('line 2, y=' + str(m) + 'x +', str(b2))
                    for other in self.robots:
                        print('checking other robot')
                        if robot.cx == other.cx and robot.cy == other.cy:
                            print("it's the same robot")
                            if not go_again:
                                avoided = True
                        else:
                            if other.done:
                                print('other is done.')
                                print('analyzing trajectory')
                                print('robot position', str(other.cx), str(other.cy))
                                y1 = (m * other.cx) + b1
                                y2 = (m * other.cx) + b2
                                if y1 < other.cy < y2 or y2 < other.cy < y1:
                                    print('other is within parameters')
                                    distance = math.sqrt(((other.cx - robot.cx) ** 2) + ((other.cy - robot.cy) ** 2))
                                    if distance < 50:
                                        print('on track for collision')
                                        print('turning to avoid')
                                        robot.move('left', 60)
                                        if robot.last_angle < 300:
                                            robot.last_angle = robot.last_angle + 60
                                        else:
                                            robot.last_angle = robot.last_angle - 300
                                        avoided = False
                                        go_again = True
                                    else:
                                        print('collision unlikely')
                                        avoided = True

                                else:
                                    print('not on track for collision')
                                    if not go_again:
                                        avoided = True
                            else:
                                print('other robot is still moving')
                                if not go_again:
                                    avoided = True
                else:
                    print('robot is done')
                    if not go_again:
                        avoided = True
            go_again = False

    def run(self):
        self.make_robots()
        for robot in self.robots:
            robot.move("forward", 1)
        time.sleep(1.5)
        while not self.done:
            for robot in self.robots:
                robot.turn()
            time.sleep(.5)
            for robot in self.robots:
                robot.go()
            time.sleep(.5)
            self.check_done()
            for robot in self.robots:
                robot.if_done()

hedge = MarvelmindHedge('/dev/tty.usbmodem1421')
hedge.start()
time.sleep(2)
rs = RobotSwarm('swarm.txt')
rs.run()



