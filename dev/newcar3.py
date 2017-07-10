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
<td><button name="TURN" value="90" type="submit">ON</button></td>
</tr>
<tr>
<td>RIGHT:</td>
<td><button name="TURN" value="-90" type="submit">ON</button></td>
</tr>
<tr>
<td>DIRECTION:</td>
<td><button name="FORWARD" value="10" type="submit">FORWARD</button></td>
<td><button name="STOP" value="ON" type="submit">STOP</button></td>
<td><button name="BACK" value="10" type="submit">BACKWARD</button></td>
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


def find_params(request):
    pos = request.find('?')+1
    a = request[pos:].split(" HTTP")[0]
    params = a.split('&')
    return (params)

left = cm.Motor("left")
right = cm.Motor("right")
smr = cm3.SpeedMeter(13)
sml = cm3.SpeedMeter(15)
car = cm3.Car(left, right, sml, smr)


dt = 0.2

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
terminate = False
while not terminate:

    print ("Waiting for connection")
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = str(conn.recv(1024))
    params = find_params(request)

    if request[7] == '?':

        print(params)

        for param in params:
            name, value = param.split('=')
            if name == 'STOP':
                car.stop()
                # right.stop()
                # left.stop()

            elif name == 'TURN':
                value = int(value)
                car.turn_angle(value)

            elif name == 'BACK':
                # value = int(value) # not yet used

                right.backward()
                left.backward()

            elif name == 'FORWARD':
                # value = int(value) # not yet used

                right.forward()
                left.forward()

            elif name == 'END':
                terminate = True

    cm.feedback(conn, html)
    conn.close()
    utime.sleep(dt)
