# imports 
import numpy as np
import cv2

#were going to be using the Haar Cascade classifier for face detection. 
#It trains by using negative and positive images, after which it becomes 
#able to detect objects or in our case...faces :)

# importing our model from cv2
face_cascade = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml")

# we're going to use our webcam and we're giving openCV terminal access to our camera
capture = cv2.VideoCapture(0)
capture.set(3,640) # set Width
capture.set(4,480) # set height

# webcam turns green ;L

while True:
    ret, img = capture.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,    

       scaleFactor=1.2,

       minNeighbors=5,    

       minSize=(20, 20)

   )
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color= img[y:y+h, x:x+2]
    
    cv2.imshow("video", img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press ESC to quit
        break

    cap.releaseAllWindows()