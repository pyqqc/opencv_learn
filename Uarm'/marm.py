import cv2
import numpy as np
import math  as mt
import serial
import serial.tools.list_ports
import string
import binascii
import time
mMl01=((0,0),0,0,0)
mMl02=((0,0),0,0,0)
mMl03=((0,0),0,0,0)
mM01=((0,0),0,0,0)
mM02=((0,0),0,0,0)
mM03=((0,0),0,0,0)
marm=(mM01,mM02,mM03,mMl01,mMl02,mMl03)

img=cv2.imread("marm.jpg")
#图像缩一半便于屏幕显示处理
shape=img.shape
print(shape)
H=int(shape[0]/2)
W=int(shape[1]/2)
BW=int(W*1.5)+1
print(W,H)
img=cv2.resize(img,(W,H))
img= cv2.copyMakeBorder(img,0,0,400,0,cv2.BORDER_CONSTANT,value=(100,100,0))
imgcon=img.copy()
print(img.shape)
    
#电机模型
class mmotor():
#电机中心点，角度，开始，最大
    def __init__(self,center,angle,startangle,maxangle):
        self.center=center
        self.angle=angle
        self.startangle=startangle
        self.maxangle=maxangle
        self.relaangle=0
        self.pwm=500
        self.facetome=False
        
    def setcenter(self,center):
        self.center=center
        
    def draw(self,angle):
        self.angle=angle
        color=(0,255,0)
        r=30
        cv2.circle(img,self.center,r,color,-1)
        rect=(self.center,(2*r,4),angle)
        box = cv2.boxPoints(rect).astype(np.int0)
        cv2.drawContours(img,[box],0,(255,0,0),3)
    def drawrelative(self,relaangle):
        if relaangle >self.maxangle:
            relaangle=self.maxangle
        self.relaangle=relaangle
        self.angle=self.startangle+self.relaangle
        self.pwm=500+self.relaangle*180/self.maxangle*(2500-500)/180
        self.draw(self.angle)
        

# 臂模型
class mlever():
    def __init__(self,center,width,high,angle):
        self.center=center
        self.width=width
        self.angle=angle
        self.height=high
        self.jointpoint=(0,0)
        self.rightend=(width,0)
        self.rightendr=10
    
    def draw(self):
        global img,imgcon
        height=100
        # 没有连接点，以中心为轴旋转
        if self.jointpoint != (0,0):
            # 有连接点，则重新确定中心，绕连接点转
            w=int(self.width/2*mt.cos(self.angle/180*mt.pi))
            h=int(self.width/2*mt.sin(self.angle/180*mt.pi))
            self.center=(self.jointpoint[0]-w,self.jointpoint[1]-h)
            rect=(self.center, (self.width,self.height), self.angle)
            box = cv2.boxPoints(rect).astype(np.int0)
            self.rightend=(self.jointpoint[0]-w*2,self.jointpoint[1]-h*2)
        else:
            rect=(self.center, (self.width,self.height), self.angle)
            box = cv2.boxPoints(rect).astype(np.int0)
            self.rightend=(int((box[2][0]+box[3][0])/2),int((box[2][1]+box[3][1])/2))
        cv2.drawContours(img,[box],0,(255,0,0),3)    #框的颜色      
    def setl(self,center,angle):
        self.center=center
        self.angle=angle
    def setangle(self,angle):
        self.angle=angle    
    def setjointpoint(self,jointpoint):
        self.jointpoint=jointpoint
    def drawrightend(self):
        cv2.circle(img,self.rightend,self.rightendr,(0,0,255),3)

class Marm():
    def __init__(self,m01,m02,m03,ml01,ml02,ml03):
        self.m01=m01
        self.m02=m02
        self.m03=m03        
        self.ml01=ml01
        self.ml02=ml02
        self.ml03=ml03 
        self.angle1=0
        self.angle2=0
        self.angle3=0
        self.ser=None
        #将梁2固定在电机2的中心
        self.ml02.setjointpoint(self.m02.center)
        #打开串口
        ports = list(serial.tools.list_ports.comports())
        print (ports)
        #便利 寻找串口
        for p in ports:
            print (p[1])
            if "serial" in p[1] or "CH340" in p[1]:
                self.ser=serial.Serial(port=p[0])
                if self.ser is not None:
                    print(self.ser)
                    print("serial conected")
                else:
                    print("serial not connected")
                    return
            else:
                print ("No CH340 Device was found connected to the computer")
                return
        self.robotinit()
    def robotinit(self):
        if self.ser is None:
            return
        m0=bytes.fromhex('ff 01 00 08 00')# 舵机0速度为 72
        m1=bytes.fromhex('ff 01 01 08 00')# 舵机1速度为 72
        m2=bytes.fromhex('ff 01 02 08 00')# 舵机2速度为 72
        mo0=bytes.fromhex('ff 02 00 dc 05')#设置初始舵机0位置
        mo1=bytes.fromhex('ff 02 01 82 07')#设置初始舵机1的位置
        mo2 = bytes.fromhex('ff 02 02 dc 05')#设置初始舵机2的位置
        mo3 = bytes.fromhex('ff 02 03 dc 05')#设置初始舵机3的位置
        self.ser.write(m0)
        self.ser.write(m1)
        self.ser.write(m2)
        self.ser.write(mo0)
        self.ser.write(mo1)
        self.ser.write(mo2)
        self.ser.write(mo3)
    def xytoq(self,x,y):
        L1=self.ml01.width
        L2=self.ml02.width
        L3=mt.sqrt(y*y+x*x)+0.01
        #L3最长不超过两臂之和
        if L3>L1+L2:
            L3=L1+L2-4
        #L3最短不少于两臂之差
        if L3<abs(L1-L2):
            L3=abs(L1-L2)+4
        p=(L1+L2+L3)/2
        S=mt.sqrt(p*(p-L1)*(p-L2)*(p-L3))
        h=S*2/L3
        Q5=mt.asin(h/L2)/mt.pi*180
        Q4=mt.asin(y/L3)/mt.pi*180
        Q7=mt.asin(h/L1)/mt.pi*180
        Q1=180-Q5-Q7
        Q2=Q5+Q4
        #print("Q1,Q2",Q1,Q2)
        return Q1,Q2
    
    #输入参数为屏幕角度，不考虑电机面对面放置
    def scrdraw(self,angle1,angle2):
        #电机02
        self.m02.drawrelative(angle2)
        #杆02
        self.ml02.setangle(angle2)
        self.ml02.draw()
        #电机01放在杆02的右端
        self.m01.setcenter(self.ml02.rightend)
        self.m01.startangle=180+self.m02.angle
        if angle1<=0:
            angle1=0
        self.m01.drawrelative(angle1)
        #杆01固定在电机01中心，角度与电机01一样
        self.ml01.setjointpoint(self.m01.center)
        self.ml01.setangle(self.m01.angle)
        self.ml01.draw()
        self.ml01.drawrightend()
        #杆03永远保持垂直，中心点位于杆01右端下方
        self.ml03.setangle(90)
        L=int(self.ml03.width/2)
        self.ml03.center=np.add(self.ml01.rightend,(0,L))
        self.ml03.draw()
        self.ml03.drawrightend()
        if self.ser is not None:
            cv2.circle(img,(50,50),10,(0,255,0),3)
        else:
            cv2.circle(img,(50,50),10,(0,0,255),3)
        
    #输入角度考虑电机是否对面装配，然后画在图上   
    def robodraw(self,angle1,angle2):
        mangle1=angle1
        mangle2=angle2
        if self.m01.facetome == True:
            print("facetome")
            mangle1=self.m01.maxangle-angle1
        if self.m02.facetome == True:
            mangle2=slef.m02.maxangle-angle2
        print("mangle1,mangle2",mangle1,mangle2)
        self.scrdraw(mangle1,mangle2)
        
    def drawpwm(self,pwm1,pwm2):
        angle1disp=int((pwm1-500)/2000*180)   #自身角度
        angle2disp=int((pwm2-500)/2000*180)
        angel1=int(angle1disp*self.m01.maxangle/180)
        angel2=int(angle2disp*self.m02.maxangle/180)
        
        A1=180+50-(angel1+angel2)
        print("angle1disp,angle2disp,A1,%x,%x,"%(pwm1,pwm2),angle1disp,angle2disp,A1)
        self.robodraw(A1,angel2)
    def xytopwm(self,x,y):
        q1,q2=self.xytoq(x,y)
        # q1=180+50-(q2+pwmq1)
        pwmq1=180+50-(q1+q2)
        pwmq2=q2
        pwm1=int(pwmq1/180*2000+500)
        pwm2=int(pwmq2/180*2000+500)   #  角度
        return pwm1,pwm2
    
    def serwrite(self,pwm1,pwm2):
        if self.ser is None:
            return
        print(pwm1,pwm2)
        pw1str="%04x"%pwm1   #“%04x”  16进制输出  4位数
        pw2str="%04x"%pwm2
        print(pw1str,pw2str)
        mo1hexstr="ff 02 01"+" "+pw1str[2:4]+" "+pw1str[0:2]
        mo2hexstr="ff 02 02"+" "+pw2str[2:4]+" "+pw2str[0:2]
        self.ser.write(bytes.fromhex(mo1hexstr))
        self.ser.write(bytes.fromhex(mo2hexstr))
        return
    
    def robotTwin(self,x,y):
        pwm1,pwm2=self.xytopwm(x,y)
        self.drawpwm(pwm1,pwm2)
        self.serwrite(pwm1,pwm2)
def pmotor():
    global mMl03,mMl02,mMl01,mM01,mM02,mM03,marm
    #配置零件舵机
    mM02=mmotor((260+400,360),0,0,180)
    mM01=mmotor((0,0),0,0,180)
    mM03=mmotor((0,0),0,0,180)
    #配置零件梁
    mMl01=mlever((0,0),300,20,0)
    mMl02=mlever((0,0),300,20,0)
    mMl03=mlever((0,0),100,20,0)
    #组装成机械臂
    marm=Marm(mM01,mM02,mM03,mMl01,mMl02,mMl03)
    print(1)
'''
for i in range(60):
    x=i*10
    y=0
    marm.robotTwin(x,y)
    cv2.imshow("marm",img)
    if cv2.waitKey(100)&0xff == 27:
        break
    #恢复背景
    img=imgcon.copy()

for i in range(60):
    x=600-i*10
    y=0
    marm.robotTwin(x,y)
    cv2.imshow("marm",img)
    if cv2.waitKey(100)&0xff == 27:
        break
    #恢复背景
    img=imgcon.copy()
   
marm.ser.close()
cv2.destroyAllWindows()
'''
