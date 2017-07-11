import cm3
from marvelmind.marvelmind import MarvelmindHedge

#left = cm.Motor("left")
#right = cm.Motor("right")


filename = "move-algorithm.txt"
f = open(filename)
lines = f.readlines()
f.close()

for line in lines:
    name, position = line.split(":")
    endx, endy = position.split(" ")
    print(name, position)
    print(endx, endy)

hedgeswarm = MarvelmindHedge(tty='/dev/tty.usbmodem1421')
ips = ['10.0.1.116',
       '10.0.1.118']

class DrivingRobot(object):

    def __init__(self, hedgenumber, ip):
        self.number = hedgenumber
        self.ip = ip
        self.addr, self.x0, self.y0, self.z0, self.t0 = hedgeswarm.number_position(self.number)

    def set_line(self, x0, y0, fx, fy):
        slope = (fy - y0) / (fx - x0)
        intercept = y0 - (x0 * slope)
        return slope, intercept

    def xexp(self, m, b, y):
        ex = (y - b) / m
        return ex

    def turn(self, endx, endy):


