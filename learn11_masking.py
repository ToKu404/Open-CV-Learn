import cv2 as cv
import numpy as np

img = cv.imread("images/lenna.png")
cv.imshow("Lenna", img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow("Blank Image", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 50, img.shape[0]//2), 100, 255, -1)
rectangle = cv.rectangle(blank.copy(), (30,30),(370, 370), 255, -1)
mask = cv.bitwise_and(circle, rectangle)
# cv.imshow("Mask", mask)




masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow("Masked Image", masked)


cv.waitKey(0)