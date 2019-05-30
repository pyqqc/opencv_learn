import pyautogui as pg
import cv2
import time
import numpy as np

time.sleep(5)

def waitsleep(sec):
    num=int(sec/0.5)
    for i in range(num):
        waitandhit()

def locateOnScreen2():
    W=1920
    H=1080
    #print("hhhhhhhh")
    pic=pg.screenshot()
    img = cv2.cvtColor(np.array(pic),cv2.COLOR_RGB2BGR)
    print("before screenshot")
    cv2.imwrite("screenshot.png",img)
    #img=cv2.imread("bh3.jpg")
    template = cv2.imread('final white.png')
    (h, w )= template.shape[:2]
    
    #cv2.imshow("img",img)
    #cv2.imshow("tem",template)
    #cv2.waitKey()
    #cv2.destroyAllWindows()

    res = cv2.matchTemplate(img,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.7

    loc = np.where( res >= threshold)
    poss=[]
    for pt in zip(*loc[::-1]):
        poss.append(pt)
        #cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (200,0,255), 2)
    #print(poss)

    L=[]

    xc=W/2
    yc=H/2
    for pos in poss:
        x=pos[0]-xc
        y=pos[1]-yc
        L.append(x*x+y*y)

    #print(min(L))
    if L ==[]:
        return []
    Lind=L.index(min(L))
    #print(poss[Lind])


    fposs=[]

    Eposs=poss

    d=8
    fposs.append(Eposs[0])
    for espos in Eposs:
        fposse=fposs[-1]
        x1=espos[0]
        y1=espos[1]
        x2=fposse[0]
        y2=fposse[1]
        x=x1-x2
        y=y1-y2
        l=x*x+y*y
    
        if l>d:
            fposs.append(espos)
        else:
            fposs[-1]=espos
        
    for fpos in fposs:
        cv2.rectangle(img, fpos, (fpos[0] + w, fpos[1] + h), (200,0,255), 2)
        #print(fpos)
    
    
    cv2.imshow("img",img)
    cv2.waitKey(2000)
    
    if len(fposs) >0:
        return fposs[0]
    else:
        return []

def waitandhit():
    pg.typewrite("1")
    counter=1
    while True:
        try:
            counter+=1
            print("before locateonscreen")
            box=locateOnScreen2()
            print("after locateonscreen")
            break
        except:
            time.sleep(0.2)
            print("notfound")
            if counter>10:
                return 0
            
    
    if box ==[]:
        print("notfound")
    else:
        
        print(box)
        print(box[0])
        print(box[1])
        print("found")
        time.sleep(0.5)
        pg.typewrite(" ")
        time.sleep(0.5)
        pg.keyUp("w")
        time.sleep(1)
      
        pg.click(box[0]+50,box[1]+30,button='right')
        #time.sleep(1)
        #pg.click()
 
        pg.typewrite("2")
        time.sleep(2)
        print("hit2")
        pg.typewrite("1")
        time.sleep(2)
        print("hit1")
        pg.typewrite("-")
        time.sleep(2)
        print("hit-")
        pg.typewrite("1")
        print("hit1")
        time.sleep(2)
        pg.typewrite("8")
        time.sleep(2)
        pg.typewrite("1")
        time.sleep(2)
        pg.typewrite("-")
        time.sleep(2)
        pg.typewrite("-")
        time.sleep(2)
        pg.typewrite("2")
        time.sleep(2)
        pg.typewrite("8")
        time.sleep(2)
        pg.typewrite("1")
        time.sleep(2)
        pg.typewrite("1")
        time.sleep(2)
        pg.typewrite("-")
        time.sleep(2)
        pg.typewrite("5")
        print("hitend")


while True:
    for i in range(6):
        pg.keyDown("w")
        waitsleep(1)
        pg.keyUp("w")
    for i in range(1):
        pg.keyDown("a")
        time.sleep(0.855)
        pg.keyUp("a")
        print("turn")
