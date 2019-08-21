import numpy as np
import cv2
# Load an color image in grayscale
img=cv2.imread("glass.jpg")
cv2.namedWindow('glass', cv2.WINDOW_NORMAL)
print(img.shape)


cv2.imshow('glass',img)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    for y in range(3):
        for x in range(3):
            frame[0+60*y:60+60*y,0+80*x:80+80*x]=img[250:310,250:330]
            cv2.rectangle(frame,(0+80*x,0+60*y),(80+80*x,60+60*y),(0,255,0),3)
    cv2.imshow("11",frame)

    
    key=cv2.waitKey(100)
    print(key)

    if key==27:
        cv2.destroyAllWindows()
        break
cap.release()
