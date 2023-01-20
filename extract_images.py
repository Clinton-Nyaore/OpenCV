import os
import cv2 as cv

cap = cv.VideoCapture(r"E:\\MyNotesCertsProjects\\Projects\\OpenCV\\videos\\ObjectTracking\\vunatec_mangoes.3gp")

current_frame = 0

if not os.path.exists("data"):
    os.makedirs("data")

while True:
    success, frame = cap.read()

    cv.imshow("Output", frame)
    cv.imwrite("./data/image0"+str(current_frame)+".jpg", frame)

    current_frame += 1

    if cv.waitKey(30) & 0xFF==ord("s"):
        break

cap.release()
cv.destroyAllWindows()