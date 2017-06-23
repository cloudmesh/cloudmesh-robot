import cm
import network
import ubinascii
import time
import machine
import socket
import ure
from machine import Pin, PWM

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
""".format(**data)

print (html)
#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

reqpt = b'^GET \/\?(.*) HTTP(.*)'
while True:
    conn, addr = s.accept()
    #print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)

    if request is not None:
        #print(request)

        reqparam = ure.match(reqpt, request)
        #print(reqparam)
        if reqparam is not None:
            reqparam = reqparam.group(1)

            command, value = reqparam.split("=")



            if command == 'SPEED':

                # left, right = value.split('.')
                #print (left, right)

                #print ("SPEED")
                #led.blink(4)

                pass

            elif command == 'FORWARD':

                #print ("FORWARD")
                #led.blink(2)

                pass

            elif command == 'BACKWARD':

                #print ("BACKWARD")
                #led.blink(3)

                pass


    cm.feedback(conn, html)

    conn.close()
