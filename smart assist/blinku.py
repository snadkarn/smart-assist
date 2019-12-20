import cv2
import numpy as np
import dlib
from math import hypot
import time
import urllib
import urllib.request
from win32api import GetSystemMetrics

cap = cv2.VideoCapture(0)

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
li=[0]
sum=0
def midpoint(p1 ,p2):
    return int((p1.x + p2.x)/2), int((p1.y + p2.y)/2)

font = cv2.FONT_HERSHEY_PLAIN

def get_blinking_ratio(eye_points, facial_landmarks):
    left_point = (facial_landmarks.part(eye_points[0]).x, facial_landmarks.part(eye_points[0]).y)
    right_point = (facial_landmarks.part(eye_points[3]).x, facial_landmarks.part(eye_points[3]).y)
    center_top = midpoint(facial_landmarks.part(eye_points[1]), facial_landmarks.part(eye_points[2]))
    center_bottom = midpoint(facial_landmarks.part(eye_points[5]), facial_landmarks.part(eye_points[4]))

    hor_line = cv2.line(frame, left_point, right_point, (0, 255, 0), 2)
    ver_line = cv2.line(frame, center_top, center_bottom, (0, 255, 0), 2)

    hor_line_lenght = hypot((left_point[0] - right_point[0]), (left_point[1] - right_point[1]))
    ver_line_lenght = hypot((center_top[0] - center_bottom[0]), (center_top[1] - center_bottom[1]))

    ratio = hor_line_lenght / ver_line_lenght
    return ratio

while True:
    start=time.time()
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = detector(gray)
    for face in faces:
        #x, y = face.left(), face.top()
        #x1, y1 = face.right(), face.bottom()
        #cv2.rectangle(frame, (x, y), (x1, y1), (0, 255, 0), 2)

        landmarks = predictor(gray, face)

        left_eye_ratio = get_blinking_ratio([36, 37, 38, 39, 40, 41], landmarks)
        right_eye_ratio = get_blinking_ratio([42, 43, 44, 45, 46, 47], landmarks)
        blinking_ratio = (left_eye_ratio + right_eye_ratio) / 2
        
        #start=time.time()
        
        
        
        
       
        if blinking_ratio > 5.7:
            cv2.putText(frame, "BLINKING", (50, 150), font, 7, (255, 0, 0))
            
            
            
       
        #end=time.time()
        
        #eltime=end-start
        ##if eltime>start and eltime<end:
        
        #print(li)
        #else:
            #break
        end=time.time()
        #print(end-start)

        
    cv2.imshow("Frame", frame)
    
    key = cv2.waitKey(3)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
W=680
H=384
#cap = cv2.VideoCapture("eye_recording.flv")
#cap = cv2.VideoCapture(0)
url='http://192.168.43.169:8080/shot.jpg'


while True:
    # Use urllib to get the image from the IP camera
    #imgResp = urllib.urlopen(url)
    imgResp =urllib.request.urlopen(url)
    
    # Numpy to convert into a array
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    
    # Finally decode the array to OpenCV usable format ;) 
    img = cv2.imdecode(imgNp,-1)
	
	
	# put the image on screen
    cv2.imshow('IPWebcam',img)

#while True:
    #ret, frame = cap.read()
    #if ret is False:
       # break
 
    #roi = frame[269: 795, 537: 1416]
    #roi = frame[192: 576, 340: 1020]
    roi = img[192: 576, 340: 1020]
    rows, cols, _ = roi.shape
    gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)
 
   # _, threshold = cv2.threshold(gray_roi, 3, 255, cv2.THRESH_BINARY_INV)
    _, threshold = cv2.threshold(gray_roi, 50, 255, cv2.THRESH_BINARY_INV)
    _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
 
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
 
        #cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.line(roi, (x + int(w/2), 0), (x + int(w/2), rows), (0, 255, 0), 2)
        cv2.line(roi, (0, y + int(h/2)), (cols, y + int(h/2)), (0, 255, 0), 2)
        if(x>0.7*W):
            print('right')
        elif(x<0.3*W):
            print('left')
        if(y>0.7*H):
            print('top')
        elif(y<0.3*H):
            print('bottom')
        break
 
    cv2.imshow("Threshold", threshold)
    cv2.imshow("gray roi", gray_roi)
    cv2.imshow("Roi", roi)
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cv2.destroyAllWindows()