# -*- coding: utf-8 -*-
"""
Created on Wed May 23 22:38:40 2018

@author: Administrator
"""
#录制视频
#https://www.jianshu.com/p/2b79012c0228
import cv2
capture = cv2.VideoCapture(0) 
# 定义编码方式并创建VideoWriter对象 
fourcc = cv2.VideoWriter_fourcc(*'MJPG') 
outfile = cv2.VideoWriter("D:\\you-get_download\\output.avi", fourcc, 25., (640, 480)) 
while(capture.isOpened()): 
    ret, frame = capture.read() 
    if ret: 
        outfile.write(frame) # 写入文件 
        cv2.imshow('frame', frame) 
        if cv2.waitKey(1) == ord('q'): 
            break 
    else: break
