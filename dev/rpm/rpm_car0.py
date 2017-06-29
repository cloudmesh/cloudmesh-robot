import network
import ubinascii
import time
import utime
import machine
import socket
from machine import Pin, PWM

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
        self.motor = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.d = 1023
        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name

    def forward(self):
        self.direction.low()
        self.speed.duty(self.d)

    def backward(self):
        self.direction.high()
        self.speed.duty(self.d)

    def stop(self):
        self.speed.duty(0)

    def dutyset(self, value):
        if 0 <= value <= 1023:
            self.d = value


##############################################
# RPM METER MANAGEMENT
##############################################

class SpeedMeter(object):
    def __init__(self, pin):
        """
        SpeedMeter refers to the rpm meter on each wheel.
        :param pin: number of the pin
        """
        self.pin = machine.Pin(pin, machine.Pin.IN)
        self.status = Pin.value(self.pin)
        self.counter = 0

    def update(self):
        self.status = Pin.value(self.pin)

    def get(self):
        turn = True
        t0 = utime.ticks_ms()
        delta_t = 0
        count_start = self.counter
        while delta_t < 1000:
            self.update()
            if self.status == 1 and turn:
                turn = False
                self.counter += 1
            elif self.status == 0:
                turn = True
                delta_t = utime.ticks_diff(utime.ticks_ms(), t0)
        count_dt = self.counter - count_start
        print (count_dt)
        return count_dt


class Car(object):
    def __init__(self, leftmotor, rightmotor, leftrpm, rightrpm):
        self.leftmotor = leftmotor
        self.rightmotor = rightmotor
        self.leftrpm = leftrpm
        self.rightrpm = rightrpm

    def rpmtest(self):
        self.leftmotor.forward()
        self.rightmotor.forward()
        for i in range(0, 10):
            l = self.leftrpm.get()
            r = self.rightrpm.get()
            print(l)
            print(r)

smr = SpeedMeter(16)
sml = SpeedMeter(15)
right = Motor("right")
left = Motor("left")
car = Car(left, right, sml, smr)
led = LED(2)

led.blink(5)


def rpmtest():
    left.forward()
    right.forward()
    for i in range(0, 10):
        l=sml.get()
        r=smr.get()
        print(l)
        print(r)
    return "done"
