import cv2
import pygraphviz as pgv
G=pgv.AGraph("graphdemo.dot")
G.add_node("a")
G.layout(prog='dot')
G.draw("xkngd.jpg")
img=cv2.imread("xkngd.jpg")
cv2.imshow("xkngdlayout",img)
cv2.waitKey()
cv2.destroyAllWindows()

