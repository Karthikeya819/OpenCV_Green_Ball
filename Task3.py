import cv2 as cv
import numpy as np
video = cv.VideoCapture("./Video.mp4")
while True:
    isTrue,frame = video.read()
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_green = np.array([40, 40, 40])
    upper_green = np.array([75, 255, 255])
    mask = cv.inRange(hsv,lower_green,upper_green)
    contours,_ = cv.findContours(mask,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    for contour in contours:
     approx = cv.approxPolyDP(contour,0.01*cv.arcLength(contour,True),True)
     if(len(approx)>10):
        area = cv.contourArea(contour)
        if area >1600:
           x, y, w, h = cv.boundingRect(contour)
           cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
           cv.putText(frame, "Green Ball", (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv.putText(frame, "Davsam Karthikeya", (20, frame.shape[0] - 20), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv.imshow("Video",frame)
    if cv.waitKey(20) & 0XFF == ord('k'):
        break
video.release()
cv.destroyAllWindows()