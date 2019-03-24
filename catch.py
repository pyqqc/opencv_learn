import serial
import serial.tools.list_ports
import string
import binascii
import time
ports = list(serial.tools.list_ports.comports())
print (ports)
#便利 寻找串口
for p in ports:
    print (p[1])
    if "serial" in p[1] or "CH340" in p[1]:
        ser=serial.Serial(port=p[0])
        print(ser)
    else :
        
        print ("No Arduino Device was found connected to the computer")

def initspeed():#初始化速度&位置
    m0=bytes.fromhex('ff 01 00 08 00')# 舵机0速度为 72
    m1=bytes.fromhex('ff 01 01 08 00')# 舵机1速度为 72
    m2=bytes.fromhex('ff 01 02 08 00')# 舵机2速度为 72
    mo0=bytes.fromhex('ff 02 00 d0 07')#设置初始舵机0位置
    mo1=bytes.fromhex('ff 02 01 82 07')#设置初始舵机1的位置
    mo2 = bytes.fromhex('ff 02 02 dc 05')#设置初始舵机1的位置
    ser.write(m0)
    ser.write(m1)
    ser.write(m2)
    ser.write(mo0)
    ser.write(mo1)
    ser.write(mo2)

def tl():
    a=bytes.fromhex('ff 02 00 77 06')
    b=bytes.fromhex('ff 02 01 08 07')
    c=bytes.fromhex('ff 02 02 4c 04')
    ser.write(a)
    ser.write(b)
    ser.write(c)
    
#定义吸收东西
def absorbsthings():
    
    b=bytes.fromhex('ff 02 04 c4 09')  #吸
    c=bytes.fromhex('ff 02 05 f4 01')  #  开启阀门
    ser.write(b)
    ser.write(c)
#定义放东西
def relax():
    a=bytes.fromhex('ff 02 04 f4 01')  #放
    c=bytes.fromhex('ff 02 05 56 06')  #  关闭阀门
    ser.write(a)
    ser.write(c)
initspeed()
absorbsthings()
time.sleep(3)
tl()
relax()

