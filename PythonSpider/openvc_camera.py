# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:11:09 2018

@author: Administrator
"""

# 打开摄像头并灰度化显示 
import cv2
capture = cv2.VideoCapture(0) 
while(True): 
    # 获取一帧 
    ret, frame = capture.read() 
    # 将这帧转换为灰度图 
   # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   #第一个参数是窗口名称，第二个参数从摄像头读取到的内容
    cv2.imshow('frame', frame) 
    if cv2.waitKey(1) == ord('q'): 
        break
capture.release() 
cv2.destroyAllWindows()
