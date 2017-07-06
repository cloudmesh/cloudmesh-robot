import time
from math import pi
from newcm import Motor
from newcm import SpeedMeter
from newcm import LED

print("A")

class Car(object):

    def __init__(self,
                 leftmotor,
                 rightmotor,
                 leftspeedmeter,
                 rightspeedmeter
                 ):
        """
        Consolidates robot parts to one object
        :param leftmotor: Motor
        :param rightmotor: Motor
        :param leftspeedmeter: SpeedMeter
        :param rightspeedmeter: SpeedMeter
        """
        self.left = leftmotor
        self.right = rightmotor
        self.sml = leftspeedmeter
        self.smr = rightspeedmeter

    def turn_angle(self, angle):
        """
        Turns robot given angle. Turn left with negative. Turn right with positive.
        :param angle: Number (angle in degrees)
        """
        ticks = abs(((((angle * math.pi) / 180) * 13.6) / (6.7 * math.pi)) * 20)
        if angle < 0:
            self.right.set(800)
            self.right.forward()
            self.smr.wait_ticks(ticks)
            self.right.stop()
            self.right.set(1023)
        elif angle > 0:
            self.left.set(800)
            self.left.forward()
            self.sml.wait_ticks(ticks)
            self.left.stop()
            self.left.set(1023)

print("B")
left = Motor("left")
right = Motor("right")
sml = SpeedMeter(15)
smr = SpeedMeter(16)
car = Car(left, right, sml, smr)
led = LED(2)
