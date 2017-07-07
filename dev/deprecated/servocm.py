import utime
import machine

from cm import p


from cm import pin_id


##############################################
# SERVO
##############################################

class Servo(object):
    def __init__(self, pin, minimum=29, maximum=115):
        """
        define an LED on a given pin
        :param pin: the number of the pin
        """
        pin = pin_id(pin)
        self.servo = machine.PWM(machine.Pin(pin), freq=50)
        self.minimum = minimum
        self.maximum = maximum
        self.middle = int((maximum - minimum) / 2) + minimum
        self.servo.duty(self.middle)
        self.position = self.middle
        self.atdratio = 180 / (maximum - minimum)
        self.dtaratio = (maximum - minimum) / 180

    def off(self):
        self.servo.duty(0)

    def set(self, value, dt):
        if self.minimum <= value <= self.maximum:
            self.servo.duty(value)
        utime.sleep(dt)
        self.position = value

    def zero(self):
        self.servo.duty(self.middle)
        self.position = self.middle

    def low(self):
        self.servo.duty(self.minimum)
        self.position = self.minimum

    def high(self):
        self.servo.duty(self.maximum)
        self.position = self.maximum

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

    def angletoduty(self, angl):
        return round((self.dtaratio * angl), 0)

    def dutytoangle(self, d):
        return round((self.atdratio * d), 0)

    def setangle(self, value, time):
        sp = self.position
        ep = self.angletoduty(value) + self.middle
        dd = ep - sp
        if dd != 0:
            dt = abs(time / dd)
            print('dt: ' + str(dt))
        else:
            return
        if dd < 0:
            for i in range(0, abs(dd)):
                print(i)
                cp = sp - i
                self.set(cp, dt)
        elif dd > 0:
            for i in range(0, dd):
                print(i)
                cp = sp + i
                self.set(cp, dt)


s = Servo('D7')


