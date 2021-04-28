import cv2
import numpy as np
img = cv2.imread("resources/gal.jpeg")
width = 200
height = 200
pts1 = np.float32([[200, 150], [400, 150], [200, 350], [400, 350]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
ImgOutPut = cv2.warpPerspective(img, matrix, (width, height))
cv2.imshow("img", img)
cv2.imshow("output", ImgOutPut)
cv2.waitKey(0)
