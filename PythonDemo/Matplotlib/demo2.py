# -*- coding: utf-8 -*-
"""
figure的使用
"""
import matplotlib.pyplot as plt
import numpy as np
# 
x = np.linspace(-1, 1, 50)


# figure 1
y1 = 2 * x + 1
plt.figure()
plt.plot(x, y1)


# figure 2
y2 = x**2
plt.figure()
plt.plot(x, y2)


# figure 3，指定figure的编号并指定figure的大小, 指定线的颜色, 宽度和类型
#一个坐标轴上画了两个图形
y2 = x**2
plt.figure(num = 5, figsize = (4, 4))
plt.plot(x, y1)
plt.plot(x, y2, color = 'red', linewidth = 1.0, linestyle = '--')
plt.show()