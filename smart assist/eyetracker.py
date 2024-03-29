import numpy as np
import cv2
#import socket
#import time

from time import sleep

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

#hostMACAddress = 'FC:A8:9A:00:3C:A6'
#port = 1 
##size = 1024
#s=socket.socket(socket.AF_BLUETOOTH,socket.SOCK_STREAM,socket.BTPROTO_RFCOMM)
#s.connect((hostMACAddress,port))
#number signifies camera
cap = cv2.VideoCapture(0)

while 1:
    sleep(2)
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        roi_color2 = img[ey:ey+eh, ex:ex+ew]
        circles = cv2.HoughCircles(roi_gray2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
        try:
            for i in circles[0,:]:
                # draw the outer circle
                cv2.circle(roi_color2,(i[0],i[1]),i[2],(255,255,255),2)
                print("drawing circle")
                # draw the center of the circle
                cv2.circle(roi_color2,(i[0],i[1]),2,(255,255,255),3)
                
                print(i[0])
                print(i[1])
        except Exception as e:
            print (e)
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

#def move():
   # s.send("1".encode())
   # s.send("2".encode())
   # s.send("3".encode())
   # s.send("4".encode())
   # s.send("5".encode())
    
    
#move()

cap.release()
cv2.destroyAllWindows()