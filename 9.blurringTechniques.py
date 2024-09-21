import cv2

# Smoothing is used when there is noise due to sensors.
img=cv2.imread('./Image/Image3.jpeg')
cv2.imshow('Original',img)

#Averaging Blur
average=cv2.blur(img,(3,3))
cv2.imshow("Average Blur",average)

#Gaussian Blur 
gaussian=cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('Gaussian',gaussian)

#Median Blur
median=cv2.medianBlur(img,3)
cv2.imshow('Median',median)

#Bilateral Blur
bilateral=cv2.bilateralFilter(img,10,35,25)
cv2.imshow('Bilateral',bilateral)
cv2.waitKey(0)