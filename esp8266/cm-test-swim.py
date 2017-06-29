import cm
import utime

def banner (msg):
    print (70 * '=')
    print (msg)
    print (70 * '=')

banner("version")
print (cm.version)
banner("credentials")
cm.cat("credentials.txt")
banner("ls")
cm.ls()
#led = cm.LED(2)
#led.on()
#utime.sleep(1.0)
#led.off()
#led.blink(5, dt=0.2)

fin = cm.Servo("D7")
fin.low()
utime.sleep(0.5)
fin.high()
utime.sleep(0.5)
fin.mean()
utime.sleep(0.5)
fin.off()

