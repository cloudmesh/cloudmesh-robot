from machine import Pin, PWM
import time

for i in [4, 5]:
    print(i)
    pwm = PWM(Pin(i), freq=0, duty=100)

time.sleep(1)

for i in [4, 5]:
    print(i)
    pwm = PWM(Pin(i), freq=0, duty=0)


