import cv2 as cv
import numpy as np

cap=cv.VideoCapture("3月10日《不灭》.mp4")

#while(cap.isOpened()):
 #   ret,frame=cap.read()
  #  if ret==True:
   #     cv.imshow("frame",frame)
    #if cv.waitKey(25)&0xFF==ord("q"):
     #   break


#cap.release()
#cv.destroyWindows()

width=int(cap.get(3))
height=int(cap.get(4))
out=cv.VideoWriter("out.avi",cv.VideoWriter_fourcc("M","J","P","G"),10,(width,height))
while(True):
    ret,frame=cap.read()
    if ret==True:
        out.write(frame)
    else:
        break

cap.release()
out.release()
cv.destroyWindow()
