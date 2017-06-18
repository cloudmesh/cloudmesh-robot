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


LED = machine.Pin(2, machine.Pin.OUT)

def led(on):
    if on:
        LED.low()
    else:
        LED.high()

status = False
led(status)


html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<center>
<h3>cloudmesh.robot</h3>
<h2>ESP8266 LED on and off Test</h2>
</center>
<form>
<center>
LED: 
<button name="LED" value="ON" type="submit">LED ON</button>
<button name="LED" value="OFF" type="submit">LED OFF</button>
</center>
<br/>
<center>
Status: {status}
{msg}
</center>
</form>
</html>
"""

def bar(status):
    if status:
        return '<p style="color: #ffffff; background-color: #3333ff"> LED ON </p>'
    else:
        return '<p style="color: #000000; background-color: #ffffff"> LED OFF </p>'

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON = request.find('/?LED=ON')
    LEDOFF = request.find('/?LED=OFF')
    if LEDON == 6:
        #print('TURN LED ON')
        status = True
    if LEDOFF == 6:
        status = False
    led(status)

    data = {
        'status': status,
        'msg': bar(status)
    }

    response = html.format(**data)
    conn.send(response)
    conn.close()


