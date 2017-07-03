import cm
import utime
import network
import ubinascii
import machine
import socket

led = cm.LED(2)

led.on()


fin = cm.Servo("D7")
fin.off()
pitch = cm.Servo("D8")
pitch.off()
#pitch.middle()

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

pitch.setangle(0, dt=1.0)
pitch.off()

angle = 0
print ("Angle", angle)

led.blink(2)


html = """<!DOCTYPE html>
<html>
<head> 
   <title>ESP8266 Fish</title> 
</head>
<body>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Fish</h2>
</center>
<form>
<center>
<button name="LEFT" value="ON" type="submit">LEFT</button></br>
<button name="RIGHT" value="ON" type="submit">RIGHT</button></br>
<button name="MIDDLE" value="ON" type="submit">MIDDLE</button></br>
<button name="STOP" value="ON" type="submit">STOP</button></br>
<button name="FORWARD" value="ON" type="submit">FORWARD</button></br>
<button name="UP" value="ON" type="submit" >UP</button></br>
<button name="EQUAL" value="ON" type="submit" >EQUAL</button></br>
<button name="DOWN" value="ON" type="submit">DOWN</button></br>
<button name="END" value="ON" type="submit">END</button></br>
</center>
</form>
</body>
</html>
"""

#p = pitch()

# Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)




terminate = False
while not terminate:
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
    UP = request.find('/?UP=ON')
    EQUAL = request.find('/?EQUAL=ON')
    DOWN = request.find('/?DOWN=ON')
    END = request.find('/?END=ON')

    direction = 'STOP'
    left_on = False
    right_on = False
    dt = 0.4
    if END == 6:
        terminate = True
        break;
    elif LEFTON == 6:
        fin.low()
        utime.sleep(dt)
        fin.off()
    elif RIGHTON == 6:
        fin.high()
        utime.sleep(dt)
        fin.off()
    elif MIDDLEON == 6:
        fin.zero()
        utime.sleep(dt)
        fin.off()
    elif STOP == 6:
        fin.off()
        utime.sleep(dt)
        fin.off()
    elif FORWARD == 6:
        fin.swim(1, 0.5)
        fin.off()
    elif UP == 6:
        print ('UP', angle)
        if angle <= 90:
            angle = angle + 45
            pitch.setangle(angle, dt=1.0)
            pitch.off()
    elif DOWN == 6:
        print ('DOWN', angle)
        if angle >= -90:
            angle = angle - 45
            pitch.setangle(angle, dt=1.0)
            pitch.off()
    elif EQUAL == 6:
        print('EQUAL', angle)
        pitch.setangle(0, 1.0)
        pitch.off()


    cm.feedback(conn, html)
    conn.close()
    utime.sleep(0.2)
