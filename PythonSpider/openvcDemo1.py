# -*- coding: utf-8 -*-
"""
Created on Tue May 22 16:03:30 2018

@author: Administrator
"""

#导入cv模块
import cv2 as cv
#读取图像，支持 bmp、jpg、png、tiff 等常用格式
img = cv.imread("D:\\picture\\VCG41475980712.jpg")
#输出OpenCV的版本号
print(cv.__version__)
#创建窗口并显示图像
cv.namedWindow("Image")
cv.imshow("Image",img)
cv.waitKey(0)
#释放窗口
cv.destroyAllWindows()
    