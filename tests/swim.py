import cm
import time

led = cm.LED(2)

fin = cm.Servo(15)

fin.low()
led.off()

fin.high()
led.on()


time.sleep(0.5)

led.off

fin.swim(2,1.0)

