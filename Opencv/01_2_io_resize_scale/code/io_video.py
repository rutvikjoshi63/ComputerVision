import os
import cv2

# read video
# 0 for webcam
video = cv2.VideoCapture('../../../media/Videos/dog.mp4')

# Rescale
def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
def changeRes(width,height):
    # Live video
    video.set(3,width)
    video.set(4,height)
    
# visualize video
ret = True
while ret:
    ret, frame = video.read()
    # Rescale
    frame_rescaled = rescaleFrame(frame)
    
    if ret:
        cv2.imshow('frame_rescaled', frame_rescaled)
        cv2.imshow('frame', frame)
        # cv2.waitKey(40)
        if cv2.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break


video.release()
cv2.destroyAllWindows()