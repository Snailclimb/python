# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 15:37:14 2018

@author: Administrator
"""
import numpy as np
from numpy.matlib import randn
arr = np.empty((8, 4)) #二维数组  
#range(8)即 [0, 1, 2, 3, 4, 5, 6, 7]  
for i in range(8):   
   arr[i] = i #第i行的数字都为i;  
  
print(arr)
print(arr[[4, 3, 0, 6]]) #[[ 4.  4. 4.  4.] [ 3.  3. 3.  3.] [ 0.  0. 0.  0.] [ 6.  6. 6.  6.]]  
arr = np.arange(32).reshape((8, 4))
print("np.arange(32).reshape((8, 4)):")
print(arr)
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])#[ 4 23 29 10]
print(" 输出矩阵转置:  ")
arr = np.arange(15).reshape((3, 5))   
print(arr.T)
print("输出np.arange(10)：")   
arr = np.arange(10)
print(arr) 
print("输出np.sqrt(arr)：")     
print(np.sqrt(arr)) #仍是一维数组，求数组中的每个元素求平方根 
print("输出np.exp(arr))：")    
print(np.exp(arr)) #仍是一维数组，求以e为底，数组中的每个元素作为指数的值
print("randn(8):")
x = randn(8) #生成8个随机数
print(x)   
print("randn(8):")  
y = randn(8)   
print(y)   
print(np.maximum(x, y)) #仍是一维数组，每个元素为数组x和y对应元素最大的那个；
print("-------------------------------------")  
xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])   
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])   
cond = np.array([True, False, True, True, False])
result = np.where(cond, xarr, yarr)   
print(result)#输出：[1.1 2.2 1.3 1.4 2.5]
print("-------------------------------------") 
arr = randn(4, 4)
print(arr)   
print(np.where(arr > 0, 2, -2))
print("-------------------------------------")  
arr = np.random.randn(5, 4) # normally-distributed data   
print(arr)   
print(arr.mean())   
print(np.mean(arr))   
print(arr.sum())   
print(arr.mean(axis=1))      
  