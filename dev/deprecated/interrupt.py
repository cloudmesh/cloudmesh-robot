from machine import Pin


def callback(r):
    print('interrupt')

p = Pin(15, Pin.IN, Pin.PULL_UP)

p.irq(trigger=Pin.IRQ_RISING, handler=callback)
