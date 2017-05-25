import time
import requests
import os

ips = ['10.0.1.16', '10.0.1.15']


def move(ip, direction):

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



filename="dance.txt"
f = open(filename)
lines = f.readlines()
f.close()

print ("LINES", lines)

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

