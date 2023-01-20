import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
frameWidth = 640
frameHeight = 480
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
def empty(a):
    pass

cv.namedWindow("HSV")
cv.resizeWindow("HSV",640,240)
cv.createTrackbar("Hue Min","HSV",0,179,empty)
cv.createTrackbar("Sat Min","HSV",0,255,empty)
cv.createTrackbar("Val Min","HSV",0,255,empty)
cv.createTrackbar("Hue Max","HSV",179,179,empty)
cv.createTrackbar("Sat Max","HSV",255,255,empty)
cv.createTrackbar("Val Max","HSV",255,255,empty)

def findColors():
    pass


while True:
    _, frames = cap.read()
    frames_hsv = cv.cvtColor(frames, cv.COLOR_BGR2HSV)


    h_min = cv.getTrackbarPos("Hue Min", "HSV")
    s_min = cv.getTrackbarPos("Sat Min", "HSV")
    v_min = cv.getTrackbarPos("Val Min", "HSV")
    h_max = cv.getTrackbarPos("Hue Max", "HSV")
    s_max = cv.getTrackbarPos("Sat Max", "HSV")
    v_max = cv.getTrackbarPos("Val Max", "HSV")

    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv.inRange(frames_hsv, lower, upper)
    result = cv.bitwise_and(frames,frames,mask=mask)
    mask = cv.cvtColor(mask, cv.COLOR_GRAY2BGR)

    cv.imshow("Video", frames)
    cv.imshow("Result", result)
    cv.imshow("Mask", mask)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break

cap.release()
cv.destroyAllWindows()