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
arr3d[0] = old_values   
print(arr3d) # 输出 [[[1 2 3] [4 5 6]] [[3 3 3] [3 3 3]] ]

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print("输出names数组：")  
print(names)
print("输出randn(7, 4)生成的7行4列的随机数函数")
data = randn(7, 4)
print(data)
print("判断names数组中的每一个元素是否等于Bob:")
print(names == 'Bob') #, 输出 [True False False True FalseFalse False]  
print("data[names == 'Bob']输出data中判断为true的行元素:")
print(data[names == 'Bob'])
print("data[names == 'Bob', 2:]输出data中判断为true所在的行，及第3列第4列的所有元素:")  
print(data[names == 'Bob', 2:],) #输出data中判断为true所在的行，及第3列第4列的所有元素；
print("data[names == 'Bob', 3]输出data中判断为true所在的行及第4列的元素 :")  
print(data[names == 'Bob', 3]) 
print("输出名字为Bob以及Will所在的行元素 :")
print(data[((names == 'Bob') | (names == 'Will'))]) #输出名字为Bob以及Will所在的行元素  
  