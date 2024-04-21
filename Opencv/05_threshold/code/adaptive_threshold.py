import os
import cv2 as cv
import cv2


img = cv.imread('../../../media/Photos/cats.jpg')
cv.imshow('Cats', img)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Simple Thresholding
threshold, thresh = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY )
cv.imshow('Simple Thresholded', thresh)

threshold, thresh_inv = cv.threshold(img_gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 10)
# ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)


# cv2.imshow('img', img)
cv2.imshow('adaptive_thresh', adaptive_thresh)
# cv2.imshow('simple_thresh', simple_thresh)
cv2.waitKey(0)