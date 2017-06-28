import network
import ubinascii
import utime
import machine
import socket
import os
import math

##############################################
# VERSION
##############################################

version = "0.5"

##############################################
# PIN MANAGEMENT
##############################################

def p(name):
    """
    return the pin from the pin name
    :param name: the pin name D1 ... D8
    :return: 
    """
    mapping = {
        "D0": 16,
        "D1": 5,
        "D2": 4,
        "D3": 0,
        "D4": 2,
        "D5": 14,
        "D6": 12,
        "D7": 13,
        "D8": 15,
        "D9": 3,
        "D10": 1,
    }

    if name in mapping:
        return mapping[name]
    else:
        return 2


def pin_id(pin):
    if type(pin) == str:
        return p(pin)
    elif type(pin) == int:
        return pin


def mac():
    return ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()


##############################################
# FILE MANAGEMENT
##############################################

def cat(filename):
    """
    prints the content of a file
    :param filename: the filename
    """
    f = open(filename)
    data = f.read()
    print(data)
    f.close()


def ls():
    print('\n'.join(os.listdir(".")))


def clean():
    os.remove("boot.py")
    os.remove("webrepl_cfg.py")



##############################################
# LED
##############################################

class LED(object):
    # pin = 2
    def __init__(self, pin):
        """
        defne an LED on a given pin
        :param pin: the number of the pin
        """
        self.pin = pin
        self.light = machine.Pin(self.pin, machine.Pin.OUT)

    def on(self):
        """
        switch on the LED
        """

        self.light.low()

    def off(self):
        """
        switch the LED off
        """
        self.light.high()

    def blink(self, n, dt=0.1):
        """
        make the LED blink
        :param n: number of blinks
        :param dt: time delay between on and off 
        :return: 
        """
        for i in range(0, n):
            self.on()
            utime.sleep(dt)
            self.off()
            utime.sleep(dt)
            self.on()


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
            self.off()
    
