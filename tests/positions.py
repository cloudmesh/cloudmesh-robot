import sys
import time
# import requests
from marvelmindcoordinates import MarvelmindHedge
from pprint import pprint
from cloudmesh.common.Printer import Printer


class PositioningSystem(object):
    def __init___(self, tty='/dev/tty.usbmodemFD121'):
        self.tty = tty
        self.beacon = {}
        self.id = 0
        self.robot = MarvelmindHedge(self.tty)

    def status(self):
        # x,y
        pass

    # TODO: implement
    def export(self, filename):
        # file open or with statment
        for name in self.beacon:
            for element in ['name', 'x', 'y']:
                print (name,)
                print (x,)
                print (y)
                # change this at one point so it prints this to a file
                # close file

    def register(self, addr, name, kind='mobile'):
        addr, x, y, z, t = self.robot
        self.beacon[name] = {
            'name': name,
            'kind': kind,
            'addr': addr,
            'x': x,
            'y': y,
            'id': self.id
        }
        self.id = self.id + 1

    def lookup(self, addr):
        for i in self.beacon:
            if self.beacon[i]['addr'] == addr:
                return self.beacon[i]
        return None

        # def reset():
        # set all positions to some vale within the fixedbecona
        # pass

        # def info(self, kind='mobile'):
        # mobile, all, stationarty

        # dependent on type returns info about the beacons
        # not sure how to implement yet

        # def count(self, type= ....)
        # retusn number of beacons found

        # def set_count(stationary, mobile)
        # instead of probing the beacons hard code the set count
        # so we can figure out if we have power issue

        # def probe (id):
        # similar to get but with more info get just gives xy


positions = PositioningSystem()

print (positions.tty)
print (positions.beacon)

positions.register("Hedge 1", "robi15")
positions.register("Hedge 3", "robi16")

print(positions.beacon)

print(Printer.dict(positions.beacon, order=['id', 'name', 'kind', 'x', 'y', 'addr']))

# positions = robot.position()

sys.exit(0)
# robot = MarvelmindHedge(tty='/dev/tty.usbmodemFD121')


"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


# def move(ip, direction, epsilon=0.0001):
#    if direction == 'left':
#        payload = {'LEFT': 'ON'}
#    elif direction == 'right':
#        payload = {'RIGHT': 'ON'}
#    elif  direction == 'stop':
#        payload = {'STOP': 'ON'}
#    elif direction == 'forward':
#        payload = {'FORWARD': 'ON'}
#    elif direction == 'backward':
#        payload = {'BACK': 'ON'}
#    else:
#        print ("ERROR: unkown direction:", direction)
#    try:
#        headers = {'User-Agent': "Car"}
#        r = requests.get('http://' + ip, headers=headers, params=payload)
#    except Exception as e:
#        print (type(e), e)
