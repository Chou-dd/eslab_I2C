import RPi.GPIO as GPIO
from time import sleep
import smbus
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN)

GPIO.add_event_detect(27, GPIO.FALLING, callback=my_callback, bouncetime=300)

bus = smbus.SMBus(1)
def my_callback(channel):
    global bus
    inter = bus.read_byte_data(0x53,0x30)
    if((inter&0x10)==0x10):
        print("ACT detected\n")
    if((inter&0x08)==0x08):
        print("INACT detected\n")

bus.write_byte_data(0x53,0x31,0x2B) #initial data format and fall edge interrupt
bus.write_byte_data(0x53,0x24,0x06) #set ACT THREHOLD
bus.write_byte_data(0x53,0x25,0x06) #set INACT THREHOLD
bus.write_byte_data(0x53,0x26,0x01) 
bus.write_byte_data(0x53,0x27,0x66) #set ACT_x ACT_y INACT_x INACT_y
bus.write_byte_data(0x53,0x2F,0x18) #set INT2 pin receive ACT interrupt
bus.write_byte_data(0x53,0x2E,0x18) #enable ACT INACT interrupt
bus.write_byte_data(0x53,0x2D,0x08) #start measure



try:
    while(True):
        sleep(0.1)
except KeyboardInterrupt:
GPIO.cleanup() # clean up GPIO on CTRL+C exit
GPIO.cleanup() # clean up GPIO on normal exit