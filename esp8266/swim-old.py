
LEFTON = request.find('/?LEFT=ON')
RIGHTON = request.find('/?RIGHT=ON')
MIDDLEON = request.find('/?MIDDLE=ON')
FORWARD = request.find('/?FORWARD=1')
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
