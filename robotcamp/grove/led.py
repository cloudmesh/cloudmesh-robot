import time
import grovepi
import sys

class LED(object):

    def __init__(self, pin=3):
        self.pin = pin
        pinMode(self.pin, "OUTPUT")

    def on(self):
        digitalWrite(self.pin, 1)  # Send HIGH to switch on LED

    def off(self):
        digitalWrite(self.pin, 0)  # Send LOW to switch off LED

    def blink(self, n, t=0.2):
        for i in range(0, n):
            try:
                # LED on
                self.on()
                time.sleep(t) # duration on 
                # LED off                
                self.off()
                time.sleep(t) #duration off

            except KeyboardInterrupt:  # Turn LED off before stopping
                digitalWrite(self.pin, 0)
                sys.exit()
                break
            except IOError:  # Print "Error" if communication error encountered
                print ("Error")

if __name__ == "__main__":
    led = LED(pin=3)
    led.blink(5)
    
