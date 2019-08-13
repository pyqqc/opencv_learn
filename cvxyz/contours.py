import numpy as np
import cv2

im = cv2.imread('xyz0.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)

#cv2.drawContours(im, contours, -1, (0,255,0), 3)

'''
for cnt in contours:
    cv2.drawContours(im, [cnt], 0, (0,255,0), 1)
    x,y,w,h = cv2.boundingRect(cnt)
    im = cv2.rectangle(im,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("contours",im)
    cv2.waitKey(100)
'''
for cnt in contours:
    cv2.drawContours(im, [cnt], 0, (0,255,0), 1)
    area = cv2.contourArea(cnt)
    if area >10000 or area < 100:
        continue
    print("area=",area)
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.drawContours(im,[box],0,(0,0,255),2)
    cv2.imshow("contours",im)
    cv2.waitKey(100)
cv2.waitKey()
cv2.destroyAllWindows()

