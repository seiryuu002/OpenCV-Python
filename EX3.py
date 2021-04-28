import numpy as np
import cv2
import math

img = np.zeros((512, 512, 3), np.uint8)
cv2.putText(img, "OpenCV", (90, 450), cv2.FONT_ITALIC, 3, (255, 255, 255), 3, cv2.LINE_AA)

r1 = 70
r2 = 30

ang = 60

d = 170
h = int(d/2*math.sqrt(3))
print(h)
dot_red = (256,128)
dot_green = (round(dot_red[0]-d/2), round(dot_red[1]+h))
dot_blue = (round(dot_red[0]+d/2), round(dot_red[1]+h))

# tan = float(dot_red[0]-dot_green[0])/(dot_green[1]-dot_red[0])
# ang = math.atan(tan)/math.pi*180

red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)

full = -1

cv2.circle(img, dot_red, r1, red, full)
cv2.circle(img, dot_green, r1, green, full)
cv2.circle(img, dot_blue, r1, blue, full)
cv2.circle(img, dot_red, r2, black, full)
cv2.circle(img, dot_green, r2, black, full)
cv2.circle(img, dot_blue, r2, black, full)

cv2.ellipse(img, dot_red, (r1, r1), ang, 0, ang, black, full)
cv2.ellipse(img, dot_green, (r1, r1), 360-ang, 0, ang, black, full)
cv2.ellipse(img, dot_blue, (r1, r1), 360-2*ang, ang, 0, black, full)

cv2.imwrite("opencv_logo.png", img)