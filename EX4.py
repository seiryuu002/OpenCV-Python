# wap to draw unfilled rectangle by dragging mouse
# Exercise based on tutorial 4
import cv2 as cv
import numpy as np
drawing = False # true when we start drawing
ix, iy = -1, -1

img = np.zeros((512, 512, 3), np.uint8)


def draw(event, x, y, flags, param):
    global ix, iy, drawing
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.rectangle(img, (0, 0), (512, 512), (0, 0, 0), -1)
            cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            cv.rectangle(img, (ix + 10, iy + 10), (x - 10, y - 10), (0, 0, 0), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        cv.rectangle(img, (ix + 10, iy + 10), (x - 10, y - 10), (0, 0, 0), -1)


cv.namedWindow('image')
cv.setMouseCallback('image', draw)

while 1:
    cv.imshow('image', img)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break
cv.destroyAllWindows()
