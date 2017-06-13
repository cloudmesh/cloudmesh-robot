# Making ESP8266 robots move straight.

In the method definitions of the `motor` class in car4.py, which you can download on [this](https://github.com/cloudmesh/cloudmesh.robot/tree/master/tests0), find the lines 42 to 48:

	def forward(self):
        self.direction.low()
        
        if self.name == "left":
            self.duty(1010)
        elif self.name == "right":
            self.duty(1023)
    
  If the car veers left, lower the value inside the parenthesis of the `self.duty()` function under `if self.name == "left": `. Contrarily, if the car veers right, lower the value inside the parenthesis of the `self.duty()` function under `if self.name == "right": `. Adjust these values until the robot car is able to drive straight, since each car is different, there is no universal **duty**, it varies for each robot. Lowering the duty makes the motor produce less power, so the robot will move more slowly as it is lowered. 1023 is the maximum duty amount.
