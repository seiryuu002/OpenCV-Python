# try to create a paint application
import cv2 as cv
import numpy as np

drawing = False
r, g, b, size = 0, 0, 0, 0


def a(self):
    pass


img = np.zeros((300, 512, 3), np.uint8)
img[:] = [255, 255, 255]
img2 = np.zeros((300, 512, 3), np.uint8)
cv.namedWindow('image')
# Trackbars for R, G ,B
cv.createTrackbar('R', 'image', 0, 255, a)
cv.createTrackbar('G', 'image', 0, 255, a)
cv.createTrackbar('B', 'image', 0, 255, a)
# Trackbars for Size of brush
cv.createTrackbar('size', 'image', 2, 50, a)


def track_pos():
    global r, g, b, size
    r = cv.getTrackbarPos('R', 'image')
    g = cv.getTrackbarPos('G', 'image')
    b = cv.getTrackbarPos('B', 'image')
    size = cv.getTrackbarPos('size', 'image')


def draw(event, x, y, flags, param):
    global drawing
    print(x)
    print(y)
    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            cv.circle(img, (x, y), size, (b, g, r), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        cv.circle(img, (x, y), size, (b, g, r), -1)

cv.setMouseCallback('image', draw)
while True:
    fin = np.hstack((img,img2))
    cv.imshow('image', fin)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break
    # Get current positions of trackbars
    track_pos()
cv.destroyAllWindows()
