import network
import ubinascii
import time
import machine
import socket
from machine import Pin, PWM
import os
import math

##############################################
# VERSION
##############################################

version = 0.1

##############################################
# PIN MANAGEMENT
##############################################

def p(name):
    if name == "D8":
        return 15
    elif name == "D7":
        return 13
    else:
        return 2

##############################################
# WEB REPL
##############################################

def console():
    import webrepl
    webrepl.start()


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
    print (data)
    f.close()

def clean():
    os.remove("boot.py")
    os.remove("webrepl_cfg.py")

##############################################
# NETWORK MANAGEMENT
##############################################

def get_attributes(filename):
    f = open(filename)
    contents = f.read()
    f.close()
    contents.replace("\r\n","\n")

    attributes = {}
    lines = contents.split("\n")
    for line in lines:
        if ":" in line:
            attribute, value = line.split(":")
            attributes[attribute.strip()] = value.strip()

    return attributes


def connect(filename='credentials.txt'):
    """
    connects to the network while using the credentials
    :return: the network information
    """
    print('starting network ...')

    credentials = get_attributes(filename)
    print (credentials)

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(credentials['ssid'], credentials['password'])
        while not sta_if.isconnected():
            pass
    print('connection ok')

    return sta_if.ifconfig()


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
        self.light = machine.Pin(pin, machine.Pin.OUT)

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
            time.sleep(dt)
            self.off()
            time.sleep(dt)


class LED2(object):
    def __init__(self, pin):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        self.light = machine.PWM(machine.Pin(pin), freq=1000)

    def pulse(self, t):
        for i in range(20):
            self.light.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
            time.sleep_ms(t)


##############################################
# SERVO
##############################################

class Servo(object):
    def __init__(self, pin, min=40, max=115):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        self.servo = machine.PWM(machine.Pin(pin), freq=50)
        self.minimum = min
        self.maximum = max
        self.middle = int((max - min) / 2) + min

    def off(self):
        self.servo.duty(0)

    def set(self, value, dt=0.1):
        pos = value + self.minimum
        if self.minimum <= pos <= self.maximum:
            self.servo.duty(pos)
        time.sleep(dt)
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
            time.sleep(dt)
            self.off()
            self.high()
            time.sleep(dt)
            self.off()


##############################################
# MAIN FOR TESTING
##############################################

def hello():

    led = LED(2)
    led.blink(2)

    #ap_if = network.WLAN(network.AP_IF)
    #print(ap_if.active())
    #print(ap_if.ifconfig())

    led.blink(2)

    net = connect()
    print (net)
    print ('IP: ', net[0])

    led.blink(2)

    # mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    # print ('MAC:', mac)

    led.blink(2)

if __name__ == "__main__":
    hello()
