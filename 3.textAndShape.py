import cv2
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8') #create a blank image
cv2.imshow('Blank',blank)

#1. Create a whole blank canvas for certain color
# blank[:]=0,255,0
# cv2.imshow('Green',blank)

#2. Only paint a certain portion of the blank canvas
# blank[100:300,300:400]=78,20,40
# cv2.imshow('Portion Color',blank)

#3. Draw a rectangle
# cv2.rectangle(blank, (100,200),(300,400),(100,50,26),thickness=5)  # to fill rectangle thickness=cv2.FILLED or -1
# cv2.imshow('Rectange',blank)

#4. Draw a circle
# cv2.circle(blank,(200,400),70,(180,110,170),thickness=-1)
# cv2.imshow('Circle',blank)

#5. Draw line
# cv2.line(blank,(100,200),(250,250),(180,180,180),thickness=2)
# cv2.imshow('Line',blank)

#6. Text on image
# cv2.putText(blank,'HEllo',(250,200),cv2.FONT_HERSHEY_TRIPLEX,1.3,(200,200,200),2)
# cv2.imshow('Text',blank)

#cv2.waitKey(0)