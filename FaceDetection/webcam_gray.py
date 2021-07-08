
import cv2;

# Using the Haar Cascade from OpenCV
face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml');

video = cv2.VideoCapture(0);

while True:
    check, frame = video.read();
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
                                          scaleFactor=1.1, minNeighbors=5);
    for x,y,w,h in faces:
        gray = cv2.rectangle(gray, (x,y), (x+w,y+h), (0,255,0), 3);

    cv2.imshow('Face Detector',gray);

    key = cv2.waitKey(1);

    if key == ord('q'):
        break;

video.release();
cv2.destroyAllWindows();

