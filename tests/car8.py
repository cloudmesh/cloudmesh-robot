import network
import ubinascii
import time
import machine
import socket
from machine import Pin, PWM




class LED(object):
    """ creates an LED with a pin attribute 
"""
    # pin = 2
    def __init__(self, pin):
        self.light = machine.Pin(pin, machine.Pin.OUT)


    def on(self):
        """turns the LED on
        """
        self.light.low()

    def off(self):
        """turns the LED off
        """
        self.light.high()

    def blink(self, n):
        """flashes the LED n times"""
        for i in range(0,n):
            self.on()
            time.sleep(0.1)
            self.off()
            time.sleep(0.1)
            self.on()




class motor(object):
    """the motor class has the name attribute and a forward duty and backward duty"""


    def __init__(self, name, forward_duty, backward_duty):
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0

        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name
        self.forward_duty = forward_duty
        self.backward_duty = backward_duty

    def forward(self):
        """turns a motor on in the forward direction"""
        self.direction.low()
        self.duty(self.forward_duty)

    def backward(self):
        """turns a motor on in the backward direction"""
        self.direction.high()
        self.duty(self.backward_duty)

    def stop(self):
        """stops a motor"""
        self.duty(0)

    def duty(self, d):
        """specifies the duty associated with the pin """
        PWM(Pin(self.pin_speed), freq=1000, duty=d)


led = LED(2)
right = motor("right", 1023, 1023)
left = motor("left", 1023, 1023)


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

<center>
<form>
<table>
<td></td><td></td>
<td><button name="FORWARD" value="ON" type="submit">FORWARD</button></td>
<td></td><td></td>

</tr>
<tr>
<td><button name="LEFT" value="ON" type="submit">LEFT ON</button></td>
<td><button name="LEFT" value="OFF" type="submit">LEFT OFF</button></td>
<td><center><button name="STOP" value="ON" type="submit">STOP</button></center></td>
<td><button name="RIGHT" value="ON" type="submit">RIGHT ON</button></td>
<td><button name="RIGHT" value="OFF" type="submit">RIGHT OFF</button></td>

</tr>
<td></td><td></td>
<td><button name="BACK" value="ON" type="submit">BACKWARD</button></td>
<td></td><td></td>
<tr>

</tr>
</table>
</form>
</center>

<center>
<h2>Tune</h2>
</center>

<center>
<form>
<table>
	<tr>
  <td>LEFT MOTOR DUTY:</td>
  <td><button name="SUBHL" value="ON" type="submit"><<</button></td>
  <td><button name="SUBSL" value="ON" type="submit"><</button></td>
  <td> <input type= number name= "LMD" value='""" + str(left.forward_duty) + """'> </td>
  <td><button name="ADDSL" value="ON" type="submit">></button></td>
  <td><button name="SUBSL" value="ON" type="submit">>></button></td>
    </tr>
  </table>
  
<table>
	<tr>
  <td>RIGHT MOTOR DUTY:</td>
  <td><button name="SUBHR" value="ON" type="submit"><<</button></td>
  <td><button name="SUBSR" value="ON" type="submit"><</button></td>
  <td> <input type= number name= "RMD" value='""" + str(right.forward_duty) + """'> </td>
  <td><button name="ADDSR" value="ON" type="submit">></button></td>
  <td><button name="ADDHR" value="ON" type="submit">>></button></td>
    </tr>
  </table>
</form>
</center>

</html>"""

led.blink(5)

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
    FORWARD = request.find('/?FORWARD=ON')
    STOP = request.find('/?STOP=ON')
    BACK = request.find('/?BACK=ON')
    SUBHL = request.find('/?SUBHL=ON')
    SUBSL = request.find('/?SUBSL=ON')
    ADDHL = request.find('/?ADDHL=ON')
    ADDSL = request.find('/?ADDSL=ON')
    SUBHR = request.find('/?SUBHR=ON')
    SUBSR = request.find('/?SUBSR=ON')
    ADDHR = request.find('/?ADDHR=ON')
    ADDSR = request.find('/?ADDSR=ON')


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
    if SUBHL == 6:
        left.forard_duty -= 5
    if SUBSL == 6:
        left.forward_duty -= 1
    if ADDHL == 6:
        left.forward_duty += 5
    if ADDSL == 6:
        left.forward_duty += 1
    if SUBHR == 6:
        right.forward_duty -= 5
    if SUBSR == 6:
        right.forward_duty -= 1
    if ADDHR == 6:
        right.forward_duty += 5
    if ADDSR == 6:
        right.forward_duty += 1
    
        
        

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

