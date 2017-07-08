import cm
import cm3
import socket
import network
import ubinascii
import utime


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
<td><button name="LEFT" value="ON" type="submit">ON</button></td>
</tr>
<tr>
<td>RIGHT:</td>
<td><button name="RIGHT" value="ON" type="submit">ON</button></td>
</tr>
<tr>
<td>DIRECTION:</td>
<td><button name="FORWARD" value="ON" type="submit">FORWARD</button></td>
<td><button name="STOP" value="ON" type="submit">STOP</button></td>
<td><button name="BACK" value="ON" type="submit">BACKWARD</button></td>
</tr>
<tr>
<td>END:</td> 
<td><button name="END" value="ON" type="submit">END</button></td>
</tr>
</table>
</form>
</html>
"""

utime.sleep(.5)

led.blink(6)

left = cm.Motor("left")
right = cm.Motor("right")
smr = cm3.SpeedMeter(16)
sml = cm3.SpeedMeter(15)
car = cm3.Car(left, right, sml, smr)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
terminate = False
while not terminate:
    conn, addr = s.accept()
    print("Connection from %s" % str(addr))
    request = str(conn.recv(1024))
    print("Content = %s" % request)

    LEFTON = request.find('/?LEFT=ON')
    RIGHTON = request.find('/?RIGHT=ON')
    FORWARD = request.find('/?FORWARD=ON')
    STOP = request.find('/?STOP=ON')
    BACK = request.find('/?BACK=ON')
    END = request.find('/?END=ON')

    direction = 'STOP'
    left_on = False
    right_on = False
    if LEFTON == 6:
        car.turn_angle(90)
        direction = 'LEFT'
    if RIGHTON == 6:
        car.turn_angle(-90)
        direction = 'LEFT'
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
    if END == 6:
        terminate = True

    cm.feedback(conn, html)
    conn.close()
    utime.sleep(0.2)
