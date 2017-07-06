import time
from marvelmind import MarvelmindHedge
from math import pi
from newcm import Motor
from newcm import SpeedMeter


class DrivingRobot(object):

    def __init__(self,
                 leftmeter,
                 rightmeter,
                 leftmotor,
                 rightmotor,
                 tty,
                 alpha=45,
                 epsilon=4,
                 ):
        """

        :param leftmeter: SpeedMeter
        :param rightmeter: SpeedMeter
        :param leftmotor: Motor
        :param rightmotor: Motor
        :param tty: String
        :param alpha: Number
        :param epsilon: Number
        """
        self.sml = leftmeter
        self.smr = rightmeter
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.alpha = alpha
        self.epsilon = epsilon
        self.going_left = True
        self.going_right = True
        self.on_track = 0
        self.slope = None
        self.intercept = None
        self.tty = tty

    def set_line(self, x0, y0, fx, fy):
        """

        :param x0: initial x
        :param y0: initial y
        :param fx: final x
        :param fy: final y
        :return: Slope, Y intercept
        """
        self.slope = (fy - y0) / (fx - x0)
        self.intercept = y0 - (x0 * self.slope)
        return self.slope, self.intercept

    def turn_angle(self, angle):
        """
        Turns robot given angle. Turn left with negative. Turn right with positive.
        :param angle:
        :return:
        """
        radangle = (angle * pi) / 180
        distance = radangle * 13.6
        rotations = distance / (6.7 * pi)
        ticks = rotations * 20
        if angle < 0:
            self.rightmotor.set(500)
            self.rightmotor.forward()
            self.smr.wait_ticks(ticks)
            self.rightmotor.stop()
            self.rightmotor.set(1023)
        elif angle > 0:
            self.leftmotor.set(500)
            self.leftmotor.forward()
            self.sml.wait_ticks(ticks)
            self.leftmotor.stop()
            self.leftmotor.set(1023)

    def forward(self, distance):
        rotations = distance / (6.7 * pi)
        ticks = round((rotations * 20), 0)
        cleft = 0
        cright = 0
        lturn = True
        rturn = True
        turn_off = False
#        slow_adjust = 51
        self.leftmotor.forward()
        self.rightmotor.forward()
        while True:
            if cleft > ticks:
                self.leftmotor.stop()
                if turn_off:
                    break
                else:
                    turn_off = True
            if cright > ticks:
                self.rightmotor.stop()
                if turn_off:
                    break
                else:
                    turn_off = True
            left_status = self.sml.update()
            right_status = self.smr.update()
            if left_status == 1 and lturn:
                lturn = False
                cleft += 1
            elif left_status == 0 and not lturn:
                lturn = True
            if right_status == 1 and rturn:
                cright += 1
            elif right_status == 0 and not rturn:
                rturn = True

#            if cleft > cright:
#                if slow_adjust > 50:
#                    self.leftmotor.set(self.leftmotor.d - 2)
#                    slow_adjust = 0
#                else:
#                    slow_adjust += 1
#            elif cright > cleft:
#                if slow_adjust > 50:
#                    self.rightmotor.set(self.rightmotor.d - 2)
#                    slow_adjust = 0
#                else:
#                    slow_adjust += 1

    def drive_to(self, fx, fy):
        """

        :param fx: Number Final x position
        :param fy: Number Final y position
        """
        robot = MarvelmindHedge(self.tty)
        robot.start()
        addr0, x0, y0, z0, t0 = robot.position()
        m, b = self.set_line(x0, y0, fx, fy)
        going_left = True
        going_right = True
        on_track = 0
        finalerror = 10

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

            elif displacement < - self.epsilon:
                if going_left:
                    if on_track == 0:
                        on_track += 1
                    elif on_track == 1:
                        on_track += 1
                    else:
                        self.alpha -= 5
                    self.turn_angle(self.alpha)
                    going_left = False
                    going_right = True
                    self.forward(10)  # move forward 10 cm
                elif going_right:
                    on_track = 0
                    self.alpha += 10
                    self.turn_angle(self.alpha)
                    self.forward(10)

            elif displacement > self.epsilon:
                if going_right:
                    if on_track == 0:
                        on_track += 1
                    elif on_track == 1:
                        on_track += 1
                    else:
                        self.alpha -= 5
                    self.turn_angle(- self.alpha)
                    going_left = True
                    going_right = False
                    self.forward(10)
                elif going_left:
                    on_track = 0
                    self.alpha += 10
                    self.turn_angle(- self.alpha)
                    self.forward(10)


class RelativeMove(object):

    def __init__(self,
                 # left speed meter
                 # right speed meter
                 # left motor
                 # right motor
                 ):
        pass

    def angle(self, value):
        # left turn negative
        # right turn positive
        # convert angle to radians
        # convert radians to distance
        # convert distance to wheel ticks
        # stop motor after that number of ticks
        pass

    def forward(self, distance):
        # rotations = distance / circumference
        # ticks = round(rotations * 20)
        # current left = 0
        # current right = 0
        # left turn = True
        # right turn = True
        # turn_off = False
        # left motor forward()
        # right motor forward()
        # while True:
            # if current left > ticks:
                # left motor stop()
                # if turn_off:
                    # break
                # else:
                    # turn_off = True
            # if current right > ticks:
                # right motor stop()
                # if turn_off:
                    # break
                # else:
                    # turn_off = True
            # left status = left motor update()
            # right status = right motor update()
            # if left status == 1 and left turn:
                # left turn = False
                # current left += 1
            # elif left status == 0:
                # left turn = True
            # if right status == 1 and right turn:
                # right turn = False
                # current right += 1
            # elif right status == 0:
                # right turn = True
        pass
