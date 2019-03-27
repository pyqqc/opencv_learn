import marm as m
import cv2
m.pmotor()# 初始化变量
for i in range(60):
    x=600-i*10
    y=0
    m.marm.robotTwin(x,y)
    cv2.imshow("marm",m.img)
    if cv2.waitKey(100)&0xff == 27:
        break
    #恢复背景
    m.img=m.imgcon.copy()
   
cv2.destroyAllWindows()
