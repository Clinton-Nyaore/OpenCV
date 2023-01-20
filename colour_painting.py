import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

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

my_colors = [[0,91,0,60,255,255]]
myColorValues = [[51,153,255]]
my_points = []

def findColors(frames, my_colors, myColorValues):
    count = 0
    new_points = []
    img_hsv = cv.cvtColor(frames, cv.COLOR_BGR2HSV)
    lower = np.array(my_colors[0][0:3])
    upper = np.array(my_colors[0][3:6])
    mask = cv.inRange(img_hsv, lower, upper)
    x, y = getContours(mask)
    cv.circle(result, (x,y), 10, myColorValues[0], cv.FILLED)
    if x!=0 and y!=0:
        new_points.append([x,y,count])
    count += 1
    return new_points
    #cv.imshow("Mask", mask)

def getContours(frames):
    contours, _ = cv.findContours(frames,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        cv.drawContours(result, cnt, -1, (255,0,0),3)
        peri = cv.arcLength(cnt, True)
        approx = cv.approxPolyDP(cnt, 0.02*peri, True)
        x,y,w,h = cv.boundingRect(approx)
    return x+w//2,y


def drawOnCanvas(my_points, myColorValues):
    for point in my_points:
        cv.circle(result, (point[0],point[1]), 10, myColorValues[point[2]], cv.FILLED)


while True:
    _, frames = cap.read()
    result = frames.copy()
    new_points = findColors(frames, my_colors, myColorValues)
    if len(new_points)!=0:
        for newp in new_points:
            my_points.append(newp)
    if len(my_points)!=0:
        drawOnCanvas(my_points, myColorValues)
    cv.imshow("Video", result)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break