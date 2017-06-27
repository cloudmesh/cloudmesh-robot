import cm
import network
import ubinascii
import time
import machine
import socket
from machine import Pin, PWM

led = cm.LED(2)

right = cm.motor("right")
left = cm.motor("left")

led.blink(5)

credentials = cm.get_attributes('credentials.txt')

print(credentials)

print('starting network ...')

credentials = cm.get_attributes('credentials.txt')

print(credentials)

led.blink(2)

net = cm.connect()

led.blink(5)

data = {
    "style": "style=\"height:100px;width:100px;background-color:#4CAF50\"",
    "stylered": "style=\"height:100px;width:100px;background-color:Red\""
}

html = """<!DOCTYPE html>
<html>
<head> 

<title>Cloudmesh ESP8266 Car</title> 

</head>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Car Test</h2>
</center>
<form>
<center>
<table>

<tr>
<td></td>
<td><button name="FORWARD" value="ON" type="submit" {style}>FORWARD</button></td>
<td></td>
</tr>

<tr>
<td><button name="LEFT" value="ON" type="submit"  {style}">LEFT ON</button></td>
<td><button name="STOP" value="ON" type="submit" {stylered}>STOP</button></td>
<td><button name="RIGHT" value="ON" type="submit" {style}>RIGHT ON</button></td>
</tr>

<tr>
<td></td>
<td><button name="BACK" value="ON" type="submit" {style}>BACKWARD</button></td>
<td></td>
</tr>

</table>
<center>
</form>
</html>
""".format(**data)

print (html)
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
    RIGHTON = request.find('/?RIGHT=ON')
    FORWARD = request.find('/?FORWARD=ON')
    STOP = request.find('/?STOP=ON')
    BACK = request.find('/?BACK=ON')

    direction = 'STOP'
    left_on = False
    right_on = False
    if LEFTON == 6:
        left.forward()
        direction = 'LEFT'
    if LEFTOFF == 6:
        left.stop()
    if RIGHTON == 6:
        right.forward()
        direction = 'LEFT'
    if RIGHTOFF == 6:
        right.stop()
    if STOP == 6:
        right.stop()
        left.stop()
        direction = 'STOP'
    if FORWARD == 6:
        right.forward()
        left.forward()
        direction = 'FORWARD'
    if BACK == 6:
        right.backward()
        left.backward()
        direction = 'BACKWARD'


    cm.feedback(conn, html)

    conn.close()
