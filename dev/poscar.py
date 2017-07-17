import cm
# import cm3
import socket
import network
import ubinascii
import utime
from machine import Pin


p1 = Pin(15, Pin.OUT)
p2 = Pin(13, Pin.OUT)

led = cm.LED(2)

led.blink(5)


credentials = cm.get_attributes('credentials.txt')
utime.sleep(.5)
led.blink(2)

ap_if = network.WLAN(network.AP_IF)
utime.sleep(.5)
led.blink(3)

net = cm.connect()
utime.sleep(.5)
led.blink(4)

mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
utime.sleep(.5)
led.blink(5)
print('mac')


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
<td><button name="LEFT" value="800" type="submit">ON</button></td>
</tr>
<tr>
<td>RIGHT:</td>
<td><button name="RIGHT" value="800" type="submit">ON</button></td>
</tr>
<tr>
<td>DIRECTION:</td>
<td><button name="STOP" value="1" type="submit">STOP</button></td>
</tr>
<tr>
<td>END:</td> 
<td><button name="END" value="1" type="submit">END</button></td>
</tr>
</table>
</form>
</html>
"""

utime.sleep(.5)

led.blink(6)


def find_params(request):
    pos = request.find('?')+1
    a = request[pos:].split(" HTTP")[0]
    params = a.split('&')
    return (params)

left = cm.Motor("left")
right = cm.Motor("right")
#smr = cm3.SpeedMeter(13)
#sml = cm3.SpeedMeter(15)
#car = cm3.Car(left, right, sml, smr)


dt = 0.1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

terminate = False
while not terminate:
    conn, addr = s.accept()

    request = str(conn.recv(1024))
    if request[7] == '?':
        params = find_params(request)
        for param in params:
            name, value = param.split('=')
            value = int(value)
            if name == 'LEFT':
                left.set(value)
            if name == 'RIGHT':
                right.set(value)
            if name == 'STOP':
                left.stop()
                right.stop()
            if name == 'END':
                terminate = True


    cm.feedback(conn, html)
    conn.close()
    utime.sleep(dt)

