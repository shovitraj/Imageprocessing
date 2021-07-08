import cv2;

# Using the Haar Cascade from OpenCV
smile_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_smile.xml');

video = cv2.VideoCapture(0);

while True:
    check, frame = video.read();
    
    smile = smile_cascade.detectMultiScale(frame,
                                          scaleFactor=1.1, minNeighbors=5);
    for x,y,w,h in eyes:
        RGB = cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3);
        
    cv2.imshow('Smile Detector',RGB);

    key = cv2.waitKey(1);

    if key == ord('q'):
        break;

video.release();
cv2.destroyAllWindows();
