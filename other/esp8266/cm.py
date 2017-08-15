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
    for file in ['boot.py', 'webrepl_cfg.py']:
        try:
            os.remove("boot.py")
        except Exception as e:
            print ("File does not exist", file)


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

    def forward(self, value=None):
        if value is not None:
            self.motor.duty(value)
            self.direction.low()
        else:
            self.motor.duty(self.d)
            self.direction.low()

    def backward(self, value=None):
        if value is not None:
            self.motor.duty(value)
            self.direction.high()
        else:
            self.motor.duty(self.d)
            self.direction.high()

    def stop(self):
        self.motor.duty(0)

    def set(self, value):
        print (self.name, value)
        if 0 <= value <= 1023:
            self.d = value
            self.motor.duty(self.d)
            self.direction.low()
        elif -1023 <= value < 0:
            self.d = -value
            self.motor.duty(self.d)
            self.direction.high()

##############################################
# SERVO
##############################################

class Servo(object):
    def __init__(self, pin, minimum=29, maximum=115):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        pin = pin_id(pin)
        self.servo = machine.PWM(machine.Pin(pin), freq=50)
        self.minimum = minimum
        self.maximum = maximum
        self.middle = int((maximum - minimum) / 2) + minimum
        self.servo.duty(self.middle)
        self.position = self.middle
        self.atdratio = 180 / (maximum - minimum)
        self.dtaratio = (maximum - minimum) / 180

    def off(self):
        self.servo.duty(0)

    def set(self, value, dt):
        if self.minimum <= value <= self.maximum:
            self.servo.duty(value)
        utime.sleep(dt)
        self.position = value

    def zero(self):
        self.servo.duty(self.middle)
        self.position = self.middle

    def low(self):
        self.servo.duty(self.minimum)
        self.position = self.minimum

    def high(self):
        self.servo.duty(self.maximum)
        self.position = self.maximum

    def swim(self, n, dt=0.1):
        self.zero()
        for i in range(0, n):
            self.low()
            utime.sleep(dt)
            self.off()
            self.high()
            utime.sleep(dt)
            self.zero()
            utime.sleep(dt)
            self.off()

    def angletoduty(self, angl):
        return round((self.dtaratio * angl), 0)

    def dutytoangle(self, d):
        return round((self.atdratio * d), 0)

    def setangle(self, value, dt=1.0):
        start_position = self.position
        end_position = self.angletoduty(value) + self.middle
        duty_step = end_position - start_position
        if duty_step != 0:
            _dt = abs(dt / duty_step)
            # print('dt: ' + str(_dt))
        else:
            return
        if duty_step < 0:
            for i in range(0, abs(duty_step)):
                # print(i)
                cp = start_position - i
                self.set(cp, _dt)
        elif duty_step > 0:
            for i in range(0, duty_step):
                # print(i)
                cp = start_position + i
                self.set(cp, _dt)


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


# def ap(filename='credentials.txt'):
#    credentials = get_attributes(filename)
#    print(credentials)
#
#    print("start ap")
#
#   sta_if = network.WLAN(network.STA_IF)
#    ap_if = network.WLAN(network.AP_IF)
#
#    sta_if.active()
#    ap_if.active()
#    ap_if.ifconfig()
#
#    sta_if.connect(credentials['ssid'], credentials['password'])
#    print(sta_if)
#
#    print(sta_if.ifconfig())
#    print(ap_if.ifconfig())


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
    
