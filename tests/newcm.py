import network
import ubinascii
import utime
import machine
import socket
import os
import math


##############################################
# PIN MANAGEMENT
##############################################

from cm import p
from cm import pin_id
from cm import mac


##############################################
# MOTOR MANAGEMENT
##############################################

class Motor(object):
    """the motor class has the name attribute and a forward duty and backward duty"""

    def __init__(self, name):
        """Sets up two motors for a robot car
        :param name: left or right
        """
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0
        self.d = 1023
        self.motor = machine.PWM(machine.Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = machine.Pin(self.pin_direction, machine.Pin.OUT)
        self.name = name

    def forward(self):
        self.motor.duty(self.d)
        self.direction.low()

    def backward(self):
        self.motor.duty(self.d)
        self.direction.high()

    def stop(self):
        self.motor.duty(0)

    def set(self, value):
        if 0 <= value <= 1023:
            self.d = value


##############################################
# LED
##############################################

from cm import LED


##############################################
# FILE MANAGEMENT
##############################################

from cm import cat
from cm import ls
from cm import clean


##############################################
# SERVO
##############################################

class Servo(object):
    def __init__(self, pin, minimum=40, maximum=115):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        pin = pin_id(pin)
        self.servo = machine.PWM(machine.Pin(pin), freq=50)
        self.minimum = minimum
        self.maximum = maximum
        self.middle = int((maximum - minimum) / 2) + minimum

    def off(self):
        self.servo.duty(0)

    def set(self, value, dt=0.1):
        pos = value + self.minimum
        if self.minimum <= pos <= self.maximum:
            self.servo.duty(pos)
        utime.sleep(dt)
        self.off()

    def zero(self):
        self.low()

    def low(self):
        self.servo.duty(self.minimum)

    def high(self):
        self.servo.duty(self.maximum)

    def mean(self):
        self.servo.duty(self.middle)

    def swim(self, n, dt=0.1):
        self.zero()
        for i in range(0, n):
            self.low()
            utime.sleep(dt)
            self.off()
            self.high()
            utime.sleep(dt)
            self.mean()
            utime.sleep(dt)
            self.off()


##############################################
# NETWORK MANAGEMENT
##############################################

from cm import get_attributes
from cm import connect
from cm import net
from cm import ap


##############################################
# WEBPAGE MANAGEMENT
##############################################

from cm import feedback

##############################################
# RPM MANAGEMENT
##############################################


class SpeedMeter(object):

    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.IN)
        self.status = self.pin.value()
        self.counter = 0

    def update(self):
        self.status = self.pin.value()

    def get(self):
        turn = True
        t0 = utime.ticks_ms()
        delta_t = 0
        count_start = self.counter
        while delta_t < 500:
            self.update()
            if self.status == 1 and turn:
                turn = False
                self.counter += 1
            elif self.status == 0:
                turn = True
                delta_t = utime.ticks_diff(utime.ticks_ms(), t0)
        count_dt = self.counter - count_start
        return count_dt

    def rpm(self):
        return (self.get() / 20) * 300

    def wait_ticks(self, ticks):
        turn = True
        cticks = 0
        while cticks < ticks:
            self.update()
            if self.status == 1 and turn:
                turn = False
                cticks += 1
            elif self.status == 0:
                turn = True


##############################################
# RPM MANAGEMENT
##############################################


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


##############################################
# DrivingRobot
##############################################


def set_line(x0, y0, fx, fy):
    slope = (fy - y0) / (fx - x0)
    intercept = y0 - (x0 * slope)
    return slope, intercept

