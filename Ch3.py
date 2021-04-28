import cv2

img = cv2.imread("resources/phoenix.png")
print(img.shape)
imgResize = cv2.resize(img, (300, 300))
cv2.imshow("image", img)
cv2.imshow("resized", imgResize)
cv2.waitKey(0)
