#!/usr/bin/env python
# test
# get_xy.py - 2D coordinates receiver from Marvelmind mobile beacon USB/serial port
# Written by Boris Zinin (b.zinin@gmail.com)
#
# Serial port device name (physical or USB/virtual) should be provided as an argument: 
#   /dev/ttyACM0 - typical for Linux / Raspberry Pi
#   /dev/tty.usbmodem1451 - typical for Mac OS X
#
# To prevent errors when installing crcmod module used in this script, use the following sequence of commands:
#   sudo apt-get install python-pip
#   sudo apt-get update
#   sudo apt-get install python-dev
#   sudo pip install crcmod

import sys
from time import sleep
import crcmod
import serial
import struct

def do_Navigate( X, Y, Timestamp ):
  print "X: {:d}\t   Y: {:d}\t\t T: {:.2f}".format( X,  Y, Timestamp/64.0 )
  # add application-specific X,Y coordinates processing here... 

  return

tty = sys.argv[1]
while True:
 try:
  ser = serial.Serial( tty, 9600, timeout=3 )
  pktSize = 23

  # start by reading & flushing 45 bytes: 2x pkt_size - 1
  ser.flushInput()
  len_buf = pktSize*2 - 1
  buf = ser.read(len_buf)
  buf = ''
  while buf is not None:
    buf += ser.read(len_buf)

    pktHdrOffset = buf.find('\xff\x47\x01\x00\x10')
    if pktHdrOffset == -1:
        print '\n*** ERROR: Marvelmind USNAV beacon packet header not found (check modem board or radio link)'
        continue
    elif pktHdrOffset > 0:
        print '\n>> Found USNAV beacon packet header at offset %d' % pktHdrOffset

    # parse the packet
    usnTimestamp, usnX, usnY, usnCRC16 = struct.unpack_from ( '<LhhxxxxxxxxH', buf, pktHdrOffset+5 )

    # check packet CRC
    crc16 = crcmod.predefined.Crc('modbus')
    crc16.update( buf[ pktHdrOffset : pktHdrOffset + pktSize - 2 ] )
    CRC_calc = int( crc16.hexdigest(), 16 )

    if CRC_calc == usnCRC16:
      do_Navigate( usnX, usnY, usnTimestamp )
    else:
      print '\n*** CRC ERROR'
     
    # align next packet start to the 5-byte header
    len_tail = len( buf ) - (pktHdrOffset + pktSize)
    len_buf = pktSize - len_tail
    if len_buf == 0:
        len_buf = pktSize
        buf = ''
    elif len_buf < 0:
        # resync if any error
        print '\n>>>> Buffer out of sync !\n'
        ser.flushInput()
        len_buf = pktSize*2 - 1
        buf = ''
    else:
        # flush the proccessed packet from the buffer
        buf = buf[ pktHdrOffset + pktSize : ]

 except OSError:
   print '\n*** ERROR: OS error (possibly serial port is not available)'
   sleep(1)
   
 except serial.SerialException:
   print '\n*** ERROR: serial port error (possibly beacon is reset, powered down or in sleep mode). Restarting reading process...'
   ser = None
   sleep(1)

 except KeyboardInterrupt:
  ser.close()
  sys.exit()
