import cv2 as cv

facedetect=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
cam=cv.VideoCapture(0)
while(True):
    ret,img=cam.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces=facedetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    img=cv.flip(img,1)
    cv.imshow('detection',img)
    if cv.waitKey(0)==ord('q'):
        break
cv.waitKey()
cam.release()
cv.destroyAllWindows()

'''

import cv2 as cv
eyedetect=cv.CascadeClassifier("haarcascade_eye.xml")
cam=cv.VideoCapture(0)
while(True):
    ret,img=cam.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    eyes=eyedetect.detectMultiScale(gray,1.3,5)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(img,(ex,ey),(ex+ew,ey+eh),(255,255,0),2)
    img=cv.flip(img,2)
    cv.imshow("Detection image",img)
    if cv.waitKey(0)==ord("q"):
        break
cv.waitKey()
cam.release()
cv.destroyAllWindows()


import cv2 as cv

smiledetect=cv.CascadeClassifier("haarcascade_smile.xml")

cam=cv.VideoCapture(0)

while(True):
    ret,img=cam.read()
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    smiles=smiledetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in smiles:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    img=cv.flip(img,1)
    cv.imshow("Smile detection",img)
    if cv.waitKey(0)==ord("q"):
        break
cv.waitKey()
cam.release()
cv.destroyAllWindows()

'''



