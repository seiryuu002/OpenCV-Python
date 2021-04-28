# Tutorial no.2
# Getting input from camera
# First we import required modules

import cv2 as cv

frame_width = 400
frame_height = 300
cap = cv.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Our operations on the frame come here
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv.imshow('frame', gray)
    if cv.waitKey(1) == ord('x'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
