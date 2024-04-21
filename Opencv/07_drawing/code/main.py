import os
import numpy as np

import cv2


img = np.zeros((500,500,3), dtype='uint8') # gives blank img dtype of img
print(img.shape)

# 1. Paint the image a certain colour
img[200:300, 300:400] = 0,0,255 # BGR
cv2.imshow('Green', img)

# 2. Draw a Rectangle
cv2.rectangle(img, (0,0), (img.shape[1]//2, img.shape[0]//2), (0,255,0), thickness=-1) # 1 or 2 is thickness of line
cv2.imshow('Rectangle', img)

# 3. Draw A circle
cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 40, (0,0,255), thickness=3)
cv2.imshow('Circle', img)

# 4. Draw a line
cv2.line(img, (100,250), (300,400), (255,255,255), thickness=3)
cv2.imshow('Line', img)

# text
cv2.putText(img, 'Hey you!', (0,225), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 255, 0), 10)
cv2.imshow('Text', img)

# cv2.imshow('img', img)
cv2.waitKey(0)
