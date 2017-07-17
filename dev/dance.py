import requests
import time


ips = ['10.0.1.104',
       '10.0.1.118']

class Swarm(object):

    def __init__(self, ips):
        self.ips = ips
        filename = "dance.txt"
        f = open(filename)
        self.lines = f.readlines()
        f.close()
        print ("LINES", self.lines)

    def move(self, direction, ip):

        if direction == "left":
            payload = {'LEFT': 'ON'}
        elif direction == "right":
            payload = {'RIGHT': 'ON'}
        elif direction == "forward":
            payload = {'FORWARD': 'ON'}
        elif direction == "stop":
            payload = {'STOP': 'ON'}
        elif direction == "backward":
            payload = {'BACKWARD': 'ON'}
        else:
            print ("ERROR: unknown direction:", direction)

        try:
            headers = {'User-Agent': "Car"}
            r = requests.get('http://' + ip, headers=headers, params=payload)
        except Exception as e:
            print (type(e), e)

    def run(self):
        for line in self.lines:
            direction, duration = line.strip().split(' ')
            duration = float(duration)
            print (">", direction, "><", duration, ">")
            for ip in ips:
                print(ip, direction)
                self.move(ip, direction)
            time.sleep(duration)
            for ip in ips:
                print('stop ', ip)
                self.move(ip, "stop")
