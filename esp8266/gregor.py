import cm
import network
import time
import socket

#led = cm.LED(2)

right = cm.Motor("right")
left = cm.Motor("left")

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

<title>Cloudmesh ESP8266 Car</title> 

</head>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Car Test</h2>
</center>
<form>
<center>

<table>

<tr>
<td></td>
<td><button name="FORWARD" value="ON" type="submit" >FORWARD</button></td>
<td></td>
</tr>

<tr>
<td><button name="LEFT" value="1000" type="submit">LEFT</button></td>
<td><button name="SPEED" value="0.100" type="submit">do not use</button></td>
<td><button name="SPEED" value="0.0" type="submit">do not use</button></td>
<td><button name="SPEED" value="100.0" type="submit">do not use</button></td>
</tr>

<tr>
<td></td>
<td><button name="BACKWARD" value="ON" type="submit">BACKWARD</button></td>
<td></td>
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
while True:
    i = i + 1
    conn, addr = s.accept()
    print ("I", i)

    request = str(conn.recv(1024))
    # print (request[7], request)
    #request = conn.recv(512)
    print (">", request[7], "?", "<", len(request))
    if request[7] == '?':
        print (">>>>>>>>>>>>>>>>>>>>>")

        params = find_params(request)
        for param in params:
            name, value = param.split('=')
            value = int(value)
            if name == 'LEFT':
                left.set(value)
            if name == 'RIGHT':
                right.set(value)



        #elif 6 == request.find('/?FORWARD'):

        #    pass

        #elif 6 == request.find('/?BACWARD'):

        #    pass

    cm.feedback(conn, html)

    conn.close()
