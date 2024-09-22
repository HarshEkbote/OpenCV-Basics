import numpy as np
import cv2

haar_cascade=cv2.CascadeClassifier('face_detect.xml')
people=['Henry Cavill','Hugh Jackman','Robert Downey Jr','Scarlett Johansson','Sydney Sweeney']

features=np.load('features.npy',allow_pickle=True)
labels=np.load('lables.npy')

face_recogniser=cv2.face.LBPHFaceRecognizer_create()
face_recogniser.read('face_trained.yaml')

img=cv2.imread('./val_image1.jpeg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Person',gray)


#Detect face in image
face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
for (x,y,w,h) in face_rect:
    face_roi=gray[y:y+h,x:x+h]
    
    label,conf=face_recogniser.predict(face_roi)
    print(f'Label:{people[label]}\nConfidence:{conf}')
    
    cv2.putText(img,str(people[label]),(20,20),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),2)
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Detected image',img)
cv2.waitKey(0)
