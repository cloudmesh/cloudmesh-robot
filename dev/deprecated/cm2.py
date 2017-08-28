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

version = "0.5.broken"


##############################################
# PIN MANAGEMENT
##############################################

from cm import p
from cm import pin_id
from cm import mac

##############################################
# WEB REPL
##############################################

def console():
    import webrepl
    webrepl.start()


##############################################
# FILE MANAGEMENT
##############################################

from cm import cat
from cm import ls
from cm import clean

##############################################
# NETWORK MANAGEMENT
##############################################

from cm import get_attributes
from cm import connect
from cm import net

from cm import ap


##############################################
# LED
##############################################

from cm import LED

class LED2(object):
    def __init__(self, pin):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        pin = pin_id(pin)
        self.light = machine.PWM(machine.Pin(pin), freq=1000)

    def pulse(self, t):
        for i in range(20):
            self.light.duty(int(math.sin(float(i) / 10.0 * math.pi) * 500.0 + 500.0))
            utime.sleep_ms(t)


##############################################
# SERVO
##############################################

from cm import Servo


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
        self.direction.low()
        self.motor.duty(self.d)

    def backward(self):
        self.direction.high()
        self.motor.duty(self.d)

    def stop(self):
        self.motor.duty(0)

    def set(self, value):
        if 0 <= value <= 1023:
            self.d = value

##############################################
# WEBPAGE MANAGEMENT
##############################################

from cm import feedback


##############################################
# MAIN FOR TESTING
##############################################

def hello():
    led = LED(2)
    led.blink(2)

    # ap_if = network.WLAN(network.AP_IF)
    # print(ap_if.active())
    # print(ap_if.ifconfig())

    led.blink(2)

    netw = connect()
    print(netw)
    print('IP: ', netw[0])

    led.blink(2)

    # mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    # print ('MAC:', mac)

    led.blink(2)

# if __name__ == "__main__":
#    hello()
