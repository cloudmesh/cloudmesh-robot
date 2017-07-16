from newcm import SpeedMeter
from newcm import Motor
from newcm import LED
from mmcar import DrivingRobot
from time import sleep

car = DrivingRobot(SpeedMeter(15),
                   SpeedMeter(16),
                   Motor("left"),
                   Motor("right"),
                   '/dev/tty.usbmodemFD121'
                   )

led = LED(2)
led.blink(5)
sleep(10)
car.drive_to(100, 100)
