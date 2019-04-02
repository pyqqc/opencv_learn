import marm as m
import cv2
m.pmotor()# 初始化变量
def a():
    m.marm.robotTwin(500,0)
    cv2.imshow("marm",m.img)

    #恢复背景
    m.img=m.imgcon.copy()
   
    cv2.destroyAllWindows()
a()
