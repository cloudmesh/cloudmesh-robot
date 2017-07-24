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

* [Buzzer](http://www.linuxcircle.com/2015/04/12/how-to-play-piezo-buzzer-tunes-on-raspberry-pi-gpio-with-pwm/)

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

Connect the LED To D4

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