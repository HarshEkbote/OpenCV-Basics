import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('./Image/Image3.jpeg')
cv2.imshow('Original',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GRAY",gray)

#Laplacian Edge detection
lap=cv2.Laplacian(src=gray,ddepth=cv2.CV_64F)
lap=np.uint8(np.absolute(lap))
cv2.imshow('Laplacian',lap)

#Sobel
sobel_x=cv2.Sobel(gray,cv2.CV_64F,1,0)
sobel_y=cv2.Sobel(gray,cv2.CV_64F,0,1)

combine_sobel=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('Sobel_X',sobel_x)
cv2.imshow('Sobel_Y',sobel_y)
cv2.imshow('Sobel_Cobined',combine_sobel)

#Canny
canny=cv2.Canny(gray,150,175)
cv2.imshow('canny',canny)


cv2.waitKey(0)