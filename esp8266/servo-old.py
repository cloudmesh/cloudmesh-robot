
class Servo_old(object):
    def __init__(self, pin, minimum=40, maximum=115):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        self.pin = pin_id(pin)
        self.servo = machine.PWM(machine.Pin(self.pin), freq=50)
        self.minimum = minimum
        self.maximum = maximum
        self.middle = int((maximum - minimum) / 2.0) + minimum

    def off(self):
        self.servo.duty(0)

    def set(self, value, dt=0.1):
        pos = value + self.minimum
        if self.minimum <= pos <= self.maximum:
            self.servo.duty(pos)
        utime.sleep(dt)
        self.off()

    def zero(self):
        self.low()

    def low(self):
        self.servo.duty(self.minimum)

    def high(self):
        self.servo.duty(self.maximum)

    def mean(self):
        self.servo.duty(self.middle)

    def swim(self, n, dt=0.1):
        self.zero()
        for i in range(0, n):
            self.low()
            utime.sleep(dt)
            self.off()
            self.high()
            utime.sleep(dt)
            self.zero()
            utime.sleep(dt)
            self.off()

    def info(self):
        d = {
            "pin": self.pin,
            "maximum": self.maximum,
            "minimum": self.minimum,
            "middle": self.middle,
            "value": 0.0
        }
        return d
