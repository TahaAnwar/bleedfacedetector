# Bleed AI Face Detector

A Python package that lets you use 4 different face detectors by just changing a single line of code.

## Usage

First import the library then choose one of the 4 provided methods of face detection and then pass in a 8 bit BGR image (Image read by opencv) and get the face detections

#### Here you can see how to use haar cascade based face detection
```
import bleedefacedetector as fd

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

** import bleedefacedetector as fd **
* fd.haar_detect(img)  #Haar cascade/ viola jones based detection 
* fd.hog_detect(img)   #hog (histogram of oriented gradients) based detection 
* fd.ssd_detect(img)   #SSD + Mobilenet based detection  
* fd._detect(img)   #CNN based detection  *(Only use this in real time when you are running on a GPU)* **
