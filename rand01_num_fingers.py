import cv2 as cv
import numpy as np

img = cv.imread("images/fingers2.jpg")
cv.imshow("Hand", img)


# 1. Skin Mask
# Convert BGR to HSV
hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV Hand", hsvim)
# Lower Range Of Skin COLOR IN HSV
lower = np.array([0, 48, 80], dtype="uint8")
# Upper Range of Skin COlor in HSV
upper = np.array([20, 255, 255], dtype="uint8")
# Detect skin on the rang of lowe and upper pixel value in hsv colorspace
skinRegionHSV = cv.inRange(hsvim, lower, upper)
cv.imshow("Selection Hand", skinRegionHSV)
# Blurring image to improve masking
blurred = cv.blur(skinRegionHSV, (2,2))
cv.imshow("Blurred", blurred)
# Apllying threshold
_, thresh = cv.threshold(blurred, 0, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)


# 2. Find Contour
contours,_ = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
contours = max(contours, key=lambda x: cv.contourArea(x))
cv.drawContours(img, [contours], -1, (255, 255, 0), 2)
cv.imshow("Contours", img) 

# 3. Convex Hull
hull = cv.convexHull(contours)
cv.drawContours(img, [hull], -1, (0, 255, 255), 2)
cv.imshow("Hull", img)

# 4. Convexity Defects
hull = cv.convexHull(contours, returnPoints=False)
defects = cv.convexityDefects(contours, hull)

# 5. Counting dinger
if defects is not None:
    cnt = 0

for i in range(defects.shape[0]):
    s, e, f, d = defects[i][0]
    start = tuple(contours[s][0])
    end = tuple(contours[e][0])
    far = tuple(contours[f][0])

    a = np.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    b = np.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    c =  np.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

    angle = np.arccos((b**2 + c**2 - a**2) / (2*b*c))
    if angle <= np.pi/2:
        cnt+=1
        cv.circle(img, far, 4,  [0,0,255], -1)

if cnt > 0 :
    cnt+=1
cv.putText(img, str(cnt), (0, 50), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv.LINE_AA)


cv.imshow("Result", img)



cv.waitKey(0)