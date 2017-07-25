Intro

Electronics: http://www.instructables.com/id/Basic-Electronics/
Volatage: https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law
Unix: http://www.ee.surrey.ac.uk/Teaching/Unix/index.html

* [grove examples](https://github.com/DexterInd/GrovePi/tree/master/Software/Python)

Buzzer
======
 
The Grove - [Buzzer](http://wiki.seeed.cc/Grove-Buzzer/) module has a piezo buzzer as the main component. The piezo can be connected to digital outputs, and will emit a tone when the output is HIGH. Alternatively, it can be connected to an analog pulse-width modulation output to generate various tones and effects.

Simple
------

	# GrovePi + Grove Buzzer
	import time
	import grovepi

	# Connect the Grove Buzzer to digital port D8
	# SIG,NC,VCC,GND
	buzzer = 8

	grovepi.pinMode(buzzer,"OUTPUT")

	while True:
   		try:
   		   # Buzz for 1 second
   		   grovepi.digitalWrite(buzzer,1)
   		   print 'start'
   		   time.sleep(1)

        	# Stop buzzing for 1 second and repeat
        	grovepi.digitalWrite(buzzer,0)
        	print 'stop'
        	time.sleep(1)

    	except KeyboardInterrupt:
       	 grovepi.digitalWrite(buzzer,0)
        	 break
    	except IOError:
       	 print "Error"

Buzzer
------

[Buzzer](http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/)  
To set up the buzzer, connect the red voltage wire to the GPIO Pin 5 and the black ground wire to the GPIO ground. The following code defines the buzzer class, which includes a buzz method and a play method. The buzz method plays the given pitch for the given duration, and the play method plays one of five precoded tunes, depending on the method's argument.

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

This class will allow you to fully utilize the functions of the buzzer. 
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

Connect the LED To D4. An LED is the simplest possible module for a raspberry pi, as it is responsive only to the provided power. To make the led brighter, provide it more power. To make it dimmer, decrease its power. The following code describes the LED class.

	import time
	from grovepi import *

	class LED(object):
	
		def __init__(self, port)
			self.port = port
			pinMode(led,"OUTPUT")
			print ("LED on D", port)
		
		def blink(n, dt=0.2):
		   count = 0
		   while count < n:
		   		try:
		   			n = n + 1
		   			digitalWrite(led,1)
		   			time.sleep(dt)
		   			digitalWrite(led,0)
		   			time.sleep(dt)

		   	 except KeyboardInterrupt:	
		        digitalWrite(led,0)
		        break
    		except IOError:				
	        	print ("Error")

	led = LED(4)        	
	time.sleep(1)
	led.blink(5) # -1 forever

Temperature
-----------

Attach a temperature sensor and read the temperature. 
Use the LCD screen to print the value

The dht_sensor_type below may need to be changed depending on the DHT sensor you use:

* 0 - DHT11 - blue one - comes with the GrovePi+ Starter Kit
* 1 - DHT22 - white one, aka DHT Pro or AM2302
* 2 - DHT21 - black one, aka AM2301


    from grovepi import *
    from grove_rgb_lcd import *
    import time
    
    dht_sensor_port = 7		# Connect the DHt sensor to port 7
    dht_sensor_type = 0     # Change depending on your sensor type 
    dt = 1.0
    while True:
        try:
            [temp, hum] = dht(dht_sensor_port,dht_sensor_type)		#Get the temperature and Humidity from the DHT sensor
            message = "Temp:" + str(temp) + "C      " + "Humidity :" + str(hum) + "%"
            
            # print on terminal
            print(message)
             
            # print on LCD 
            setRGB(0,128,64)
            setRGB(0,255,0)
            setText(message)
            time.sleep(dt)
            
        except KeyboardInterrupt:	
		        digitalWrite(led,0)
		        break
    		except IOError, TypeError:				
	        	print ("Error")
	        	
* [Advanced Code](https://github.com/DexterInd/GrovePi/blob/master/Projects/Advanced_RGB_LCD_TempAndHumidity/grovepi_lcd_dht.py)
	        	
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
