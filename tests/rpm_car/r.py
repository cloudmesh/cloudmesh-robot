import network
import ubinascii
import time
import utime
import machine
# import socket
from machine import Pin, PWM


class LED(object):
    """ associates an LED object with a pin"""

    # pin = 2
    def __init__(self, pin):
        self.light = machine.Pin(pin, machine.Pin.OUT)

    def on(self):
        """turns the LED on """
        self.light.low()

    def off(self):
        """turns the LED off """
        self.light.high()

    def blink(self, n):
        """flashes the LED n times"""
        for i in range(0, n):
            self.on()
            time.sleep(0.1)
            self.off()
            time.sleep(0.1)
            self.on()


class motor(object):
    def __init__(self, name):
        self.forward_speed = 1023
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0

        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name

    def forward(self):
        self.direction.low()
        self.duty(1023)

    def backward(self):
        self.direction.high()
        self.duty(1023)

    def stop(self):
        self.duty(0)

    def duty(self, d):
        PWM(Pin(self.pin_speed), freq=1000, duty=d)

    def set_forward_speed(self, duty):
        self.forward_speed = duty


class speed_meter(object):
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
        print ("GET")
        turn = True
        t0 = utime.ticks_ms()
        delta_t = 0
        count_start = self.counter
        print ("CN", self.counter)
        while delta_t < 200000:
            self.update()
            print ("L", delta_t, self.status, self.counter)
            if self.status == 1 and turn:
                print("A")
                turn = False
                self.counter += 1
            elif self.status == 0:
                print ("B")
                turn = True
                delta_t = utime.ticks_diff(utime.ticks_ms(), t0)
        count_dt = self.counter - count_start
        print (count_dt)
        return count_dt, self.counter

smr = speed_meter(16)



# sml = speed_meter(15)

#right = motor("right")
#left = motor("left")
led = LED(2)
led.blink(5)

print("hello")

for i in range(0, 400):
    # while True:
    print ("I:", i)
    print(smr.get())
    time.sleep(0.5)
    # print(sml.get())

    # def rpm_finder():
    #    t0 = 0
    #    delta_t_r = 0
    #    delta_t_l = 0
    #    while delta_t_r < 200000 and delta_t_l < 200000:
    #        if smr.status == 0:
    #            smr.count += 1
    #            delta_t_r = utime.ticks_diff(utime.ticks_us(), t0)
    #        if smr.status == 1:
    #            continue
    #        if sml.status == 0:
    #            sml.count += 1
    #            delta_t_l = utime.ticks_diff(utime.ticks_us(), t0)
    #        if sml.status == 1:
    #            continue
    #    right_rotations = smr.count / 20
    #    left_rotations = sml.count / 20
    #    rpm_r = right_rotations * 300
    #    rpm_l = left_rotations * 300
