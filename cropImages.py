import cv2

path = "Resources/(1).jpg"
img = cv2.imread(path)

width , height = 400 , 400
imgResize = cv2.resize(img,(width,height))
imgCrop = img[300:540,0:900]

cv2.imshow("Resized",imgResize)
cv2.imshow("original",img)
cv2.imshow("Croped",imgCrop)
cv2.waitKey(0)
