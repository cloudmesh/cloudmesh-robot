import time
import requests
import os
from cloudmesh.common import Parameter

ips = ['10.0.1.19']


class Swarm(object):

    def __init__(self, environment=None):
        if environment is None:
            environment = "turtle"
        self.mode(environment)


    def mode(self, name):
        environment = name

    def move(ip, direction):

        if self.environment == "robot":
            if direction == 'left':
                payload = {'LEFT': 'ON'}
            elif direction == 'right':
                payload = {'RIGHT': 'ON'}
            elif  direction == 'stop':
                payload = {'STOP': 'ON'}
            elif direction == 'forward':
                payload = {'FORWARD': 'ON'}
            elif direction == 'backward':
                payload = {'BACK': 'ON'}
            else:
                print ("ERROR: unkown direction:", direction)

            try:
                headers = {'User-Agent': "Car"}
                r = requests.get('http://' + ip, headers=headers, params=payload)
            except Exception as e:
                print (type(e), e)
        elif self.environment ==  "turtle":
            pass

    def dance(self, filename):
        filename="dance.txt"
        f = open(filename)
        self.lines = f.readlines()
        f.close()
        print ("LINES", self.lines)

    def run(self):
        for line in lines:
            direction, duration = line.strip().split(' ')
            duration = float(duration)
            print (">", direction, "><", duration, ">")
            for ip in ips:
                move(ip, direction)
            time.sleep(duration)
            for ip in ips:
                move(ip, "stop")

        direction = "stop"
        for ip in ips:
            move(ip, direction)

