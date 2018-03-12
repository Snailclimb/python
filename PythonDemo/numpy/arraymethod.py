# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:51:47 2018

@author: Administrator
@description： numpy库操纵数组的一些方法
"""
import numpy as np

from numpy.matlib import randn
#定义数组类型
arr3 = np.array([1, 2, 3], dtype=np.float64)   
arr4 = np.array([1, 2, 3], dtype=np.int32)   
print(arr3.dtype)#float64
print(arr4.dtype)#int32 
#转换数组类型
arr5 = np.array([1, 2, 3, 4, 5])   
print(arr5.dtype) #int32  
arr6 = arr5.astype(np.float64) #将数组5的数据类型转换为float64  
print(arr6.dtype) #float64 
#数组间以及数组与数之间的运算 
arr = np.array([[1., 2., 3.], [4., 5., 6.]])   
print(arr * arr) #相应元素相乘，输出为[[1. 4. 9.] [16. 25. 36.]]  
print(arr - arr) #相应元素相减，输出为[[0. 0. 0.] [0. 0. 0.]] 
#创建二维数组，取值，修改值
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    
print(arr2d[2]) #数组标号从0开始，输出第三行元素：[7 8 9]  
#创建三维数组  
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]) #2个二维数组  
old_values = arr3d[0].copy() #将第1个二维数组拷贝至old_values   
print(old_values) #输出：[[1 2 3], [4 5 6]]
arr3d[0] = 3 #将第1个二维数组的元素都修改为3  
arr3d[1] = 3 #将第2个二维数组的元素都修改为3
print(arr3d) #输出全为3的三维数组 
  