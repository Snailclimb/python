# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:14:42 2018

@author: Administrator
"""

# 打开摄像头并灰度化显示 
import cv2
capture = cv2.VideoCapture(0) 
# OpenCV人脸识别分类器 
classifier = cv2.CascadeClassifier( "D:\openvc\haarcascade_frontalface_default.xml" ) 
color = (0, 255, 0) # 定义绘制颜色 

while(True): 
    # 获取一帧 
    ret, frame = capture.read() 
    # 将这帧转换为灰度图 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # 调用识别人脸 
    faceRects = classifier.detectMultiScale( gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32)) 
    for (x, y, w, h) in faceRects: 
        cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("frame", gray) 
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break

capture.release() 
cv2.destroyAllWindows()