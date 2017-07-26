Intro

Electronics: http://www.instructables.com/id/Basic-Electronics/
Volatage: https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law
Unix: http://www.ee.surrey.ac.uk/Teaching/Unix/index.html

* [grove examples](https://github.com/DexterInd/GrovePi/tree/master/Software/Python)

Buzzer
======
 
The Grove - [Buzzer](http://wiki.seeed.cc/Grove-Buzzer/) module has a piezo buzzer as the main component. The piezo can be connected to digital outputs, and will emit a tone when the output is HIGH. Alternatively, it can be connected to an analog pulse-width modulation output to generate various tones and effects. The following describes a digital configuration for the buzzer. To begin, plug the buzzer into the D8 port. In this configuration, it has two settings, on and off. Notice that the code for the digital Buzzer is the same as the code for the digital LED.

Simple
------

	# GrovePi + Grove Buzzer
	import time
	import grovepi
	
	# connect the buzzer to pin 4
	
	class Buzzer(object):
	
	    def __init__(self, pin):
	        self.pin = pin
	        grovepi.pinMode(self.pin, "OUTPUT")
	
	    def buzz(self, n):
	        for n in range(0, n):
	            try:
	                # Blink the LED
	                grovepi.digitalWrite(self.pin, 1)  # Send HIGH to switch on Buzzer
	                print ("LED ON!")
	                time.sleep(1)
	
	                grovepi.digitalWrite(self.pin, 0)  # Send LOW to switch off Buzzer
	                print ("LED OFF!")
	                time.sleep(1)
	
	            except KeyboardInterrupt:  # Turn LED off before stopping
	                grovepi.digitalWrite(self.pin, 0)
	                break
	            except IOError:  # Print "Error" if communication error encountered
	                print ("Error")
	
	buzzer = Buzzer(4)
	buzzer.buzz(5)

Buzzer
------

[Buzzer](http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/)  
To set up the buzzer in the analog configuration, connect the red voltage wire to the GPIO Pin 5 and the black ground wire to the GPIO ground. The following code defines the buzzer class, which includes a buzz method and a play method. The buzz method plays the given pitch for the given duration, and the play method plays one of five precoded tunes, depending on the method's argument.

	import RPi.GPIO as GPIO   #import the GPIO library
	import time               #import the time library

	class Buzzer(object):
 		def __init__(self):
  			GPIO.setmode(GPIO.BCM)  
  			self.buzzer_pin = 5 #set to GPIO pin 5
  			GPIO.setup(self.buzzer_pin, GPIO.IN)
  			GPIO.setup(self.buzzer_pin, GPIO.OUT)
			print("buzzer ready")
				
 		def __del__(self):
  			class_name = self.__class__.__name__
  			print (class_name, "finished")

 		def buzz(self,pitch, duration):   #create the function “buzz” and feed it the pitch and duration)
 
  			if(pitch==0):
   				time.sleep(duration)
   				return
  			period = 1.0 / pitch     #in physics, the period (sec/cyc) is the inverse of the frequency (cyc/sec)
  			delay = period / 2     #calcuate the time for half of the wave  
  			cycles = int(duration * pitch)   #the number of waves to produce is the duration times the frequency

  			for i in range(cycles):    #start a loop from 0 to the variable “cycles” calculated above
   				GPIO.output(self.buzzer_pin, True)   #set pin 18 to high
   				time.sleep(delay)    #wait with pin 18 high
   				GPIO.output(self.buzzer_pin, False)    #set pin 18 to low
   				time.sleep(delay)    #wait with pin 18 low

 		def play(self, tune):
  			GPIO.setmode(GPIO.BCM)
  			GPIO.setup(self.buzzer_pin, GPIO.OUT)
 			x=0

  			print("Playing tune ",tune)
  			if(tune==1):
    			pitches=[262,294,330,349,392,440,494,523, 587, 659,698,784,880,988,1047]
    			duration=0.1
    			for p in pitches:
      				self.buzz(p, duration)  #feed the pitch and duration to the function, “buzz”
      				time.sleep(duration *0.5)
    			for p in reversed(pitches):
     				self.buzz(p, duration)
      				time.sleep(duration *0.5)

  			elif(tune==2):
    			pitches=[262,330,392,523,1047]
    			duration=[0.2,0.2,0.2,0.2,0.2,0,5]
   				for p in pitches:
     				self.buzz(p, duration[x])  #feed the pitch and duration to the function, “buzz”
      				time.sleep(duration[x] *0.5)
      				x+=1
  			elif(tune==3):
   				pitches=[392,294,0,392,294,0,392,0,392,392,392,0,1047,262]
    			duration=[0.2,0.2,0.2,0.2,0.2,0.2,0.1,0.1,0.1,0.1,0.1,0.1,0.8,0.4]
    			for p in pitches:
      				self.buzz(p, duration[x])  #feed the pitch and duration to the func$
     				time.sleep(duration[x] *0.5)
      				x+=1

  			elif(tune==4):
    			pitches=[1047, 988,659]
    			duration=[0.1,0.1,0.2]
    			for p in pitches:
      				self.buzz(p, duration[x])  #feed the pitch and duration to the func$
      				time.sleep(duration[x] *0.5)
      				x+=1

  			elif(tune==5):
    			pitches=[1047, 988,523]
    			duration=[0.1,0.1,0.2]
   				for p in pitches:
   					self.buzz(p, duration[x])  #feed the pitch and duration to the func$
      				time.sleep(duration[x] *0.5)
      				x+=1

  			GPIO.setup(self.buzzer_pin, GPIO.IN)

		if __name__ == "__main__":
  			a = input("Enter Tune number 1-5:")
  			buzzer = Buzzer()
 			buzzer.play(int(a))

This class will allow you to fully utilize the functions of the buzzer. The buzz method allows you to manipulate both the tone and the duration it is played for. The tone specifies the frequency of the desired sound, and the analog connection allows the method to modulate the frequency of the current and create a tone with that frequency.
Tone
----

	import RPi.GPIO as GPIO 
	import time 

	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(7, GPIO.OUT) 
	GPIO.setup(15, GPIO.OUT) 

	c = 261
	d = 294
	e = 329
	f = 349
	g = 392
	a = 440
	b = 493
	C = 423
	r = 1
	p = GPIO.PWM(15, 100)
	
	def Blink(numTimes, speed):
   	 	for i in range(0,numTimes): 
       	 print "Iteration " + str(i+1) 
        	GPIO.output(7, True) 
        	GPIO.output(15, True) 
        	time.sleep(speed) ## Wait
        	p.start(100)             # start the PWM on 100  percent duty cycle  
        	p.ChangeDutyCycle(90)   # change the duty cycle to 90%  
        	p.ChangeFrequency(c)  # change the frequency to 261 Hz (floats also work)  
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(d)  # change the frequency to 294 Hz (floats also work)  
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(e)   
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(f)  
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(g)    
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(a)    
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(b)    
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(C)    
        	time.sleep(speed) ## Wait
        	p.ChangeFrequency(r)  
        	time.sleep(speed) ## Wait
        	p.stop()                # stop the PWM output  

	    print "Done" ## When loop is complete, print "Done"
    	GPIO.cleanup()

	iterations = 4
	speed = 2

	Blink(int(iterations),float(speed))
	
LED
---

* [LED](https://www.dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/raspberry-pi-led-tutorial/)

Connect the LED To D4. An LED is the simplest possible module for a raspberry pi, as it is responsive only to the provided power. For an LED to emit light, it must be exposed to a voltage greater than some minimum value. Below this voltage, the diode is nonconductive, but above it, the diode conducts. As you increase the voltage, the conductivity of the diode increases exponentially and its brightness increases likewise. If the current through the LED becomes too high, the LED will burn out. The following code describes the LED class. The LED class has one method, blink. Since it is connected to a digital output, the voltage has only two states, on and off. This means that we cannot change the brightness of the LED.

	import time
	from grovepi import *
	
	print ("This example will blink a Grove LED connected to the GrovePi+ on the port labeled D3.\nIf you're having trouble seeing the LED blink, be sure to check the LED connection and the port number.\nYou may also try reversing the direction of the LED on the sensor.")
	print (" ")
	print ("Connect the LED to the port labele D3!" )
	
	
	class LED(object):
	
	    def __init__(self, pin):
	        self.pin = pin
	        pinMode(self.pin, "OUTPUT")
	
	    def blink(self, n):
	        for n in range(0, n):
	            try:
	                # Blink the LED
	                digitalWrite(self.pin, 1)  # Send HIGH to switch on LED
	                print ("LED ON!")
	                time.sleep(1)
	
	                digitalWrite(self.pin, 0)  # Send LOW to switch off LED
	                print ("LED OFF!")
	                time.sleep(1)
	
	            except KeyboardInterrupt:  # Turn LED off before stopping
	                digitalWrite(self.pin, 0)
	                break
	            except IOError:  # Print "Error" if communication error encountered
	                print ("Error")
	
	led = LED(3)
	led.blink(5)

Temperature
-----------
The temperature sensor can be attached with and without the LCD display. Without the display, you can print the temperature and humidity values into your terminal. To run the following code, plug the temperature sensor into the D7 port.

	from grovepi import *
	#from grove_rgb_lcd import *
	import time
	
	dht_sensor_port = 7  # Connect the DHt sensor to port 7
	
	time.sleep(2)
	
	while True:
	    time.sleep(.1)
	    try:
	        [temp, hum] = dht(dht_sensor_port, 0)  # Get the temperature and Humidity from the DHT sensor
	        print "temp =", temp, "C\thumadity =", hum, "%"
	        t = str(temp)
	        h = str(hum)
	        print("Temp:" + t + "C      " + "Humidity :" + h + "%")
	        #setRGB(0, 128, 64)
	        #setRGB(0, 255, 0)
	        #setText("Temp:" + t + "C      " + "Humidity :" + h + "%")
	    except (IOError, TypeError) as e:
	        print "Error"


The `dht_sensor_type` below may need to be changed depending on the DHT sensor you use:

* 0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
* 1 - DHT22 - white one, aka DHT Pro or AM2302
* 2 - DHT21 - black one, aka AM2301  

	        	
Advanced Code
-------------

This code has been taken from [Advanced Code](https://github.com/DexterInd/GrovePi/blob/master/Projects/Advanced_RGB_LCD_TempAndHumidity/grovepi_lcd_dht.py). It supports a Temperature sensor connected to the `dht_sensor_port` 7. The program has not yet been successfully implemented.


	import decimal
	from grovepi import *
	from grove_rgb_lcd import *
	
	dht_sensor_port = 7     # Connect the DHt sensor to port 7
	lastTemp = 0.1          # initialize a floating point temp variable
	lastHum = 0.1           # initialize a floating Point humidity variable
	tooLow = 62.0           # Lower limit in fahrenheit
	justRight = 68.0        # Perfect Temp in fahrenheit
	tooHigh = 74.0          # Temp Too high
	
	
	# Function Definitions
	def CtoF( tempc ):
	   "This converts celcius to fahrenheit"
	   tempf = round((tempc * 1.8) + 32, 2);
	   return tempf;
	
	def FtoC( tempf ):
	   "This converts fahrenheit to celcius"
	   tempc = round((tempf - 32) / 1.8, 2)
	   return tempc;
	
	def calcColorAdj(variance):     # Calc the adjustment value of the background color
	    "Because there is 6 degrees mapping to 255 values, 42.5 is the factor for 12 degree spread"
	    factor = 42.5;
	    adj = abs(int(factor * variance));
	    if adj > 255:
	        adj = 255;
	    return adj;
	
	def calcBG(ftemp):
	    "This calculates the color value for the background"
	    variance = ftemp - justRight;   # Calculate the variance
	    adj = calcColorAdj(variance);   # Scale it to 8 bit int
	    bgList = [0,0,0]               # initialize the color array
	    if(variance < 0):
	        bgR = 0;                    # too cold, no red
	        bgB = adj;                  # green and blue slide equally with adj
	        bgG = 255 - adj;
	        
	    elif(variance == 0):             # perfect, all on green
	        bgR = 0;
	        bgB = 0;
	        bgG = 255;
	        
	    elif(variance > 0):             #too hot - no blue
	        bgB = 0;
	        bgR = adj;                  # Red and Green slide equally with Adj
	        bgG = 255 - adj;
	        
	    bgList = [bgR,bgG,bgB]          #build list of color values to return
	    return bgList;
	
	while True:
	
	    try:
	        temp = 0.01
	        hum = 0.01
	        [ temp,hum ] = dht(dht_sensor_port,0)       #Get the temperature and Humidity from the DHT sensor
	                                                    #Change the second parameter to 0 when using DHT (instead of DHT Pro)
	                                                    #You will get very large number values if you don't!
	        if (CtoF(temp) != lastTemp) and (hum != lastHum) and not math.isnan(temp) and not math.isnan(hum):
	                print("lowC : ",FtoC(tooLow),"C\t\t","rightC  : ", FtoC(justRight),"C\t\t","highC : ",FtoC(tooHigh),"C") # comment these three lines
	                print("lowF : ",tooLow,"F\t\tjustRight : ",justRight,"F\t\ttoHigh : ",tooHigh,"F")                       # if no monitor display
	                print("tempC : ", temp, "C\t\ttempF : ",CtoF(temp),"F\t\tHumidity =", hum,"%\r\n")
	                
	                lastHum = hum          # save temp & humidity values so that there is no update to the RGB LCD
	                ftemp = CtoF(temp)     # unless the value changes
	                lastTemp = ftemp       # this reduces the flashing of the display
	                # print "ftemp = ",ftemp,"  temp = ",temp   # this was just for test and debug
	                
	                bgList = calcBG(ftemp)           # Calculate background colors
	                
	                t = str(ftemp)   # "stringify" the display values
	                h = str(hum)
	                # print "(",bgList[0],",",bgList[1],",",bgList[2],")"   # this was to test and debug color value list
	                setRGB(bgList[0],bgList[1],bgList[2])   # parse our list into the color settings
	                setText("Temp:" + t + "F      " + "Humidity :" + h + "%") # update the RGB LCD display
	                
	    except (IOError,TypeError) as e:
	        print("Error" + str(e))
	        
	        
LCD Screen
----------
The LCD screen can be used to display text. In order to use it, plug it into one of the I2C ports.  The following code will allow you to print messages on the screen.

	import time, sys
	
	if sys.platform == 'uwp':
	    import winrt_smbus as smbus
	
	    bus = smbus.SMBus(1)
	else:
	    import smbus
	    import RPi.GPIO as GPIO
	
	    rev = GPIO.RPI_REVISION
	    if rev == 2 or rev == 3:
	        bus = smbus.SMBus(1)
	    else:
	        bus = smbus.SMBus(0)
	
	# this device has two I2C addresses
	DISPLAY_RGB_ADDR = 0x62
	DISPLAY_TEXT_ADDR = 0x3e
	
	
	# set backlight to (R,G,B) (values from 0..255 for each)
	def setRGB(r, g, b):
	    bus.write_byte_data(DISPLAY_RGB_ADDR, 0, 0)
	    bus.write_byte_data(DISPLAY_RGB_ADDR, 1, 0)
	    bus.write_byte_data(DISPLAY_RGB_ADDR, 0x08, 0xaa)
	    bus.write_byte_data(DISPLAY_RGB_ADDR, 4, r)
	    bus.write_byte_data(DISPLAY_RGB_ADDR, 3, g)
	    bus.write_byte_data(DISPLAY_RGB_ADDR, 2, b)
	
	
	# send command to display (no need for external use)
	def textCommand(cmd):
	    bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x80, cmd)
	
	
	# set display text \n for second line(or auto wrap)
	def setText(text):
	    textCommand(0x01)  # clear display
	    time.sleep(.05)
	    textCommand(0x08 | 0x04)  # display on, no cursor
	    textCommand(0x28)  # 2 lines
	    time.sleep(.05)
	    count = 0
	    row = 0
	    for c in text:
	        if c == '\n' or count == 16:
	            count = 0
	            row += 1
	            if row == 2:
	                break
	            textCommand(0xc0)
	            if c == '\n':
	                continue
	        count += 1
	        bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(c))
	
	
	# Update the display without erasing the display
	def setText_norefresh(text):
	    textCommand(0x02)  # return home
	    time.sleep(.05)
	
	    textCommand(0x08 | 0x04)  # display on, no cursor
	    textCommand(0x28)  # 2 lines
	    time.sleep(.05)
	    count = 0
	    row = 0
	    for c in text:
	        if c == '\n' or count == 16:
	            count = 0
	            row += 1
	            if row == 2:
	                break
	            textCommand(0xc0)
	            if c == '\n':
	                continue
	        count += 1
	        bus.write_byte_data(DISPLAY_TEXT_ADDR, 0x40, ord(c))
	
	
	# example code
	if __name__ == "__main__":
	    on = True
	    while on:
	        print('To exit, type x.')
	        message = input('Type a short message: ')
	        if message.lower == 'x':
	            on = False
	        else:
	            setText(message)
	            setRGB(0, 128, 64)
	        for c in range(0, 255):
	            setRGB(c, 255 - c, 0)
	            time.sleep(0.01)
	    setRGB(0, 255, 0)
	    setText("Goodbye")

		        	
Moisture
--------

* [Code 1](https://github.com/DexterInd/GrovePi/blob/master/Projects/plant_monitor/plant_project.py)

* [code 2](https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_moisture_sensor.py)

Flow
----

* [Flow](https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_flow_read.py)
* [Sensor](http://www.seeedstudio.com/depot/G14-Water-Flow-Sensor-p-1345.html)

Water
-----

* [Water](https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_water_sensor.py)

Temperature from Web
--------------------

* [code](https://github.com/DexterInd/GrovePi/blob/master/Projects/OLED_Weather%20Display/weather.py)

Twitter feed

sudo pip install python-twitter

Sensors used in this code are:

light sensor on port A1
sound sensor on port A0
temperature and humidity sensor on port D2
LED for visual feedback on port D3 (with PWM)

* [twitter feed](https://github.com/DexterInd/GrovePi/blob/master/Projects/Sensor_Twitter_Feed/wifi_twit.py)


*[advanced rain notifier](https://github.com/DexterInd/GrovePi/blob/master/Projects/rain_notifier/rain_notifier.py)
