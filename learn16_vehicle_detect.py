import cv2 as cv

vehicle = cv.VideoCapture('videos/road_traffic.mp4')

ret, frame1 = vehicle.read()
ret, frame2 = vehicle.read()


while True:
    # Menemukan perbedaan mutlak antara piksel dari dua image (mendeteksi mobil bergerak)
    diff = cv.absdiff(frame1, frame2)
    # Convert ke gray
    gray = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    # Bluring
    blur = cv.GaussianBlur(gray, (5,5),0)
    # Threshold 
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)
    # Dilating
    dilated = cv.dilate(thresh, None, iterations=3)
    # Cari Contour
    contours,_ = cv.findContours(dilated, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw rectanglez
    for contour in contours:
        (x,y,w,h) = cv.boundingRect(contour)
        
        if cv.contourArea(contour)<700:
            continue
        cv.rectangle(frame1, (x,y), (x+w, y+h), (0,255,0), 2)
        cv.putText(frame1, 'VEHICLE', (x, y-4), cv.FONT_HERSHEY_SIMPLEX, 0.3, (0,255,0),1)
    # show video
    cv.imshow("vehicle", frame1)
    frame1 = frame2
    ret, frame2 = vehicle.read()

    # stop playing video when the end 
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

cv.destroyAllWindows()
vehicle.release()