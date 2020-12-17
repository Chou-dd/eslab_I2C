import smbus
from time import sleep

bus = smbus.SMBus(1)
address = 0x53

bus.write_byte_data(address, 0x2C, 0X0C)

while True:
    bytes = bus.read_i2c_block_data(0x53,0x32,6)
    x = bytes[0] | (bytes[1]<<8)
    if(x&(1<<16-1)):
        x = x - (1<<16)
    y = bytes[2] | (bytes[3]<<8)
    if(y&(1<<16-1)):
        y = y - (1<<16)
    z = bytes[4] | (bytes[5]<<8)
    if(z&(1<<16-1)):
        z = z - (1<<16)
    x = x*0.004
    y = y*0.004
    z = z*0.004
    x = round(x,4)
    y = round(y,4)
    z = round(z,4)
    #print "x = %.3fG, y = %.3fG, z = %.3fG"%(x,y,z)
    print("x =", x,", y =", y," z =", z)
