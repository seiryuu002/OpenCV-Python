import cv2
import numpy as np

frame_width = 640
frame_height = 480
cap = cv2.VideoCapture(0)
cap.set(3, frame_width)
cap.set(4, frame_height)
cap.set(10, 150)

my_colors = [[107, 100, 110, 125, 200, 185], [0, 120, 140, 10, 170, 240]]
my_colors_value = [[204, 0, 0], [51, 51, 255]]
my_points = []


def draw(my_points, my_colors_value):
    for point in my_points:
        cv2.circle(img_result, (point[0], point[1]), 10, my_colors_value[point[2]], cv2.FILLED)


def get_contours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1:
            # cv2.drawContours(img_result, cnt, -1, (0, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


def find_color(img, my_colors, my_colors_value):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    new_points = []
    for color in my_colors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(img_hsv, lower, upper)
        a, b = get_contours(mask)
        cv2.circle(img_result, (a, b), 10, my_colors_value[count], cv2.FILLED)
        if a != 0 and b != 0:
            new_points.append([a, b, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return new_points


while True:
    success, img = cap.read()
    img_result = img.copy()
    new_points = find_color(img, my_colors, my_colors_value)
    if len(new_points) != 0:
        for newp in new_points:
            my_points.append(newp)
    if len(new_points) != 0:
        draw(my_points, my_colors_value)
    cv2.imshow("Video", img_result)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break
