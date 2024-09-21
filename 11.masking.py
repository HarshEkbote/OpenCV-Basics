import cv2
import numpy as np

# mask need to be the same size/dimensions as the input image
img=cv2.imread('./Image/Image9.jpg')
cv2.imshow('Original',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
cv2.imshow('Blank',blank)

mask=cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv2.imshow('Mask',mask)

masked_image=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked image',masked_image)
cv2.waitKey(0)