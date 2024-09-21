import cv2
import numpy as np

blank=np.zeros((400,400),dtype='uint8')
rectangle=cv2.rectangle(blank.copy(),(30,30),(360,360),255,-1)
circle=cv2.circle(blank.copy(),(200,200),200,255,-1)

cv2.imshow('Rectangle',rectangle)
cv2.imshow('Circle',circle)

#bitwise AND  --> intersecting regions
bitwise_and=cv2.bitwise_and(rectangle,circle)
cv2.imshow('bitwise_and',bitwise_and)

#bitwise OR --> non intersecting and intersecting regions
bitwise_or=cv2.bitwise_or(rectangle,circle)
cv2.imshow('bitwise_or',bitwise_or)

#bitwise exor --> non intersecting regions
bitwise_xor=cv2.bitwise_xor(rectangle,circle)
cv2.imshow('bitwise_xor',bitwise_xor)

#bitwise_not --> invert the binary color
bitwise_not=cv2.bitwise_not(rectangle)
cv2.imshow('bitwise_not',bitwise_not)

cv2.waitKey(0)