import time
import requests
import os
from marvelmind import MarvelmindHedge


def move(ip, direction, epsilon=0.0001):
    """
    Moves robot through web server
    :param ip: String
    :param direction: String
    :param epsilon: String
    """
    if direction == 'left':
        payload = {'LEFT': 'ON'}
    elif direction == 'right':
        payload = {'RIGHT': 'ON'}
    elif direction == 'stop':
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

