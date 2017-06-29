import network
import ubinascii
import time
import utime
import machine
#import socket
from machine import Pin, PWM

# BUG REUSE FROM CM?
class LED(object):
    """ associates an LED object with a pin"""
    # pin = 2
    def __init__(self, pin):
        self.light = machine.Pin(pin, machine.Pin.OUT)


    def on(self):
        """turns the LED on """
        self.light.low()

    def off(self):
        """turns the LED off """
        self.light.high()

    def blink(self, n):
        """flashes the LED n times"""
        for i in range(0,n):
            self.on()
            time.sleep(0.1)
            self.off()
            time.sleep(0.1)
            self.on()


class speed_meter(object):

    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.IN)
        self.status = Pin.value(self.pin)
        self.count = 0

# IS THIS THE SAME FROM CM, IF NOT YOU NEED DIFEFRENT NAME TO DISTIBUICH BETTER
class motor(object):


    def __init__(self, name):
        self.forward_speed = 1023
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0

        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name

    def forward(self):
        self.direction.low()
        self.duty(1023)

    def backward(self):
        self.direction.high()
        self.duty(1023)

    def stop(self):
        self.duty(0)

    def duty(self, d):
        PWM(Pin(self.pin_speed), freq=1000, duty=d)

    def set_forward_speed(self, duty):
        self.forward_speed = duty



smr = speed_meter(16)
#sml = speed_meter(15)
right = motor("right")
left = motor("left")
led = LED(2)
led.blink(5)



def rpm_finder():
    t0 = 0
    delta_t = 0
    while delta_t_r < 200000 and delta_t_l < 200000:
        if smr.status == 0:
            smr.count += 1
            delta_t_r = utime.ticks_diff(utime.ticks_us(), t0))
        if smr.status == 1:
            continue
#        if sml.status == 0:
#            sml.count += 1
#            delta_t_l = utime.ticks_diff(utime.ticks_us(), t0))
#        if sml.status == 1:
#            continue
    right_rotations = smr / 20
#    left_rotations = sml / 20
    rpm_r = right_rotations * 300
#    rpm_l = left_rotations * 300

def get_attributes(filename):
    f = open(filename)
    contents = f.read()
    f.close()
    # print (contents)
    contents.replace("\r\n", "\n")

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
</table>
</form>
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

    response = ''.join(html.split('\n')[1:])

    #blink (3)
    #time.sleep(0.5)


    response_headers = {
        'Content-Type': 'text/html; encoding=utf8',
        'Content-Length': len(response),
        'Connection': 'close',
    }


    # BUG THERE IS A FUNCTION FOR THIS IN CM
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

