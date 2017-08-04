import machine

class Motor(object):

    def __init__(self, pin):
        self.pin = pin
        self.motor = machine.PWM(machine.Pin(self.pin), freq=1000)
        self.direction = machine.Pin(self.pin, machine.Pin.OUT)


