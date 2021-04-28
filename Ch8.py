import cv2


def get_contours(img2):
    contours, hierarchy = cv2.findContours(img2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area > 1:
            cv2.drawContours(imgContour, cnt, -1, (0, 0, 0), 2)
            peri = cv2.arcLength(cnt, True)
            # print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            print(len(approx))
            object_corners = len(approx)
            x, y, w, h = cv2.boundingRect(approx)
            if object_corners == 3:
                object_type = "tri"
            elif object_corners == 4:
                aspect_ratio = w/float(h)
                if 0.95 < aspect_ratio < 1.05:
                    object_type = "square"
                else:
                    object_type = "rectangle"
            elif object_corners == 5:
                object_type = "pentagon"
            elif object_corners == 6:
                object_type = "hexagon"
            elif object_corners == 8:
                object_type = "star"
            elif object_corners == 12:
                object_type = "dstar"
            else:
                object_type = "circle"
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(imgContour, object_type, ((x+(w//2)-10), (y+(h//2)-10)),
                        cv2.FONT_HERSHEY_COMPLEX, 0.3, (0, 0, 0), 1)


path = 'resources/shape.png'
img = cv2.imread(path)
imgContour = img.copy()
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
imgCanny = cv2.Canny(imgBlur, 50, 50)
get_contours(imgCanny)
# cv2.imshow("Output", img)
# cv2.imshow("OutputCanny", imgCanny)
cv2.imshow("OutputContour", imgContour)
cv2.waitKey(0)
