import network
import ubinascii
import time
import utime
import machine
import socket
from machine import Pin, PWM
import cm

class motor2(object):
    """the motor class has the name attribute and a forward duty and backward duty"""

    def __init__(self,
                 name):

        """
        Sets up two motors for a robot car
        :param name:
        :param forward_duty:
        :param backward_duty:
        :param pin_left_speed:
        :param pin_left_direction:
        :param pin_right_speed:
        :param pin_right_direction:
        """
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0

        self.d = 0
        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=self.d)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name

    def forward(self):
        """turns a motor on in the forward direction"""
        self.direction.low()
        self.duty(self.d)

    def backward(self):
        """turns a motor on in the backward direction"""
        self.direction.high()
        self.duty(self.d)

    def stop(self):
        """stops a motor"""
        self.duty(0)

    def duty(self, value):
        """
        specifies the duty associated with the pin
        :param value: the duty value
        """
        if 0 <= value <= 1023:
            ### BUG ?  this shoudl set the duty and not create a new PWM???? Check
            self.d = value

class SpeedMeter(object):

    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.IN)
        self.status = Pin.value(self.pin)
        self.counter = 0

    def update(self):
        self.status = Pin.value(self.pin)

    def tick_up(self):
        if self.status == 1:
            self.counter += 1

    def get(self):
        turn = True
        t0 = utime.ticks_ms()
        delta_t = 0
        count_start = self.counter
        while delta_t < 100:
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

right = motor2("right")
left = motor2("left")

led.blink(5)