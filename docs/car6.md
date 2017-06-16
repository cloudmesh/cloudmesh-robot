# Changes made in car6.py

Today we edited the car4.py program to allow users to tune the robots to go straight through the website.

The first change we made was to the LED class. We made the "blink" function into a method of the LED class.

	class LED(object):
    
    	# pin = 2
    def __init__(self, pin):
        self.light = machine.Pin(pin, machine.Pin.OUT)


    def on(self):
        """turns the LED on
        """
        self.light.low()

    def off(self):
        """turns the LED off
        """
        self.light.high()
        
	def blink(self, n):
        """flashes the LED n times
        """
    	for i in range(0,n):
        	self.on()
       	 	time.sleep(0.1)
        	self.off()
        	time.sleep(0.1)
            self.on()
We next gave the motor class two more attributes:
foreward\_duty  
backward\_duty  
so that they can be tweaked by the program later.

We next edited the webpage to add four new buttons: one to adjust the car leftward when it moves forward, one to adjust it rightward when it moves foreward, and two to do the same as it moves backward. The html code now looks as follows:

html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 Car</title> </head>
<center>
<h3>Cloudmesh.robot</h3>
<h2>ESP8266 Car Test</h2>
</center>
<form>
<table>
<tr>
<td>LEFT:</td> 
<td><button name="LEFT" value="ON" type="submit">ON</button></td>
<td><button name="LEFT" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>RIGHT:</td>
<td><button name="RIGHT" value="ON" type="submit">ON</button></td>
<td><button name="RIGHT" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>DIRECTION:</td>
<td><button name="FORWARD" value="ON" type="submit">FORWARD</button></td>
<td><button name="STOP" value="ON" type="submit">STOP</button></td>
<td><button name="BACK" value="ON" type="submit">BACKWARD</button></td>
</tr>
<tr>
<td>TLF:</td>
<td><button name="TUNE LEFT FORWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE LEFT FORWARD" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>TRF:</td>
<td><button name="TUNE RIGHT FORWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE RIGHT FORWARD" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>TLB:</td>
<td><button name="TUNE LEFT BACKWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE LEFT BACKWARD" value="OFF" type="submit">OFF</button></td>
</tr>
<tr>
<td>TRB:</td>
<td><button name="TUNE RIGHT BACKWARD" value="ON" type="submit">ON</button></td>
<td><button name="TUNE RIGHT BACKWARD" value="OFF" type="submit">OFF</button></td>
</tr>
</table>
</form>
<h3>Tune</h3>

</html>
"""
 
 The python code accepts the inputs as 
  
 	TLF = request.find('/?TLF=ON')  
 	TRF = request.find('/?TRF=ON')
 	TLB = request.find('/?TLB=ON')
 	TRB = request.find('/?TRB=ON')
andit interprets the code by changing the attribute value of the left or right motor object in order to adjust the direction.

    if TLF == 6:
        right.forward_duty -= 1
    if TRF == 6:
        left.forward_duty -= 1
    if TLB == 6:
        right.backward_duty -= 1
    if TRB == 6:
        left.backward_duty -= 1
 
The code did not successfully run on the robot for an unknown reason. 
 
	

