import cv2
import matplotlib.pyplot as plt
import numpy as np

img=cv2.imread('./Image/Image3.jpeg')
#cv2.imshow('Original',img)

blank=np.zeros(img.shape[:2],dtype='uint8')
mask=cv2.circle(blank,(img.shape[1]//2,img.shape[0]//2),40,255,-1)

# grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('GreyScale',grey)

#GreyScale Histogram for entire image
#gray_hist=cv2.calcHist([grey],[0],None,[256],[0,256])

#Histogram for a mask
# mask= cv2.bitwise_and(grey,grey,mask=circl)
# cv2.imshow('Mask',mask)
# gray_hist=cv2.calcHist([grey],[0],mask,[256],[0,256])


#Color Histogram
masked_image= cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('Masked',masked_image)
plt.figure()
plt.title('Color histogram')
plt.xlabel('Bins')
plt.ylabel('No of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist=cv2.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()



# plt.figure()
# plt.title('Grey histogram')
# plt.xlabel('Bins')
# plt.ylabel('No of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

cv2.waitKey(0)