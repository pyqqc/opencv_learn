import cv2

img=cv2.imread("bbb.jpg")
cv2.imshow("img",img)
cv2.waitKey()
cv2.detroyAllWindows()
