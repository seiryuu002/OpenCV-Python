import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)

# print(img)
# img[:] = 200, 180, 255
center_red = (256, 128)
center_green = (171, 275)
center_blue = (338, 275)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
fill = -1
# cv2.line(img, (0, 0), (512, 512), (197, 183, 255), 3)
# cv2.line(img, (0, 512), (512, 0), (197, 183, 255), 3)
# cv2.circle(img, (256, 256), 128, (0, 255, 0), 3)
# cv2.putText(img, "OP", (235, 268), cv2.FONT_ITALIC, 1, (0, 255, 255), 3)

cv2.rectangle(img, (0, 0), (512, 512), black, fill)

cv2.circle(img, center_red, 70, red, fill)
cv2.circle(img, center_red, 30, black, fill)
cv2.circle(img, center_green, 70, green, fill)
cv2.circle(img, center_green, 30, black, fill)
cv2.circle(img, center_blue, 70, blue, fill)
cv2.circle(img, center_blue, 30, black, fill)

cv2.ellipse(img, center_red, (70, 70), 60, 0, 60, black, fill)
cv2.ellipse(img, center_blue, (70, 70), 240, 0, 60, black, fill)
cv2.ellipse(img, center_green, (70, 70), 300, 0, 60, black, fill)

cv2.putText(img, "OpenCV", (90, 430), cv2.FONT_ITALIC, 3, white, 8, cv2.LINE_AA)

cv2.imshow("window", img)
cv2.waitKey(0)
