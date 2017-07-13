# Feather esp8266

[doc](https://learn.adafruit.com/adafruit-feather-huzzah-esp8266/using-nodemcu-lua)

## OSX Terminal

[CoolTerm](https://learn.sparkfun.com/tutorials/terminal-basics/coolterm-windows-mac-linux)

download [http://freeware.the-meiers.org/CoolTermMac.zip](http://freeware.the-meiers.org/CoolTermMac.zip)


### Check

    cms robot login
    
### Probe

    cms robot probe
    
### Erase

Erasing the feather is simple as it has a bild in mechanism to detect
if it is going to be erased. Hence no reset button needs to be pressed

    cms robot flash erase
    
### Python
    
    cms robot flash python
    
    
Flashing is conducted with 460800 baud, it will take about 15 seconds.  


After flashing you should try to login

    cms robot login

Set the boudrate to 115200
 
    CTRL-A CTRL-B
    
    *** baud: 
    
type in 

    115200 <ENTER>
    
Make sure that echo is switched to OFF 
    
    CTRL-A CTRL-C
    
toogles it.
    
   
Now you should see 
    
    >>>
    
    
Try typing in

    print("Hello")
    