NodeMCU ESP12 Dev Kit V1.0 Pin Definition:
==========================================

|nodemcs|   The GPIO numbers of teh NodeMCU, do not correspond with the
actual numbers used in micropythons pin library. The numbers are as
follows:

+------------+-----------+
| Pin/GPIO   | NodeMCU   |
+============+===========+
| 15         | D8        |
+------------+-----------+

LED
===

Links
-----

-  `Feather HUZZAH
   ESP8266 <https://learn.adafruit.com/micropython-basics-blink-a-led/blink-led>`__

Program
-------

::

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
        
        

.. figure:: ./fritzing/led-esp8266_bb.pdf
   :alt: breadboard

   breadboard

.. figure:: ./fritzing/led-esp8266_schem.png
   :alt: schema

   schema

.. |nodemcs| image:: ./images/nodemcu.png
