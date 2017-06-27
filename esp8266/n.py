"""
from wireless import WLAN

def ap():
    wifi = WLAN(mode=WLAN.AP)
    my_ssid = "fish01"
    my_auth = (WLAN.WPA2_AES_PSK, "inx")
    wifi.start_ap(ssid=my_ssid, auth=my_auth)
    return wifi
"""

print ("start")
import network

sta_if = network.WLAN(network.STA_IF)
ap_if = network.WLAN(network.AP_IF)

sta_if.active()
ap_if.active()
ap_if.ifconfig()

sta_if.connect('zz250', 'pferdpferd67')
print(sta_if)

print(sta_if.ifconfig())
print(ap_if.ifconfig())