from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import machine
import micropython
import cm

led = cm.LED(2)

SERVER = "PUTSERVERIPHERE"

CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"led"


state = 0

def led_callback(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(0)
        state = 1
    elif msg == b"off":
        led.value(1)
        state = 0
    elif msg == b"toggle":
        led.value(state)
        state = 1 - state


def main(server=SERVER):
    client = MQTTClient(CLIENT_ID, server)
    client.set_callback(led_callback)
    client.connect()
    client.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    try:
        while 1:
            #micropython.mem_info()
            client.wait_msg()
    finally:
        client.disconnect()