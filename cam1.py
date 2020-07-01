import cv2
video_capture = cv2.VideoCapture(0)   #0 default camera , can get output in any video feed

face_clsfr = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
while(True):
     ret, frame = video_capture.read()    #"ret" is the boolian value weather it can read camera or not

     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) # color convertion 
     faces = face_clsfr.detectMultiScale(gray)   #detect faces using pre trained harcascade and convert to grayscale
     
     for(x, y, w, h) in faces:
          cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
     #results=clsfr.predic(test_data)

     #cam1.imshow("LIVE",gray)   #to show gray scale frame

          cv2.imshow("LIVE",frame)  # get the video from camera 
          cv2.waitKey(1)          # delay 1 min

video_capture.release()
cv2.destroyAllWindows()
