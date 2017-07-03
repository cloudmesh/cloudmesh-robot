from newcm import SpeedMeter
from newcm import Motor

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
                # turn = False
        pass

self.update()
            if self.status == 1 and turn:
                turn = False
                self.counter += 1
            elif self.status == 0:
                turn = True
                delta_t = utime.ticks_diff(utime.ticks_ms(), t0)
        count_dt = self.counter - count_start
        return count_dt