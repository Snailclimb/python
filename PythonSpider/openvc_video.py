# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:29:59 2018

@author: Administrator
"""

import cv2
# 播放本地视频 
capture = cv2.VideoCapture("D:\\you-get_download\\muzi.flv") 
while(capture.isOpened()):
    ret, frame = capture.read() 
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow("frame", frame) #彩色画面播放
    #cv2.imshow("frame", gray) #黑白画面播放
    if cv2.waitKey(30) == ord('q'): 
        break


