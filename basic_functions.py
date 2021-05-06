import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8)
print(kernal)

frameWidth = 640
frameHeight = 360

path = "Resources/(1).jpg"
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2XYZ)
imgCanny =  cv2.Canny(imgGray,100,100)
imgDialate = cv2.dilate(imgCanny,kernal,iterations=1)
imgErode = cv2.erode(imgDialate,kernal,iterations=1)

img = cv2.resize(img, (frameWidth, frameHeight))
imgGray = cv2.resize(imgGray, (frameWidth, frameHeight))
imgCanny = cv2.resize(imgCanny, (frameWidth, frameHeight))
imgDialate = cv2.resize(imgDialate, (frameWidth, frameHeight))
imgErode = cv2.resize(imgErode, (frameWidth, frameHeight))

cv2.imshow("original",img)
cv2.imshow("grayscale",imgGray)
cv2.imshow("canny",imgCanny)
cv2.imshow("Dialated",imgDialate)
cv2.imshow("Erode",imgErode)

cv2.waitKey(0)
