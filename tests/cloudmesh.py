import network
import ubinascii
import time
import machine
import socket
from machine import Pin, PWM
import os

version = 0.1

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
        self.light.high()
        
    def blink(self, n):
        for i in range(0,n):
            self.on()
            time.sleep(0.1)
            self.off()
            time.sleep(0.1)

def get_attributes(filename):
    f = open(filename)
    contents = f.read()
    f.close()
    # print (contents)
    contents.replace("\r\n","\n")

    attributes = {}
    lines = contents.split("\n")
    for line in lines:
        if ":" in line:
            attribute, value = line.split(":")
            attributes[attribute.strip()] = value.strip()

    return attributes

def cat(filename):
    f = open(filename)
    data = f.read()
    print (data)
    f.close()

def connect():
    print('starting network ...')

    credentials = get_attributes('credentials.txt')
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

def console():
    import webrepl
    webrepl.start()

def clean():
    os.remove("boot.py")
    os.remove("webrepl_cfg.py")
    
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


