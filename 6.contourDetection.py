import cv2 
import numpy as np

img=cv2.imread("./Image/Image3.jpeg")
cv2.imshow("Original",img)

blank=np.zeros(img.shape,dtype='uint8')
cv2.imshow('Blank',blank)

grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Grey",grey)

# blur=cv2.GaussianBlur(grey,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow('Blur',blur)

# canny=cv2.Canny(blur,100,100)
# cv2.imshow("Canny",canny)

#OR

ret,thresh=cv2.threshold(grey,125,125,cv2.THRESH_BINARY)
cv2.imshow('Threshold',thresh)

contours,hierarchy=cv2.findContours(thresh,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv2.drawContours(blank,contours,-1,(200,200,200),1)
cv2.imshow('countour',blank)

cv2.waitKey(0)