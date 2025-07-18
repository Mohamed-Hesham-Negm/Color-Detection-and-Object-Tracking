import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture("F:/AI/CV/balls.mp4")
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10, 150)

myColors = [
    [22, 93, 0, 45, 255, 255],
    [100, 150, 0, 140, 255, 255]
]

myColorValues = [
    [0, 255, 255],
    [255, 0, 0]
]


myPoints = []

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for count, color in enumerate(myColors):
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
            cv2.circle(imgResult, (x, y), 10, myColorValues[count], cv2.FILLED)
    return newPoints

def getContours(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x + w // 2, y

def drawOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    if not success:
        break
    img = cv2.resize(img, (frameWidth, frameHeight))
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if newPoints:
        myPoints.extend(newPoints)
    if myPoints:
        drawOnCanvas(myPoints, myColorValues)
    cv2.imshow("Result", imgResult)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
