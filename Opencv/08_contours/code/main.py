import os

import cv2
import cv2 as cv
import numpy as np

img = cv.imread('../../../media/Photos/cats.jpg')
cv.imshow('Cats', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY_INV)
cv.imshow('Thresh', thresh)

blur = cv.GaussianBlur(img_gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE) # or None
print(f'{len(contours)} contour(s) found!')

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

for cnt in contours:
    if cv2.contourArea(cnt) > 200:
        # cv2.drawContours(img, cnt, -1, (0, 255, 0), 1)

        x1, y1, w, h = cv2.boundingRect(cnt)

        cv2.rectangle(img, (x1, y1), (x1 + w, y1 + h), (0, 255, 0), 2)

cv2.imshow('img', img)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()