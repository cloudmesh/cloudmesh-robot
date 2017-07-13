The default pins are defined in variants/nodemcu/pins_arduino.h as 
GPIO SDA=4 and SCL=5
 D1=5 
 D2=4.

Anyway, you can also choose the pins yourself using the I2C constructor Wire.begin(int sda, int scl);