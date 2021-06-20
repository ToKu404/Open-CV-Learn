import cv2 as cv
import numpy as np

img  = cv.imread("images/lenna.png")
cv.imshow("Lenna", img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow("Blur",blur)

canny = cv.Canny(img, 125, 175)
cv.imshow("Canny Edges", canny)

# thresshold
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh", thresh)

contour, hierarchies = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
print(f'{len(contour)} contours(s) found!')

cv.drawContours(blank, contour, -1, (255,0,0), 1)
cv.imshow("Contours Drawn", blank)

cv.waitKey(0)