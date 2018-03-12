# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:01:13 2018

@author: Administrator
@description： numpy库中的数组排序(sort)函数
"""
import numpy as np
from numpy.matlib import randn
arr = randn(8)   
print("排序前：")
print(arr) 
print("排序后：")  
print(np.sort(arr))   