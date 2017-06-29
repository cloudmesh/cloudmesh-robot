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
from cm import _ls
from cm import clean

##############################################
# NETWORK MANAGEMENT
##############################################

def get_attributes(filename):
    f = open(filename)
    contents = f.read()
    f.close()
    contents.replace("\r\n", "\n")

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
    print(credentials)

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(credentials['ssid'], credentials['password'])
        while not sta_if.isconnected():
            pass
    print('connection ok')

    return sta_if.ifconfig()


def net(ssid=None, password=None, username='gregor'):
    if ssid is None and password is None:
        cat("credentials.txt")
    else:
        d = {
            'ssid': ssid,
            'password': password,
            'username': username
        }
        with open('credentials.txt', 'w') as f:
            for i in ['ssid', 'password']:
                f.write(i + ": " + d[i] + "\n")
            for i in ['username']:
                f.write(i + ": " + d[i])


def ap(filename='credentials.txt'):
    credentials = get_attributes(filename)
    print(credentials)

    print("start ap")

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)

    sta_if.active()
    ap_if.active()
    ap_if.ifconfig()

    sta_if.connect(credentials['ssid'], credentials['password'])
    print(sta_if)

    print(sta_if.ifconfig())
    print(ap_if.ifconfig())


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

def feedback(conn, html):
    response = ''.join(html.split('\n')[1:])

    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(response),
        'Connection': 'close',
    }
    response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in response_headers.items())

    # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'  # this can be random

    # sending all this stuff
    conn.send('%s %s %s' % (response_proto, response_status, response_status_text))
    conn.send(response_headers_raw)
    conn.send('\n')  # to separate headers from body

    conn.send(response)


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
