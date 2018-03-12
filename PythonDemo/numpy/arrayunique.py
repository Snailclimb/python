# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 16:02:47 2018

@author: Administrator
@description： numpy库unique函数保证数组中的元素唯一（剔除重复元素）
"""

import numpy as np
names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])   
print(np.unique(names))   
ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4,5])   
print(np.unique(ints)) 