import utime
import machine
import math

##############################################
# RPM MANAGEMENT
##############################################


class SpeedMeter(object):

    def __init__(self, pin):
        self.pin = machine.Pin(pin, machine.Pin.IN)
        self.status = self.pin.value()
        self.counter = 0

    def update(self):
        self.status = self.pin.value()

    def get(self):
        turn = True
        t0 = utime.ticks_ms()
        delta_t = 0
        count_start = self.counter
        while delta_t < 2000:
            self.update()
            if self.status == 1 and turn:
                turn = False
                self.counter += 1
            elif self.status == 0:
                turn = True
                delta_t = utime.ticks_diff(utime.ticks_ms(), t0)
        count_dt = self.counter - count_start
        return count_dt

    def rpm(self):
        return (self.get() / 20) * 300

    def wait_ticks(self, ticks):
        turn = True
        cticks = 0
        while cticks < ticks:
            self.update()
            if self.status == 1 and turn:
                turn = False
                cticks += 1
            elif self.status == 0:
                turn = True


##############################################
# RPM MANAGEMENT
##############################################


class Car(object):

    def __init__(self,
                 leftmotor,
                 rightmotor,
                 leftspeedmeter,
                 rightspeedmeter
                 ):
        """
        Consolidates robot parts to one object
        :param leftmotor: Motor
        :param rightmotor: Motor
        :param leftspeedmeter: SpeedMeter
        :param rightspeedmeter: SpeedMeter
        """
        self.left = leftmotor
        self.right = rightmotor
        self.sml = leftspeedmeter
        self.smr = rightspeedmeter

    def turn_angle(self, angle):
        """
        Turns robot given angle. Turn left with negative. Turn right with positive.
        :param angle: Number (angle in degrees)
        """
        ticks = abs(((((angle * math.pi) / 180) * 13.6) / (6.7 * math.pi)) * 20)
        if angle < 0:
            self.right.forward(800)
            self.smr.wait_ticks(ticks)
            self.right.stop()
        elif angle > 0:
            self.left.forward(800)
            self.sml.wait_ticks(ticks)
            self.left.stop()

    def carstop(self):
        self.left.stop()
        self.right.stop()

    def calibrate_forward(self):
        left_count = 0
        right_count = 1
        while left_count != right_count:
            self.left.forward()
            self.right.forward()
            left_count = self.sml.get()
            right_count = self.smr.get()
            if left_count < right_count:
                if self.left.d < 1023:
                    self.carstop()
                    self.left.d += 2
                    self.turn_angle(180)
                    print("A")
                    print("left: " + str(left_count))
                    print("right: " + str(right_count))
                else:
                    self.carstop()
                    self.right.d -= 5
                    self.turn_angle(180)
                    print("B")
                    print("left: " + str(left_count))
                    print("right: " + str(right_count))
            elif right_count > left_count:
                if self.right.d < 1023:
                    self.carstop()
                    self.right.d += 2
                    self.turn_angle(180)
                    print("C")
                    print("left: " + str(left_count))
                    print("right: " + str(right_count))
                else:
                    self.carstop()
                    self.left.d -= 5
                    self.turn_angle(180)
                    print("D")
                    print("left: " + str(left_count))
                    print("right: " + str(right_count))
        self.carstop()


##############################################
# DrivingRobot
##############################################


def set_line(x0, y0, fx, fy):
    slope = (fy - y0) / (fx - x0)
    intercept = y0 - (x0 * slope)
    return slope, intercept

