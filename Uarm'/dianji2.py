import cv2
import numpy as np
import math  as mt

img=cv2.imread("marm.jpg")

#图像缩一半便于屏幕显示处理
shape=img.shape
print(shape)
H=int(shape[0]/2)
W=int(shape[1]/2)
print(W,H)
img=cv2.resize(img,(W,H))
imgcon=img.copy()
print(img.shape)

centerm2=(260,360)
centerm1=(500,140)
def drawmotor(centerm,angle):
    color=(0,255,0)
    r=30
    cv2.circle(img,centerm,r,color,5)
    rect=(centerm,(2*r,4),angle)
    box = cv2.boxPoints(rect).astype(np.int0)
    cv2.drawContours(img,[box],0,(255,0,0),3)



joitpoint=(260,360)
centerl=(0,0)
widthl=340
highl=20

#中心点，长度，角度
def drawlever(center,widthl,highl,angle):
    heightl=10
    
    w=int(widthl/2*mt.cos(angle/180*mt.pi))
    h=int(widthl/2*mt.sin(angle/180*mt.pi))
    center=joitpoint-np.array([w,h])
    rect=(center, (widthl, heightl), angle)
    box = cv2.boxPoints(rect).astype(np.int0)
    cv2.drawContours(img,[box],0,(255,0,0),3)


#电机01的位置变化
mc1=[(-80,360),(-74,302),(-58,244),(-34,192),(0,142),(42,100),(90,66),(144,42),(202,26),(260,20)]


for i in range(10):
    angle=i*10
    #电机02
    drawmotor(centerm2,angle)
    drawlever(centerl,widthl,highl,angle)    
    drawmotor(mc1[i],angle)
    cv2.imshow("marm",img)
    cv2.waitKey(1000)
    #恢复背景
    img=imgcon.copy()

cv2.destroyAllWindows()

