# Bleed AI Face Detector

A Python package that lets you use 4 different face detectors by just changing a single line of code.

## Usage

First import the library then choose one of the 4 provided methods of face detection and then pass in a 8 bit BGR image (Image read by opencv) and get the face detections

#### Here you can see how to use haar cascade based face detection
```
import bleedefacetector as fd

faces_list = fd.haar_detect(img)

```

The returned faces_list is a list of faces co-ordinates in this format: [x,y,w,h] 
Where x,y is the top left corner of the face and w,h are the width and height of the image respectively.

If 3 faces were detected on the example image then you would get back something like this:

[
[x1,y1,w1,h1]
[x2,y2,w2,h2]
[x3,y3.w3,h3]
]

## Here is the syntax to use all 4 face_detectors

>>  import bleedfacedetector as fd 
> * fd.haar_detect(img)  #Haar cascade/ viola jones based detection 
> * fd.hog_detect(img)   #hog (histogram of oriented gradients) based detection 
> * fd.ssd_detect(img)   #SSD + Mobilenet based detection  
> * fd._detect(img)   #CNN based detection  *(Only use this in real time when you are running on a GPU)* 

NO matter which method you use the returned faces are always in the same format [x,y,w,h]

## Face Detection Example on Image
Here is an example code in which you can detect faces using any of the methods , all you have to do is just change one line


```
import bleedfacedetector as fd
import cv2

img = cv2.imread('family.jpg')

faces = fd.ssd_detect(img)

for (x,y,w,h,) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.putText(img,'Face Detected',(x,y+h+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2, cv2.LINE_AA)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
## Results:
![Results of SSd detection](images/detectedfamily.jpg)


So just change fd.ssd_detect(img) with any other method , note when you use any method other than ssd then consider passing height=0 for better accuracy at the cost of increased time

like this: <br>
```fd.haar_detect(img,height=0)```

* This is because I resize all images to 350 height keeping aspect ratio constant , this is to increase speed but sometimes good detections require a larger height so height = 0 means set height to original. 
* Note you can set custom height by setting height to any number, maybe if you're getting fine results try lowering the height below the defult 350 to get faster speed *
* Note the height parameter is not for SSD based method *

## Result when using hog with height=0
![Results of HOg detection](images/detectedfamilywithhog.jpg)

