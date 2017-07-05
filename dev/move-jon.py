from newcm import SpeedMeter
from newcm import Motor
from mmcar import DrivingRobot

car = DrivingRobot(SpeedMeter(15),
                   SpeedMeter(16),
                   Motor("left"),
                   Motor("right"),
                   '/dev/tty.usbmodemFD121',
                   45,
                   4,
                   )

car.drive_to(100, 100)
