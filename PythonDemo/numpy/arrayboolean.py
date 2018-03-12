# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:07:17 2018

@author: Administrator
@description： any和all函数
"""
import numpy as np
from numpy.matlib import randn
print('Boolean values are coerced to 1 (True) and 0 (False) in the above methods. Thus, sum is often used as a means of counting True values in a boolean array:')   
arr = randn(100)
print("输出生成的随机数数组中数值大于0的个数：")   
print((arr > 0).sum())   
bools = np.array([False, False, True, False])
print(bools) 
print("只要有一个为true就输出true:")  
print(bools.any())  # true
print("全部才输出true：") 
print(bools.all())  #false
bools2 = np.array([ True,  True, True,  True])
print(bools2.all())  #true

#两个数组之间
# any():a数组与b数组有一个元素对应相等就输出true
#all():a数组与b数组每个元素都对应相等才输出true
a=np.array([1,2,3])
b=np.array([2,2,3])
boolean=(a==b).all()
boolean2=(a==b).any()
print(boolean)#true
print(boolean2)#true