import cv2 as cv

img = cv.imread("images/lenna.png")

cv.imshow("Lenna", img)

# Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Lenna Gray", gray)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow("Lenna Blur", blur)

# Edge Cascade
cany = cv.Canny(img, 125, 175)
# cv.imshow("Lenna Edge", cany) 

# Dilating the image (Melebarkan)
dilated = cv.dilate(cany, (5,5), iterations=2)
# cv.imshow("Lenna Dialted", dilated)

# Eroding (Mengikis)
eroded = cv.erode(dilated, (5,5), iterations=2)
# cv.imshow("Lenna Eroded", eroded)

# Resize
resized = cv.resize(img, (300, 300), interpolation=cv.INTER_AREA)
# cv.imshow("Lennar Resized", resized)

# Cropping
cropped = img[200:400, 200:400]
cv.imshow("Lenna Cropped", cropped)


cv.waitKey(0)