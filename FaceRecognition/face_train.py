import os
import cv2
import numpy as np

#Get the list of the folders for the person to recognize
#people=['Henry Cavill','Hugh Jackman','Robert Downey Jr','Scarlett Johansson','Sydney Sweeney']
people=[]
for i in os.listdir(r"D:\ML Basics\OpenCV\FaceRecognition\Face_images"):
    people.append(i)
#print(people)

haar_cascade=cv2.CascadeClassifier('face_detect.xml')

DIR="D:\ML Basics\OpenCV\FaceRecognition\Face_images"

features=[]
labels=[]
def create_train():
    for person in people:
        path=os.path.join(DIR,person)
        label=people.index(person)
        
        for image in os.listdir(path):
            img_path=os.path.join(path,image)
            img_array=cv2.imread(img_path)
            gray=cv2.cvtColor(img_array,cv2.COLOR_BGR2GRAY)
            
            faces_rect=haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
            for (x,y,w,h) in faces_rect:
                faces_roi=gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print('Training Done------')
face_recogniser=cv2.face.LBPHFaceRecognizer_create()

#train the recognizer on featrure list and labels list
features=np.array(features,dtype='object')
labels=np.array(labels)
face_recogniser.train(features,labels)

face_recogniser.save('face_trained.yaml')
np.save('features.npy',features)
np.save('lables.npy',labels)


