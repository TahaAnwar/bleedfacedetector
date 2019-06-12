import bleedfacedetector as fd
import cv2

img = cv2.imread('images/family.jpg')
#img = cv2.imread('images/imrankhanface.jpg')

faces = fd.ssd_detect(img)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(img,'Face Detected',(x,y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
