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

version = 0.3


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

def getmac():
    mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
    return mac

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
    print(data)
    f.close()


def ls():
    print ('\n'.join(os.listdir()))

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
    if ssid == None and password == None:
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
        pin = pin_id(pin)
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
        pin = pin_id(pin)
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
# MOTOR MANAGEMENT
##############################################

class motor(object):
    """the motor class has the name attribute and a forward duty and backward duty"""

    def __init__(self,
                 name,
                 forward_duty=1023,
                 backward_duty=1023):

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

        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name
        self.forward_duty = forward_duty
        self.backward_duty = backward_duty

    def forward(self):
        """turns a motor on in the forward direction"""
        self.direction.low()
        self.duty(self.forward_duty)

    def backward(self):
        """turns a motor on in the backward direction"""
        self.direction.high()
        self.duty(self.backward_duty)

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
            PWM(Pin(self.pin_speed), freq=1000, duty=value)


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


if __name__ == "__main__":
    hello()
