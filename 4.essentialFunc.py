import cv2

img=cv2.imread('./Image/Image2.jpeg')
# cv2.imshow('Original',img)

#1. Convert Image to Greyscale
# grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grey',grey)


#2. To Blur an Image
# blur=cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
# cv2.imshow('Blur',blur)

#3. Edge Cascade (to find edges in the image)
# edge=cv2.Canny(img,145,241)  #we can also pass the blur image to reduce the number of edges
# cv2.imshow('Edge Detector',edge)

# #4. Dilating the image
# dilated=cv2.dilate(edge,(7,7),iterations=5)
# cv2.imshow('Dilated',dilated)

# #5. Eroding
# eroded=cv2.erode(dilated,(7,7),iterations=5)
# cv2.imshow("Eroded",eroded)

# #6. Resize image
# resize=cv2.resize(img,(500,500),interpolation=cv2.INTER_CUBIC)   
# #If image size is increased than original use cv2.INTER_LINEAR or cv2.INNER_CUBIC for interpolation
# #IF image size is reduced than original image the use cv2.INNER_AREA for interpolation
# cv2.imshow('Resized',resize)

#7. Cropping
# cropped=img[10:30,50:80]
# cv2.imshow("Crop",cropped)

cv2.waitKey(0)