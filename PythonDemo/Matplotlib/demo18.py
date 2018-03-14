# -*- coding: utf-8 -*-
"""
主次坐标轴 
"""
import numpy as np
import matplotlib.pyplot as plt

# 定义数据
x = np.arange(0, 10, 0.1)
y1 = 0.05 * x ** 2
y2 = -1 * y1

# 定义figure
fig, ax1 = plt.subplots()
# 得到ax1的对称轴ax2
ax2 = ax1.twinx()
# 绘制图像
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')

# 设置label
ax1.set_xlabel('X data')
ax1.set_xlabel('Y1', color = 'g')
ax2.set_xlabel('Y2', color = 'b')

plt.show()
