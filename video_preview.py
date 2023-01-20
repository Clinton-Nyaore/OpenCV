import cv2 as cv
import numpy as np


cap = cv.VideoCapture(r"E:\\MyNotesCertsProjects\\Projects\\OpenCV\\videos\\ObjectTracking\\vunatec_mangoes.3gp")

if (cap.isOpened() == False): 
    print("Error reading video file")
  
# We need to set resolutions.
# so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
   
size = (frame_width, frame_height)
   
# Below VideoWriter object will create
# a frame of above defined The output 
# is stored in 'filename.avi' file.
result = cv.VideoWriter('filename.avi', cv.VideoWriter_fourcc(*'MJPG'), 10, (400, 580), True)

while True:
    _, video = cap.read()
    video = cv.resize(video, (400, 580))

    result.write(video)

    cv.imshow("Video", video)

    if cv.waitKey(30) & 0xFF==ord("s"):
        break

cap.release()
cv.destroyAllWindows()