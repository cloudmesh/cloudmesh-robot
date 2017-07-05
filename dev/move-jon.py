from newcm import SpeedMeter
from newcm import Motor
from mmcar import DrivingRobot

car = DrivingRobot(SpeedMeter(15),
                   SpeedMeter(16),
                   Motor("left"),
                   Motor("right"),
                   45,
                   4,
                   '/dev/tty.usbmodemFD121'
                   )

car.drive_to(100, 100)
