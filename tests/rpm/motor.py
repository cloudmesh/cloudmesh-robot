class Motor(object):
    """the motor class has the name attribute and a forward duty and backward duty"""

    def __init__(self, name):
        """Sets up two motors for a robot car
        :param name: left or right
        """
        if name == "left":
            self.pin_speed = 4
            self.pin_direction = 2
        elif name == "right":
            self.pin_speed = 5
            self.pin_direction = 0
        self.motor = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.d = 1023
        self.speed = PWM(Pin(self.pin_speed), freq=1000, duty=0)
        self.direction = Pin(self.pin_direction, Pin.OUT)
        self.name = name

    def forward(self):
        self.direction.low()
        self.speed.duty(self.d)

    def backward(self):
        self.direction.high()
        self.speed.duty(self.d)

    def stop(self):
        self.speed.duty(0)

    def dutyset(self, value):
        if 0 <= value <= 1023:
            self.d = value
