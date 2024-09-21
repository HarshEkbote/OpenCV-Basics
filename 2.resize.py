# import cv2
#Rescale an Image or Video


# def changeRes(width,height): #will only work for Live Video
#     capture.set(3,width)
#     capture.set(4,height)
    
# def rescaleFrame(frame,scale=0.75): #Will work for Image,Video as well as Live video
#     height=int(frame.shape[0]*scale)
#     width=int(frame.shape[1]*scale)
#     dimensions=(width,height)
#     return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)

# capture=cv2.VideoCapture('Video/Video3.mp4')
# while True:
#     isTrue,frame=capture.read()
#     if isTrue:
#         rescaledFrame=rescaleFrame(frame)
#         cv2.imshow('Rescaled Image',rescaledFrame)
#         cv2.imshow('Video',frame)
#     else:
#         break
#     if cv2.waitKey(20) & 0xFF==ord('d'):
#         break
# capture.release()
# cv2.destroyAllWindows()