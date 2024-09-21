import cv2
import numpy as np

img= cv2.imread('./Image/Image2.jpeg')
cv2.imshow("Original",img)

# 1. Translation
# -x ---> Left   x ---> Right
# -y ---> Up   y ---> Down
# def translate(img,x,y):
#     mat=np.float32([[1,0,x],[0,1,y]])
#     dims=(img.shape[1],img.shape[0])
#     return cv2.warpAffine(img,mat,dims)
# translated=translate(img,-100,10)
# cv2.imshow("Translation",translated)

# 2.Rotation

# def rotate(img,angle,rotPoint=None):
#     (height,width)=img.shape[:2]
#     if rotPoint==None:
#         rotPoint=(width//2,height//2)
#     rotMat=cv2.getRotationMatrix2D(rotPoint,angle,scale=1.0)
#     dimensions=(width,height)
#     return cv2.warpAffine(img,rotMat,dimensions)
# rotated=rotate(img,45)
# cv2.imshow("Rotation",rotated)

# 3. Resize
# resized=cv2.resize(img,(550,500),interpolation=cv2.INTER_CUBIC)
# cv2.imshow("Resize",resized)

# 4. Flip image
# flipCode 0: flip vertically 
# flip code 1: flip horizontally
# flip code -1: flip both
# flipped=cv2.flip(img,1)
# cv2.imshow("Flipped vertically",flipped)

#5. Cropped
# cropped=img[10:30,10:50]
# cv2.imshow("Cropped",cropped)

cv2.waitKey(0)