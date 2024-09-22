import cv2

img=cv2.imread('./image1.jpg')
cv2.imshow('Image',img)

#Convert image to greyscale
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray person',gray)

#Define the haar cascade classifier to read the xml file
haar_cascade=cv2.CascadeClassifier('haar_face.xml')


face_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=1)

#print number of people in image
print('Number of people in image:',len(face_rect))

#loop over the face_rect to plot the boxes
for x,y,w,h in face_rect:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('Detected faces',img)

cv2.waitKey(0)