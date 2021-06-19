import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype='uint8')
# cv.imshow('Blank', blank)

# IMPORTANT COLOR IS = BGR

# 1. Paint the image a certain color
# blank[:] = 255, 255, 255
# blank[200:300] = 0,0,255
# blank[:,200:300] = 0,0,255
# cv.imshow('England Flag', blank)

# 2. Draw a Rectangle
# source, sudut1, sudut2, warna, ketebalan
# 0,50 = x=0 , y=50 
# 250, 0 = x=250, y=0 
# thikness = -1 (filled) atau 2
print(len(blank))
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,255), thickness=-1)
cv.rectangle(blank, (blank.shape[1]//2, blank.shape[0]//2), (blank.shape[1], blank.shape[0]), (0,255,255), thickness=-1)
# cv.imshow('Rectangle', blank)


# 3. Draw a Circle
# source, center, radius, color, ketebalan
cv.circle(blank, (250, 250), 40, (0,0,255), thickness=-1)
# cv.imshow('Circle', blank)

# 4. Draw a Line
cv.line(blank, (0,500), (500,0), (255,255,255), thickness=5)
# cv.imshow("Line", blank)

# 5. Draw Eclipse
# src, center, axes, angle, startAngle, endAngle, color, thikness
cv.ellipse(blank,(250,375),(100,50),0,0,180,(255,255,255),-1)


# 6. Write a Text
# src, text, titik mulai, font, font scale, color, thikness
cv.putText(blank, "Nuclear", (145,125), cv.FONT_HERSHEY_TRIPLEX,1.5, (255,255,255), 3)
cv.imshow("Text", blank)



cv.waitKey(0)
