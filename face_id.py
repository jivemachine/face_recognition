# imports 
import numpy as np
import face_recognition
import cv2

#were going to be using the Haar Cascade classifier for face detection. 
#It trains by using negative and positive images, after which it becomes 
#able to detect objects or in our case...faces :)

# we're going to use our webcam and we're giving openCV terminal access to our camera
capture = cv2.VideoCapture(0)

image = face_recognition.load_image_file("test.jpeg")
encode_image = face_recognition.face_encodings(image)[0]

known_face_encodings = [encode_image]
known_face_names = ["Jeremy"]

capture.set(3,640) # set Width
capture.set(4,480) # set height

while True:
    ret, img = capture.read()
    
    rgb_img = img[:, :, ::-1]
    
    #img = cv2.flip(img, -1)
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_recognition.face_locations(rgb_img)
    face_encodings = face_recognition.face_encodings(rgb_img, faces)

    for (x, y, w, h), face_encoding in zip(faces, face_encodings):

        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        face_distance = face_recognition.face_distance(known_face_encodings, face_encoding)

        best_match_index = np.argmin(face_distance)

        if matches[best_match_index]:
            name = known_face_names[best_match_index]




        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
        
        cv2.rectangle(img, (x, w -35), (y, w), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_TRIPLEX
        cv2.putText(img, name, (h + 6, w - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow("face_id", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()