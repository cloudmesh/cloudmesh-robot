import utime
import machine

##############################################
# RPM METER MANAGEMENT
##############################################

class SpeedMeter(object):
    def __init__(self, pin):
        """
        SpeedMeter refers to the rpm meter on each wheel.
        :param pin: number of the pin
        """
        self.pin = machine.Pin(pin, machine.Pin.IN)

        self.status = pin.value(self.pin)
        self.counter = 0

    def update(self):
        self.status = self.pin.value(self.pin)

    def get(self):
        turn = True
        t0 = utime.ticks_ms()
        delta_t = 0
        count_start = self.counter
        while delta_t < 1000:
            self.update()
            if self.status == 1 and turn:
                turn = False
                self.counter += 1
            elif self.status == 0:
                turn = True
                delta_t = utime.ticks_diff(utime.ticks_ms(), t0)
        count_dt = self.counter - count_start
        print (count_dt)
        return count_dt
