#
# cp car-speed.py main.py;  cms robot put -o main.py
#
import cm
import cm3
import network
import time
import socket

#led = cm.LED(2)

right = cm.Motor("right")
left = cm.Motor("left")

smr = cm3.SpeedMeter(16)
sml = cm3.SpeedMeter(15)
car = cm3.Car(left, right, sml, smr)

#led.blink(5)

credentials = cm.get_attributes('credentials.txt')

print(credentials)

print('starting network ...')

credentials = cm.get_attributes('credentials.txt')

print(credentials)

# led.blink(2)

net = cm.connect()

# led.blink(5)


html = """<!DOCTYPE html>
<html>
<head> 

<title>Cloudmesh ESP8266 Car Angle</title> 

</head>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Car Test</h2>
</center>
<form>
<center>

<table>

<tr>
<td><button name="LEFT" value="-90" type="submit">LEFT</button></td>
<td><button name="RIGHT" value="90" type="submit">RIGHT</button></td>
<td><button name="END" value="ON" type="submit">END</button></td>
</tr>

</table>
<center>
</form>
</html>
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def find_params(request):
    pos = request.find('?')+1
    a = request[pos:].split(" HTTP")[0]
    params = a.split('&')
    return (params)

i = 0

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
                car.turn_angle(value)
                #left.set(value)
            if name == 'RIGHT':
                car.turn_angle(value)
                #right.set(value)
            if name == 'END':
                terminate = True

    cm.feedback(conn, html)

    conn.close()
