import cv2 as cv

img = cv.imread('images/model.jpg')
img = cv.resize(img, (300, 300),interpolation=cv.INTER_CUBIC)
# cv.imshow('Model', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow("Gaussian Blur", gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median Blur", median) 

# Bilaterial
bilateral = cv.bilateralFilter(img, 10, 35, 25) 
cv.imshow("Bilaterial Blur", bilateral)

cv.waitKey(0)