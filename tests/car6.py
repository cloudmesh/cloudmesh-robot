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
        """flashes the LED n times
"""
    	for i in range(0,n):
        	self.on()
       	 	time.sleep(0.1)
        	self.off()
        	time.sleep(0.1)




class motor(object):
    """the motor class has the name attribute and a forward duty and backward duty"""


    def __init__(self, name, forward_duty=1023, backward_duty=1023):
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
        """ """
        PWM(Pin(self.pin_speed), freq=1000, duty=d)


led = LED(2)
right = motor("right")
left = motor("left")


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
<td>DIRECTION:</td>
<td><button name="FORWARD" value="ON" type="submit">FORWARD</button></td>
<td><button name="STOP" value="ON" type="submit">STOP</button></td>
<td><button name="BACK" value="ON" type="submit">BACKWARD</button></td>
</tr>
<tr>
<td>TLF:</td>
<td><button name="TUNE LEFT FORWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE LEFT FORWARD" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>TRF:</td>
<td><button name="TUNE RIGHT FORWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE RIGHT FORWARD" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>TLB:</td>
<td><button name="TUNE LEFT BACKWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE LEFT BACKWARD" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>TRB:</td>
<td><button name="TUNE RIGHT BACKWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE RIGHT BACKWARD" value="OFF" type="submit">OFF</button></td>
</tr>
</table>
</form>
<h3>Tune</h3>

</html>
"""

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
    TLF = request.find('/?TLF=ON')
    TRF = request.find('/?TRF=ON')
    TLB = request.find('/?TLB=ON')
    TRB = request.find('/?TRB=ON')


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
    if TLF == 6:
        right.forward_duty -= 1
    if TRF == 6:
        left.forward_duty -= 1
    if TLB == 6:
        right.backward_duty -= 1
    if TRB == 6:
        left.backward_duty -= 1
        
        

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

