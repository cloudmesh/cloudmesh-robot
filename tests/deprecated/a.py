#
# USB CONNECTION
#
import network

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)
sta_if.active()
ap_if.active()
ap_if.ifconfig()
#
# WLAN
#
sta_if.active(True)
sta_if.ifconfig(('aaa','255.255.255.0','bbb','ccc'))
sta_if.connect()
print (sta_if)
print (dir(sta_if))
print ("Status:", sta_if.status())
print ("Connected:", sta_if.isconnected())
print ("Active:", sta_if.active())
print ("Scan:", sta_if.scan())
sta_if.connect('attwifi')
print ("Status:", sta_if.status())
print ("Conected to att:", sta_if.isconnected())


