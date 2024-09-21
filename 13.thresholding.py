import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('./Image/Image3.jpeg')
cv2.imshow('Original',img)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray',gray)

#Simple Thresholding
threshold,thresh=cv2.threshold(src=gray,thresh=130,maxval=255,type=cv2.THRESH_BINARY)
cv2.imshow('Simple Thresholding',thresh)

threshold,thresh_inv=cv2.threshold(gray,130,255,cv2.THRESH_BINARY_INV)
cv2.imshow('Simple Thresholding Inverse',thresh_inv)

#Adaptive Thresholding
adaptive_thresh=cv2.adaptiveThreshold(src=gray,maxValue=255,adaptiveMethod=cv2.ADAPTIVE_THRESH_GAUSSIAN_C,thresholdType=cv2.THRESH_BINARY,blockSize=11,C=3)
cv2.imshow('Adaptive Thresholding',adaptive_thresh)

adaptive_thresh_inv=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,3)
cv2.imshow('Adaptive Thresholding Inverse',adaptive_thresh_inv)

cv2.waitKey(0)