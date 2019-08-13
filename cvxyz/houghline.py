import cv2
import numpy as np

img = cv2.imread('xyzb.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("xknzblines",gray)
cv2.waitKey()
edges = cv2.Canny(gray,100,150,apertureSize = 7)
minLineLength = 50
maxLineGap = 1
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        print(x1,y1,x2,y2)
cv2.imshow("xknzblines",img)
cv2.waitKey()
cv2.destroyAllWindows()
