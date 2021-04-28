import cv2

face_cascade = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
img = cv2.imread("resources/lisa.jpg")
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, width, height) in faces:
    cv2.rectangle(img, (x, y), (x+width, y+height), (0, 255, 0), 2)

cv2.imshow("OUTPUT", img)
cv2.waitKey(0)
