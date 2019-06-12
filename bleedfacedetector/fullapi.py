import cv2
import dlib
import numpy as np

hog_detctor = dlib.get_frontal_face_detector()
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cnn_detector = dlib.cnn_face_detection_model_v1('mmod_human_face_detector.dat')
net = cv2.dnn.readNetFromCaffe("caffeandproto/deploy.prototxt.txt", "caffeandproto/res10_300x300_ssd_iter_140000.caffemodel")


def haar_detect(img,scaleFactor = 1.3,minNeighbors = 5,height=350):
    scale=1
    # if the height is 0 then original height will be used
    if height:
       scale = height / img.shape[0]
       img = cv2.resize(img, None, fx=scale, fy=scale)

    rscale = 1/scale
    all_faces = face_cascade.detectMultiScale(img, scaleFactor, minNeighbors)
    # resizing all of the coordinates back to original size
    return [[int(var * rscale) for var in face] for face in all_faces]


def hog_detect(img,upsample=0,height=350):
    if  img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    scale=1
    # if the height is 0 then original height will be used
    if height:
       scale = height / img.shape[0]
       img = cv2.resize(img, None, fx=scale, fy=scale)

    rscale = 1/scale
    faces = hog_detctor(img, upsample)
    all_faces=[]
    for face in faces:
        x = face.left()
        y = face.top()
        w = face.right() - x
        h = face.bottom() - y
        all_faces.append([int(x*rscale),int(y*rscale),int(w*rscale),int(h*rscale)])

    return all_faces


def cnn_detect(img,upsample=0,height=350):
    if  img.ndim == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    scale=1
    # if the height is 0 then original height will be used
    if height:
       scale = height / img.shape[0]
       img = cv2.resize(img, None, fx=scale, fy=scale)

    rscale = 1/scale
    faces = cnn_detector(img, upsample)
    all_faces=[]
    for face in faces:
        x = face.rect.left()
        y = face.rect.top()
        w = face.rect.right() - x
        h = face.rect.bottom() - y
        all_faces.append([int(x*rscale),int(y*rscale),int(w*rscale),int(h*rscale)])
    return all_faces



def ssd_detect(image,conf=0.5,returnconf=False):
    (h, w) = image.shape[:2]
    resizedimage = cv2.resize(image, (300, 300))
    blob = cv2.dnn.blobFromImage(resizedimage, 1.0,(300, 300), (104.0, 177.0, 123.0))
    all_faces=[]
    # pass the blob through the network and obtain the detections
    net.setInput(blob)
    detections = net.forward()

    for i in range(0, detections.shape[2]):
        #extract the confidence associated with the prediction
        confidence = detections[0, 0, i, 2]

        #if confidence is less than predefined threshold conf then ignore those predictions
        if confidence < conf:
            continue

        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        (startX, startY, endX, endY) = box.astype("int")

        #if return conf is false then just return the boxes otherwise also return confience
        if not returnconf:
           all_faces.append([startX,startY,endX-startX, endY-startY])
        else:
           all_faces.append([startX,startY,endX-startX, endY-startY,confidence])


    return all_faces
