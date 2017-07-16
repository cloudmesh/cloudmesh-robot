# Real time Clock DS3231 RTC

Get the library urtc.py:

	wget https://raw.githubusercontent.com/adafruit/Adafruit-uRTC/master/urtc.py
	
Place it on the esp8266

	cms robot put urtc.py

Connect the board

SDA to pin 5 = D1
SCL to pin 4 = D2

Login to the board

	cms robot login
	
Execute the following code

	import machine
	i2c = machine.I2C(sda=machine.Pin(5), scl=machine.Pin(4))
	i2c.scan()

> 	[87, 104]

	from urtc import DS3231
	t = DS3231(i2c)
 
	t.datetime()

>		DateTimeTuple(year=2000, month=1, day=1, 
>						 weekday=1, hour=0, minute=15,
> 						 second=53, millisecond=None)


## Resources

	https://github.com/adafruit/Adafruit-uRTC/blob/master/urtc.py
	git clone https://github.com/adafruit/Adafruit-uRTC.git
	