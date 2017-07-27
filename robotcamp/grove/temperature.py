from grovepi import *
from grove_rgb_lcd import *
import time
import smbus
import RPi.GPIO as GPIO
from grove_i2c_barometic_sensor_BMP180 import BMP085


class WeatherStation(object):
    def __init__(self, port=7):
        self.dht_sensor_port = port
        setRGB(0,255,0)

    def get(self):    

        try:
            temp, hum = dht(self.dht_sensor_port, 0)
            # Get the temperature and Humidity from the DHT sensor
            
            t = str(temp)
            h = str(hum)
            print("Temp:" + t + "C      " + "Humidity :" + h + "%")
            setText("Temp:" + t + "C      " + "Humidity :" + h + "%")
            return t, h
        except (IOError, TypeError) as e:
            print "Error"

station= WeatherStation()

while True:
    time.sleep(2)
    print(station.get())

