import network
import ubinascii
import time
import machine
import socket
from machine import Pin, PWM


class motor


p = Pin(2, Pin.OUT)
p = Pin(0, Pin.OUT)




right = 4
left = 5

direction_right = Pin(2, Pin.OUT)


def motor (pin, status):
    if status:
        pwm = PWM(Pin(pin), freq=1000, duty=1023)
    else:
        pwm = PWM(Pin(pin), freq=1000, duty=0)


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




html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 Car</title> </head>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Car Test</h2>
</center>
<form>
<table>
<tr>
<td>LEFT:</td> 
<td><button name="LEFT" value="ON" type="submit">ON</button></td>
<td><button name="LEFT" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>RIGHT:</td>
<td><button name="RIGHT" value="ON" type="submit">ON</button></td>
<td><button name="RIGHT" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>FORWARD:</td>
<td><button name="FORWARD" value="ON" type="submit">ON</button></td>
<td><button name="FORWARD" value="OFF" type="submit">OFF</button></td>
</tr>
</table>
</form>
</html>
"""

LED = machine.Pin(2, machine.Pin.OUT)

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
    LEFTON = request.find('/?LEFT=ON')
    LEFTOFF = request.find('/?LEFT=OFF')
    RIGHTON = request.find('/?RIGHT=ON')
    RIGHTOFF = request.find('/?RIGHT=OFF')
    FORWARDON = request.find('/?FORWARD=ON')
    FORWARDOFF = request.find('/?FORWARD=OFF')

    left_on = False
    right_on = False
    if LEFTON == 6:
        left_on = True
    if LEFTOFF == 6:
        left_on = False
    if RIGHTON == 6:
        right_on = True
    if RIGHTOFF == 6:
        right_on = False
    if FORWARDOFF == 6:
        right_on = False
        left_on = False
    if FORWARDON == 6:
        right_on = True
        left_on = True

    motor(left, left_on)
    motor(right, right_on)

    response = html
    conn.send(response)
    conn.close()

