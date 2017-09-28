import cm
import cm3
import socket
import network
import ubinascii
import utime

led = cm.LED(2)
left = cm.Motor("left")
right = cm.Motor("right")
smr = cm3.SpeedMeter(16)
sml = cm3.SpeedMeter(15)
car = cm3.Car(left, right, sml, smr)

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
<td>CALIBRATION:</td>
<td><button name="CALIBRATE" value="ON" type="submit">CALIBRATE</button></td>
</tr>
</table>
</form>
</html>
"""

utime.sleep(.5)

led.blink(6)

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
    CAL = request.find('/?CALIBRATE=ON')

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
    if CAL == 6:
        car.calibrate_forward()

    response = ''.join(html.split('\n')[1:])

    #blink (3)
    #time.sleep(0.5)


    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(response),
        'Connection': 'close',
    }


    response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in response_headers.items())


    # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
    response_proto = 'HTTP/1.1'
    response_status = '200'
    response_status_text = 'OK'  # this can be random

    # sending all this stuff
    conn.send('%s %s %s' % (response_proto, response_status, response_status_text))
    conn.send(response_headers_raw)
    conn.send('\n')  # to separate headers from body


    conn.send(response)
    #blink (5)
    #time.sleep(0.5)

    conn.close()
