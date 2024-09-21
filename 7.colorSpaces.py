import cv2
import matplotlib.pyplot as plt

img=cv2.imread('./Image/Image3.jpeg')
cv2.imshow('Original',img)

# plt.imshow(img)
# plt.show()

#BGR -> grey
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grey',grey)

#BGR->HSV
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('HSV',hsv)

#BGR->LAB
lab=cv2.cvtColor(img,cv2.COLOR_BGR2LAB)
cv2.imshow('LAB',lab)

#BGR->RGB
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow("RGB",rgb)

plt.imshow(rgb)
plt.show()

#HSV->BGR
hsv_bgr=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV to BGR',hsv_bgr)

#LAB->BGR
lab_bgr=cv2.cvtColor(lab,cv2.COLOR_LAB2BGR)
cv2.imshow('LAB to BGR',lab_bgr)

#for gray to HSV/LAB we first convert grayscale image to BGR and the the BGR to HSV/LAB

cv2.waitKey(0)