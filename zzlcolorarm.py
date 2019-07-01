import numpy as np
import cv2


'''
#摄像装置
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('my_frame',frame)
cv2.waitKey(1000)
cv2.imwrite('pen2.jpg',frame)
cap.release()
cv2.destroyAllWindows()

#无光（75~90 7~11 1~22）
#自然（139~145 16~22 1~22）'''


cap=cv2.VideoCapture(0)

while(1): 

    # 获取每一帧 
    ret, frame=cap.read() 


    # 转换到    HSV 
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) # 设定红色的阈值 
    lower_red=np.array([0,200,0]) 
    upper_red=np.array([20,255,255])


    # 根据阈值构建掩模 
    mask=cv2.inRange(hsv,lower_red,upper_red) # 对原图像和掩模进行位运算 
    res=cv2.bitwise_and(frame,frame,mask=mask) # 显示图像 
    cv2.imshow('frame',frame) 
    cv2.imshow('mask',mask) 
    cv2.imshow('res',res)
    #显示轮廓
    ret,thresh = cv2.threshold(mask,127,255,0)
    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    print(len(contours))
    #测出最大的轮廓
    img=frame
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area>=400:
            img = cv2.drawContours(frame, [cnt], -1, (0,255,0), 3)
            #求轮廓中心
            M = cv2.moments(cnt) 
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00']) 
            cv2.circle(img,(cx,cy), 5, (255,0,0), -1)
    cv2.imshow('img',img)

        
    
    k=cv2.waitKey(5)&0xFF 
    if k==27: 
        break

# 关闭窗口 
cv2.destroyAllWindows()
