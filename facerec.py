import cv2, time
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyes_cascade= cv2.CascadeClassifier("haarcascade_eye.xml")
smile_cascade= cv2.CascadeClassifier("haarcascade_smile.xml")
cam=cv2.VideoCapture(0)
while True:
    check,img=cam.read()
    blackw=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face=face_cascade.detectMultiScale(blackw,scaleFactor=1.1,minNeighbors=5)
    for x,y,w,h in face:
        vid=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
        smile=smile_cascade.detectMultiScale(blackw,scaleFactor=1.3,minNeighbors=20)
        eyes=eyes_cascade.detectMultiScale(blackw,scaleFactor=1.3,minNeighbors=20)
    for x,y,w,h in smile:
        vid=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
    for x,y,w,h in eyes:
        vid=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow('hello',img)
    if cv2.waitKey(1) & 0xFF==('q'): 
        break
cam.release()
cv2.destroyAllWindows

