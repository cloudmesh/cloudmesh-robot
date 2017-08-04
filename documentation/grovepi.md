Intro
-----

[Electronics] (http://www.instructables.com/id/Basic-Electronics): An introduction to the basic principals of electronics.  
[Volatage] (https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law): An introduction to the physics of electricity.   
[Unix] (https://info-ee.eps.surrey.ac.uk/Teaching/Unix/index.html): An introduction to the Unix os.  
[grove examples](https://github.com/DexterInd/GrovePi/tree/master/Software/Python): A list of Dexter Industries example code for GrovePi modules.


LED
---

* [LED](https://www.dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/raspberry-pi-led-tutorial/)

Connect the LED To a digital port. An LED is the simplest possible module for a raspberry pi, as it is responsive only to the provided power. For an LED to emit light, it must be exposed to a voltage greater than a certain threshold value. Above this voltage, the conductivity of the diode increases exponentially and its brightness increases likewise. If the current through the LED becomes too high, the LED will burn out. The following code describes an LED class. Since it is connected to a digital output, the voltage has only two states, on and off. The default port for the LED class is D3.

	import time
	import grovepi
	import sys
	
	
	
	class LED(object):
	
	    def __init__(self, pin=3):
	        """
	        Connect the LED to a digital port. 3 is default.
	        :param pin: Integer
	        """
	        self.pin = pin
	        grovepi.pinMode(self.pin, "OUTPUT")
	
	    def on(self):
	        """
	        turns LED on.
	        :return: None
	        """
	        grovepi.digitalWrite(self.pin, 1)  # Send HIGH to switch on LED
	
	    def off(self):
	        """
	        turns LED off.
	        :return: None
	        """
	        grovepi.digitalWrite(self.pin, 0)  # Send LOW to switch off LED
	    
	    def put(self, value):
	        """
	        Puts a value on the LED. value is either 0 or 1. 0 is off, 1 is on.
	        :param value: Integer: 0 or 1
	        :return: None
	        """
	        grovepi.digitalWrite(self.pin, value)
	
	    def blink(self, n, t=0.2):
	        """
	        blinks LED n times with t time delay. Default t is .2 seconds.
	        :param n: Integer
	        :param t: Number
	        :return: None
	        """
	        for i in range(0, n):
	            try:
	                # LED on
	                self.on()
	                time.sleep(t) # duration on
	                # LED off
	                self.off()
	                time.sleep(t) #duration off
	
	            except KeyboardInterrupt:  # Turn LED off before stopping
	                grovepi.digitalWrite(self.pin, 0)
	                sys.exit()
	                break
	            except IOError:  # Print "Error" if communication error encountered
	                print ("Error")

Buzzer
------
 
Connect the buzzer to a digital port. You will notice that the Buzzer class and the LED class are interchangeable. This is because they work on the same digital principal. Their two values are on and off. The default port for the Buzzer class is D3.

	import time
	import grovepi
	import sys
	
	
	class Buzzer(object):
	
	    def __init__(self, pin=3):
	        """
	        Connect buzzer to a digital port. Default is 3.
	        :param pin: Integer
	        """
	        self.pin = pin
	        grovepi.pinMode(self.pin, "OUTPUT")
	
	    def on(self):
	        """
	        Turns buzzer on.
	        :return: None
	        """
	        grovepi.digitalWrite(self.pin, 1)  # Send high to switch on buzzer
	
	    def off(self):
	        """
	        Turns the buzzer off.
	        :return: None
	        """
	        grovepi.digitalWrite(self.pin, 0)  # Send low to switch off buzzer
	
	    def put(self, value):
	        """
	        Puts a value on the buzzer. value is either 0 or 1. 0 is off, 1 is on.
	        :param value: Integer: 0 or 1
	        :return: None
	        """
	        grovepi.digitalWrite(self.pin, value)
	
	    def beep(self, n, t=0.2):
	        """
	        Cycles the buzzer on and off n times with a t second delay. .2 seconds is the default delay.
	        :param n: Integer
	        :param t: Number
	        :return: None
	        """
	        for i in range(0, n):
	            try:
	                # on
	                self.on()
	                time.sleep(t) # duration on
	                # off
	                self.off()
	                time.sleep(t) #duration off
	
	            except KeyboardInterrupt:  # Turn BUZZER off before stopping
	                grovepi.digitalWrite(self.pin, 0)
	                sys.exit()
	                break
	            except IOError:  # Print "Error" if communication error encountered
	                print ("Error") 


Barometer
---------
Connect the barometer to an I2C port. In addition to pressure, the GrovePi barometer measures temperature. The get method returns the temperature in Fahrenheit and Celcius and the pressure.

	import smbus
	import time
	
	class Barometer(object):
	
	    def __init__(self):
	        """
	        Connect barometer to a I2C port
	        """
	        # Get I2C bus
	        self.bus = smbus.SMBus(1)
	
	    def get(self):
	        """
	        gets the values of temperature in Celcius and Fahrenheit, and Pressure
	        :return: temp_in_C, temp_in_F, preasure
	        """
	
	        # BMP280 address, 0x76(118)
	        # Read data back from 0x88(136), 24 bytes
	        b1 = self.bus.read_i2c_block_data(0x76, 0x88, 24)
	
	        # Convert the data
	        # Temp coefficents
	        dig_T1 = b1[1] * 256 + b1[0]
	        dig_T2 = b1[3] * 256 + b1[2]
	        if dig_T2 > 32767 :
	            dig_T2 -= 65536
	        dig_T3 = b1[5] * 256 + b1[4]
	        if dig_T3 > 32767 :
	            dig_T3 -= 65536
	
	        # Pressure coefficents
	        dig_P1 = b1[7] * 256 + b1[6]
	        dig_P2 = b1[9] * 256 + b1[8]
	        if dig_P2 > 32767 :
	            dig_P2 -= 65536
	        dig_P3 = b1[11] * 256 + b1[10]
	        if dig_P3 > 32767 :
	            dig_P3 -= 65536
	        dig_P4 = b1[13] * 256 + b1[12]
	        if dig_P4 > 32767 :
	            dig_P4 -= 65536
	        dig_P5 = b1[15] * 256 + b1[14]
	        if dig_P5 > 32767 :
	            dig_P5 -= 65536
	        dig_P6 = b1[17] * 256 + b1[16]
	        if dig_P6 > 32767 :
	            dig_P6 -= 65536
	        dig_P7 = b1[19] * 256 + b1[18]
	        if dig_P7 > 32767 :
	            dig_P7 -= 65536
	        dig_P8 = b1[21] * 256 + b1[20]
	        if dig_P8 > 32767 :
	            dig_P8 -= 65536
	        dig_P9 = b1[23] * 256 + b1[22]
	        if dig_P9 > 32767 :
	            dig_P9 -= 65536
	
	        # BMP280 address, 0x76(118)
	        # Select Control measurement register, 0xF4(244)
	        #		0x27(39)	Pressure and Temperature Oversampling rate = 1
	        #					Normal mode
	        self.bus.write_byte_data(0x76, 0xF4, 0x27)
	        # BMP280 address, 0x76(118)
	        # Select Configuration register, 0xF5(245)
	        #		0xA0(00)	Stand_by time = 1000 ms
	        self.bus.write_byte_data(0x76, 0xF5, 0xA0)
	
	        time.sleep(0.5)
	
	        # BMP280 address, 0x76(118)
	        # Read data back from 0xF7(247), 8 bytes
	        # Pressure MSB, Pressure LSB, Pressure xLSB, Temperature MSB, Temperature LSB
	        # Temperature xLSB, Humidity MSB, Humidity LSB
	        data = self.bus.read_i2c_block_data(0x76, 0xF7, 8)
	
	        # Convert pressure and temperature data to 19-bits
	        adc_p = ((data[0] * 65536) + (data[1] * 256) + (data[2] & 0xF0)) / 16
	        adc_t = ((data[3] * 65536) + (data[4] * 256) + (data[5] & 0xF0)) / 16
	
	        # Temperature offset calculations
	        var1 = ((adc_t) / 16384.0 - (dig_T1) / 1024.0) * (dig_T2)
	        var2 = (((adc_t) / 131072.0 - (dig_T1) / 8192.0) * ((adc_t ) /131072.0 - (dig_T1 ) /8192.0)) * (dig_T3)
	        t_fine = (var1 + var2)
	        self.cTemp = (var1 + var2) / 5120.0
	        self.fTemp = self.cTemp * 1.8 + 32
	
	        # Pressure offset calculations
	        var1 = (t_fine / 2.0) - 64000.0
	        var2 = var1 * var1 * (dig_P6) / 32768.0
	        var2 = var2 + var1 * (dig_P5) * 2.0
	        var2 = (var2 / 4.0) + ((dig_P4) * 65536.0)
	        var1 = ((dig_P3) * var1 * var1 / 524288.0 + (dig_P2) * var1) / 524288.0
	        var1 = (1.0 + var1 / 32768.0) * (dig_P1)
	        p = 1048576.0 - adc_p
	        p = (p - (var2 / 4096.0)) * 6250.0 / var1
	        var1 = (dig_P9) * p * p / 2147483648.0
	        var2 = p * (dig_P8) / 32768.0
	        self.pressure = (p + (var1 + var2 + (dig_P7)) / 16.0) / 100
	
	        return self.cTemp, self.fTemp, self.pressure
	
	    def __str__(self):
	        self.get()
	        message = \
	            "Temperature in Celsius : %.2f C" % self.cTemp + \
	            "Temperature in Fahrenheit : %.2f F" % self.fTemp + \
	            "Pressure : %.2f hPa " % self.pressure
	        return message
	        
	        
Distance Sensor
---------------
Connect the distance sensor to a digital port. The grovepi module has a built-in function to read the distance from the distance sensor, but it is improperly calibrated, so this DistanceSensor class has a calibration based on experimental data.

	#!/usr/bin/env python
	
	#21cm = 26
	#31cm = 36
	#41cm = 49
	#51cm = 62
	#61cm = 75
	#71cm = 86
	#81cm = 99
	
	#If value is smaller than 7 cm, take value. 
	
	import grovepi
	
	class DistanceSensor(object):
	
	    def __init__(self, port=4):
	        """
	        connect to digital port. D4 is defualt.
	        :param port: Integer
	        """
	        # Connect the Grove Ultrasonic Ranger to digital port D4
	        # SIG,NC,VCC,GND
	        self.ultrasonic_ranger = port
	
	    def get(self):
	        """
	        gets the value of the sensor.
	        :return: Integer
	        """
	        return grovepi.ultrasonicRead(self.ultrasonic_ranger)
	
	    def calibrate(self, tuple):
	        """
	         (cm, value)
	
	        :param tuple: [(21, 26), ....]
	        :return:
	        """
	        pass


Temperature
-----------

Heartbeat Sensor
----------------


	class HeartbeatSensor(object):
	
	    def __init__(self):
	        """
	        Connect to an I2C port.
	        """
	        rev = GPIO.RPI_REVISION
	        if rev == 2 or rev == 3:
	            self.bus = smbus.SMBus(1)
	        else:
	            self.bus = smbus.SMBus(0)
	        self.address = 0x50
	
	    def get(self):
	        """
	        Returns the heart rate of the wearer.
	        :return: Integer
	        """
	        return self.bus.read_byte(0x50)

	        
	        
LCD Screen
----------
The LCD screen can be used to display text. In order to use it, plug it into one of the I2C ports.  The following code will allow you to print messages on the screen. This has not been tested.


	    
	    
Barometer  
---------

A barometer detects and measures pressure. Our barometers measure temperature, pressure, and altitude, and must be connected to an I2C port. 


		        	
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
