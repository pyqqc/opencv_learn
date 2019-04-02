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






for i in range(10):
    angle=i*10
    #电机02
    drawmotor(centerm2,angle) 
    cv2.imshow("marm",img)
    cv2.waitKey(1000)
    #恢复背景
    img=imgcon.copy()

cv2.destroyAllWindows()

