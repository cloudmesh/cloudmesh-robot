### NodeMCU ESP12 Dev Kit V1.0 Pin Definition:

![nodemcs](./images/nodemcu.png)
 
The  GPIO numbers of teh NodeMCU, do not correspond with the actual numbers used in micropythons pin library. The numbers are as follows:

| Pin/GPIO | NodeMCU |
|----------|---------|
|      15  |    D8   |



# LED

## Links

* [Feather HUZZAH ESP8266](https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led)

## Program

	import machine
	led = machine.Pin(15,machine.Pin.OUT)
	led.high()
	led.low()
	
	
	import machine
	led = machine.Pin(15,machine.Pin.OUT)
	while True:
		led.high()
		time.sleep(0.5)
		led.low()
		time.sleep(0.5)
		
		
![breadboard](./fritzing/led-esp8266_bb.pdf)

![schema](./fritzing/led-esp8266_schem.png)


