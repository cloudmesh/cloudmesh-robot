from newcm import SpeedMeter
from newcm import Motor
import time
import requests
import os
from marvelmind import MarvelmindHedge

class DrivingRobot(object):

    def __init__(self,
                 leftmeter,
                 rightmeter,
                 leftmotor,
                 rightmotor,
                 alpha=.1,
                 epsilon=4
                 ):
        """

        :param leftmeter: SpeedMeter
        :param rightmeter: SpeedMeter
        :param leftmotor: Motor
        :param rightmotor: Motor
        :param alpha: Number
        :param epsilon: Number
        """
        self.lsm = leftmeter
        self.rsm = rightmeter
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.alpha = alpha
        self.epsilon = epsilon
        self.going_left = True
        self.going_right = True
        self.on_track = 0
        self.slope = None
        self.intercept = None

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

    def drive_to(self, tty='/dev/tty.usbmodemFD121', end_x, end_y):
        # unfinished


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
    
