import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)

# change color of a area
# img[20:30,60:100] = 255 ,0,0
# change coor of whole img
# img[:] = 255 ,0,0

# draw a line
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,255),2)

# draw a rectangle
cv2.rectangle(img,(350,100),(450,200),(0,255,0))
# cv2.rectangle(img,(350,100),(450,200),(0,255,0),cv2.FILLED)

# draw circle
cv2.circle(img,(150,400),50,(255,0,0))

# type text
cv2.putText(img,"CV Texts",(75,50),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,150,0),1)

cv2.imshow("Img",img)
cv2.waitKey(0)
