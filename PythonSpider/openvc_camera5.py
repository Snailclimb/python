# -*- coding: utf-8 -*-
"""
Created on Wed May 23 12:28:46 2018

@author: Administrator
"""

import cv2


recognizer = cv2.face.LBPHFaceRecognizer_create()
# recognizer = cv2.createLBPHFaceRecognizer() # in OpenCV 2
recognizer.read("trainner.yml")
# recognizer.load('trainner/trainner.yml') # in OpenCV 2

cascade_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)
cam = cv2.VideoCapture(0)
# font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1) # in OpenCV 2
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, im = cam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x - 50, y - 50), (x + w + 50, y + h + 50), (225, 0, 0), 2)
        img_id, conf = recognizer.predict(gray[y:y + h, x:x + w])
        if conf > 50:
            if img_id == 1:
                img_id = 'jianyujianyu'
            elif img_id == 2:
                img_id = 'ghost'
        else:
            img_id = "Unknown"
        # cv2.cv.PutText(cv2.cv.fromarray(im), str(Id), (x, y + h), font, 255)
        cv2.putText(im, str(img_id), (x, y + h), font, 0.55, (0, 255, 0), 1)
    cv2.imshow('im', im)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()