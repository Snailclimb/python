# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 14:13:32 2018

@author: Snailclimb
@description： numpy库创建数组的一些方法
"""
import numpy as np

print("创建一维数组：")
data1 = [3, 3.3, 9, 5, 6]
arr1 = np.array(data1)
print(arr1)

print("创建二维数组:")
data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]   
arr2 = np.array(data2)   
print(arr2)   
 # Type of data in array.   
print("输出第一个数组的数据类型:",arr1.dtype)   
print("输出第二个数组的维数:",arr2.ndim)  
print("输出第三个数组的形状:",arr2.shape)  
#用zeros函数创建数组  
print("np.zeros(10)创建10个元素都是0的一维数组： ")
print(np.zeros(10))
print("np.zeros((3, 6))创建3行6列都是0的二维数组：")
print(np.zeros((3, 6)))
#用Empty函数创建数组，其初始值为乱值  
print("np.empty((3,6))创建3行6列都是0的二维数组：")
print(np.empty((3,6))) 
#用arrange函数创建数组  
print("np.arange(9)创建一维数组：")
print(np.arange(9))