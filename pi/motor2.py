import RPi.GPIO as gpio
import time


def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)

'''    
def forward(tf):
    init()
    gpio.output(17, True)
    gpio.output(22, False)
    gpio.output(23, True) 
    gpio.output(24, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(17, False)
    gpio.output(22, True)
    gpio.output(23, False) 
    gpio.output(24, True)
    time.sleep(tf)
    gpio.cleanup()

print "forward"
forward(4)
print "backward"
reverse(2)
'''

init()


left = gpio.PWM(17, 50.0)
left.start(1)
right = gpio.PWM(23, 50.0)
right.start(1)

direction = False
gpio.output(24, direction)
gpio.output(22, direction)

for i in range(0,100):
   speed = float(i)
   print(speed)
   left.ChangeDutyCycle(speed)
   right.ChangeDutyCycle(speed)
   time.sleep(0.5)
gpio.cleanup()

