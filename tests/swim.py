import cm
import time
import network
import ubinascii
import time
import machine
import socket

led = cm.LED(2)

led.on()

fin = cm.Servo("D7")
pitch = cm.Servo("D8")

led.blink(1)

credentials = cm.get_attributes('credentials.txt')

print(credentials)

print('starting network ...')

credentials = cm.get_attributes('credentials.txt')

print(credentials)

#ap_if = network.WLAN(network.AP_IF)
#print(ap_if.active())
#print(ap_if.ifconfig())

led.blink(2)

net = cm.connect()

led.blink(5)

html = """<!DOCTYPE html>
<html>
<head> 
   <title>ESP8266 Fish</title> 
    <style>
        .btn {
          background: #3498db;
          background-image: -webkit-linear-gradient(top, #3498db, #2980b9);
          background-image: -moz-linear-gradient(top, #3498db, #2980b9);
          background-image: -ms-linear-gradient(top, #3498db, #2980b9);
          background-image: -o-linear-gradient(top, #3498db, #2980b9);
          background-image: linear-gradient(to bottom, #3498db, #2980b9);
          -webkit-border-radius: 28;
          -moz-border-radius: 28;
          border-radius: 28px;
          font-family: Arial;
          color: #ffffff;
          font-size: 60px;
          padding: 10px 20px 10px 20px;
          text-decoration: none;
        }
    
        .btn:hover {
          background: #3cb0fd;
          background-image: -webkit-linear-gradient(top, #3cb0fd, #3498db);
          background-image: -moz-linear-gradient(top, #3cb0fd, #3498db);
          background-image: -ms-linear-gradient(top, #3cb0fd, #3498db);
          background-image: -o-linear-gradient(top, #3cb0fd, #3498db);
          background-image: linear-gradient(to bottom, #3cb0fd, #3498db);
          text-decoration: none;
        }
    </style>
</head>
<body>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Fish</h2>
</center>
<form>
<button name="LEFT" value="ON" type="submit">ON</button></br>
<button name="RIGHT" value="ON" type="submit">ON</button></br>
<button name="MIDDLE" value="ON" type="submit">ON</button></br>
<button name="STOP" value="ON" type="submit">STOP</button></br>
<button name="FORWARD" value="ON" type="submit">FORWARD</button></br>
</form>
</body>
</html>
"""

# Setup Socket WebServer
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
    MIDDLEON = request.find('/?MIDDLE=ON')
    FORWARD = request.find('/?FORWARD=ON')
    STOP = request.find('/?STOP=ON')

    direction = 'STOP'
    left_on = False
    right_on = False
    if LEFTON == 6:
        fin.low()
    if RIGHTON == 6:
        fin.high()
    if MIDDLEON == 6:
        fin.mean()
    if STOP == 6:
        fin.off()
    if FORWARD == 6:
        fin.swim(1, 0.5)

    response = ''.join(html.split('\n')[1:])

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
    conn.close()
