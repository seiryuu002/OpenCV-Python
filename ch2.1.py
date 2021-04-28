# Reading a video
import numpy as np
import cv2 as cv
cap = cv.VideoCapture("resources/Example.mp4")
while True:
    Success, img = cap.read()
    cv.imshow('frame', img)
    if cv.waitKey(15) & 0xFF == ord('x'):
        break
cap.release()
cv.destroyAllWindows()
