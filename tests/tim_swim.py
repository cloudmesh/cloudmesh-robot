import tim_cm as cm
import utime
#import network
#import ubinascii
#import machine
import socket

led = cm.LED(2)

led.on()


fin = cm.Servo("D7")
fin.off()
pitch = cm.Servo("D8")
pitch.off()

led.blink(1)

print('starting network ...')

credentials = cm.get_attributes('credentials.txt')

print(credentials)

led.blink(2)

net = cm.connect()

led.blink(5)

pitch.setangle(0, dt=1.0)
pitch.off()

angle = 0
print ("Angle", angle)

led.blink(2)

# Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def find_params(request):
    pos = request.find('?')+1
    a = request[pos:].split(" HTTP")[0]
    params = a.split('&')
    return (params)

fin_zero = 0
fin_left = 90
fin_right = -90

pitch_zero = 0
pitch_dt = 10

dt = 0.5
dt_angle = 1.0
terminate = False
while not terminate:
    print ("Waiting for connection")
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = str(conn.recv(1024))
    params = find_params(request)

    if request[7] == '?':
        for param in params:
            name, value = param.split('=')
            if name == 'STOP':
                fin.off()
                pitch.off()
                utime.sleep(dt)
            if name == 'LEFT':
                fin.low()
                utime.sleep(dt)
                fin.off()
            elif name == 'RIGHT':
                fin.high()
                utime.sleep(dt)
                fin.off()
            elif name == 'MIDDLE':
                fin.zero()
                utime.sleep(dt)
                fin.off()
            elif name == 'SWIM':
                print('SWIM', value)
                value = int(value)
                fin.swim(value, dt)
                fin.off()
            if name == 'UP':
                print('UP', angle)
                if angle <= 90:
                    angle = angle + 45
                    pitch.setangle(angle, dt=dt_angle)
                    pitch.off()
            elif name == 'DOWN':
                print('DOWN', angle)
                if angle >= -90:
                    angle = angle - 45
                    pitch.setangle(angle, dt=dt_angle)
                    pitch.off()
            elif name == 'EQUAL':
                print('EQUAL', angle)
                pitch.setangle(0, dt_angle)
                pitch.off()
            elif name == 'ANGLE':
                print('ANGLE', value)
                fin.set(int(value), 1)
                fin.off()
            elif name == 'OFFSET':
                print('OFFSET', value)
                fin.set_offset(int(value))
            
            if name == 'END':
                terminate = True

    cm.feedback(conn)
    conn.close()
    utime.sleep(0.2)
