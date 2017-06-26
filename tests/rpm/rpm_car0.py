import network
import ubinascii
import time
import utime
import machine
import socket
from machine import Pin, PWM


class Motor(object):
    def __init__(self, name):
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0

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

    def rpm(self):
        return (self.get() / 20) * 300

smr = SpeedMeter(16)

sml = SpeedMeter(15)

right = Motor("right")
left = Motor("left")
led = cm.LED(2)
led.blink(5)



def motor_adjuster(right_meter, left_meter):
    """adjusts the duties of the motors based on the wheel rpm
    """
    if rpm_right == 0:
        print('no right')
    if rpm_left == 0:
        print('no left')
    else:
        print('rpm l')
        print(rpm_left)
        print('rpm r')
        print(rpm_right)

def test():
    left.forward()
    right.forward()
    rpm_right = right_meter.get()
    rpm_left = left_meter.get()
    print('rpm right')
    print(rpm_right)
    print('rpm left')
    print(rpm_left)
