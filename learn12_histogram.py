import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("images/lenna.png")
cv.imshow("Lenna", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Grayscale Histogram
gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

# plt.figure()
# plt.title("Grayscael histogram")
# plt.xlabel("bins")
# plt.ylabel("# of pixels")
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

# Color Histogram
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.title("Colours histogram")
plt.xlabel("bins")
plt.ylabel("# of pixels")
plt.show()
cv.waitKey(0)