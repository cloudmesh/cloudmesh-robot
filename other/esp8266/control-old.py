import cm
import network
import ubinascii
import time
import machine
import socket
import ure
from machine import Pin, PWM
import gc

#led = cm.LED(2)

right = cm.Motor("right")
left = cm.Motor("left")

#led.blink(5)

credentials = cm.get_attributes('credentials.txt')

print(credentials)

print('starting network ...')

credentials = cm.get_attributes('credentials.txt')

print(credentials)

#led.blink(2)

net = cm.connect()

#led.blink(5)

data = {
    "style": "style=\"height:100px;width:100px;background-color:#4CAF50\"",
    "stylered": "style=\"height:100px;width:100px;background-color:Red\"",
    "number": "NA"
}

form = """<!DOCTYPE html>
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

I= {number}

<table>

<tr>
<td></td>
<td><button name="FORWARD" value="ON" type="submit" {style}>FORWARD</button></td>
<td></td>
</tr>

<tr>
<td><button name="SPEED" value="0.100" type="submit"  {style}">LEFT ON</button></td>
<td><button name="SPEED" value="0.0" type="submit" {stylered}>STOP</button></td>
<td><button name="SPEED" value="100.0" type="submit" {style}>RIGHT ON</button></td>
</tr>

<tr>
<td></td>
<td><button name="BACKWARD" value="ON" type="submit" {style}>BACKWARD</button></td>
<td></td>
</tr>

</table>
<center>
</form>
</html>
"""


html = form.format(**data)



#print (html)
#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

i = 0
#request = 1024 * 'a'
while True:
    i = i + 1

    conn, addr = s.accept()
    request = conn.recv(1024)
    #request = conn.recv(512)

    request = str (request)

    free = gc.mem_free()

    data['number'] = str(i) + ' ' + str(free)

    # + ' ' + str(addr)

    if 6 == request.find('/?SPEED='):
        value = request[14:].split(' HTTP', 1)[0]
        x, y = value.split('.')

        # print(x, y)

    elif 6 == request.find('/?FORWARD'):

        pass

    elif 6 == request.find('/?BACWARD'):

        pass

    html = form.format(**data)

    cm.feedback(conn, html)

    conn.close()
    gc.collect()
