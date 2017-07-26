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