import cv2
import numpy as np

frame_width = 400
frame_height = 300
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)


def empty(a):
    pass


def stack_images(scale, img_array):
    rows = len(img_array)
    cols = len(img_array[0])
    rows_available = isinstance(img_array[0], list)
    width = img_array[0][0].shape[1]
    height = img_array[0][0].shape[0]
    if rows_available:
        for x in range(0, rows):
            for y in range(0, cols):
                if img_array[x][y].shape[:2] == img_array[0][0].shape[:2]:
                    img_array[x][y] = cv2.resize(img_array[x][y], (0, 0), None, scale, scale)
                else:
                    img_array[x][y] = cv2.resize(img_array[x][y], (img_array[0][0].shape[1], img_array[0][0].shape[0]), None, scale, scale)
                if len(img_array[x][y].shape) == 2:
                    img_array[x][y] = cv2.cvtColor(img_array[x][y], cv2.COLOR_GRAY2BGR)
        image_blank = np.zeros((height, width, 3), np.uint8)
        hor = [image_blank]*rows
        hor_con = [image_blank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(img_array[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if img_array[x].shape[:2] == img_array[0].shape[:2]:
                img_array[x] = cv2.resize(img_array[x], (0, 0), None, scale, scale)
            else:
                img_array[x] = cv2.resize(img_array[x], (img_array[0].shape[1], img_array[0].shape[0]), None, scale, scale)
            if len(img_array[x].shape) == 2:
                img_array[x] = cv2.cvtColor(img_array[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(img_array)
        ver = hor
    return ver


cv2.namedWindow("YCR_CB")
cv2.resizeWindow("YCR_CB", 300, 300)
cv2.createTrackbar("Y min", "YCR_CB", 0, 255, empty)
cv2.createTrackbar("Y max", "YCR_CB", 255, 255, empty)
cv2.createTrackbar("Cr min", "YCR_CB", 0, 255, empty)
cv2.createTrackbar("Cr max", "YCR_CB", 255, 255, empty)
cv2.createTrackbar("Cb min", "YCR_CB", 0, 255, empty)
cv2.createTrackbar("Cb max", "YCR_CB", 255, 255, empty)

while True:
    success, img = cap.read()
    imgYCR = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
    Y_min = cv2.getTrackbarPos("Y min", "YCR_CB")
    Y_max = cv2.getTrackbarPos("Y max", "YCR_CB")
    Cr_min = cv2.getTrackbarPos("Cr min", "YCR_CB")
    Cr_max = cv2.getTrackbarPos("Cr max", "YCR_CB")
    Cb_min = cv2.getTrackbarPos("Cb min", "YCR_CB")
    Cb_max = cv2.getTrackbarPos("Cb max", "YCR_CB")
    print(Y_min, Y_max, Cr_min, Cr_max, Cb_min, Cb_max)

    lower = np.array([Y_min, Cr_min, Cb_min])
    upper = np.array([Y_max, Cr_max, Cb_max])
    mask = cv2.inRange(imgYCR, lower, upper)
    imgResult = cv2.bitwise_and(img, img, mask=mask)

    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    stacked = stack_images(0.8, ([img, imgYCR], [mask, imgResult]))
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("MASK", mask)
    # cv2.imshow("Result", imgResult)
    cv2.imshow("Output", stacked)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
