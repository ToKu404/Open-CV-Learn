import cv2 as cv

# Function for rescale 
def rescaleFrame(frame, scale=0.75):
    # For Image, Video, and Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)

    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Only for Live Video
    capture.set(3, width)
    capture.set(4, height)


# Rescale implementation on image
img = cv.imread('images/model.jpg')
rescale_img = rescaleFrame(img, 0.3)
cv.imshow('Model',rescale_img)
cv.waitKey(0)

# Rescale implementation on Video
# capture = cv.VideoCapture('videos/kitten.mp4')
# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)
    
#     cv.imshow('Video', frame)
#     cv.imshow('Video REsized', frame_resized)

#     if cv.waitKey(20) & 0xFF==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

