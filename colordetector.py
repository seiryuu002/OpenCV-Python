# Required modules
import cv2
# Required modules
import cv2
import numpy as np

min_YCrCb = np.array([0, 133, 77], np.uint8)
max_YCrCb = np.array([235, 173, 127], np.uint8)

# Get pointer to video frames from primary device
image = cv2.imread("resources/Check.jpg")
imageYCrCb = cv2.cvtColor(image, cv2.COLOR_BGR2YCR_CB)
skinRegionYCrCb = cv2.inRange(imageYCrCb, min_YCrCb, max_YCrCb)

skinYCrCb = cv2.bitwise_and(image, image, mask=skinRegionYCrCb)

cv2.imwrite("resources/result.jpg", np.hstack([image, skinYCrCb]))


