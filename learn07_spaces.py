import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images/fuji.jpg")
img = cv.resize(img, (300, 300),interpolation=cv.INTER_CUBIC)
cv.imshow("Fuji", img)


# !Cannot convert grayscale to HSV
# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

plt.imshow(rgb)
plt.show()

# cv.waitKey(0)