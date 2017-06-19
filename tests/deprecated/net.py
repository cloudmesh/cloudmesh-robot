"""
First create a credentials file with::

    cms robot credential set SSID USERNAME PASSWORD

username is not used for now, make sure you match your ssid and password
it writes a file ~/.cloudmesh/robot/credentials.txt. You can copy that with::

    cms robot credential put

onto the robot. Than you can run the program with:

  cd tests
  cms robot run led.py

Connect to the ip that you get for teh robot (simply run the prg without 
the loop, to get it, or look up in your modem)
Now you can switch on and off the LED viw the web page provided.
"""
import network
import ubinascii
import time
import machine
import socket


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

def do_connect():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(credentials['ssid'], credentials['password'])
        while not sta_if.isconnected():
            pass
    return sta_if.ifconfig()


credentials = get_attributes('credentials.txt')

print (credentials)

print('starting network ...')


ap_if = network.WLAN(network.AP_IF)
print(ap_if.active())
print(ap_if.ifconfig())

net = do_connect()
print (net)
print ('IP: ', net[0])

mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
print ('MAC:', mac)

