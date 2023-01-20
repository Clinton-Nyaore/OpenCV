import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

image_width = 640
image_height = 480
def preProcess(image):
    image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    image_blur = cv.GaussianBlur(image_gray, (5,5), 1)
    image_canny = cv.Canny(image_blur, 200, 200)
    kernel = np.ones((5,5))
    image_dilate = cv.dilate(image_canny, kernel, iterations=2)
    image_thres = cv.erode(image_dilate, kernel, iterations=1)

    return image_thres


def getContours(image):
    biggest = np.array([])
    max_area = 0
    contours, _ = cv.findContours(image,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            
            peri = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            if area>max_area and len(approx)==4:
                biggest = approx
                max_area = area
    cv.drawContours(image_contour, biggest, -1, (255,0,0),20)
    return biggest

def reorder(my_points):
    my_points = my_points.reshape((4,2))
    my_points_new = np.zeros((4,1,2), np.int32)
    add = my_points.sum(1)

    my_points_new[0] = my_points[np.argmin(add)]
    my_points_new[3] = my_points[np.argmax(add)]
    diff = np.diff(my_points, axis=1)
    my_points_new[1] = my_points[np.argmax(diff)]
    my_points_new[2] = my_points[np.argmax(diff)]

    return my_points_new

def getWarp(image, biggest):
    reorder(biggest)
    pts1 = np.float32(biggest)
    pts2 = np.float32([[0,0], [image_width,0], [0,image_height], [image_width,image_height]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    image_out = cv.warpPerspective(image, matrix, (image_width,image_height))
    
    return image_out

while True:
    _, image = cap.read()
    cv.resize(image, (image_width, image_height))
    image_contour = image.copy()
    image_thres = preProcess(image)
    biggest = getContours(image_thres)
    if biggest.size != 0:
        image_warped = getWarp(image, biggest)
    else:
        another_image = ([image,image_thres],[image, image])
        cv.imshow("Another", another_image)
    cv.imshow("Image", image_warped)
    if cv.waitKey(1) & 0xFF==ord("q"):
        break