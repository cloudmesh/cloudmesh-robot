import cm
import cm3
import socket
import network
import ubinascii
import utime

credentials = cm.get_attributes('credentials.txt')

ap_if = network.WLAN(network.AP_IF)

net = cm.connect()

mac = ubinascii.hexlify(network.WLAN().config('mac'), ':').decode()
print('mac')


def find_params(request):
    pos = request.find('?')+1
    a = request[pos:].split(" HTTP")[0]
    params = a.split('&')
    return (params)

left = cm.Motor("left")
right = cm.Motor("right")
smr = cm3.SpeedMeter(16)
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
