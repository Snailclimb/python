# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 17:11:15 2018
设置坐标轴label上数字的样式
"""

import matplotlib.pyplot as plt
import numpy as np

# 绘制普通图像
x = np.linspace(-3, 3, 50)
y = 2 * x + 1

plt.figure()
plt.plot(x, y)

# 将上、右边框去掉
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置x轴的位置及数据在坐标轴上的位置
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 设置y轴的位置及数据在坐标轴上的位置
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 设置坐标轴label的大小，背景色等信息
for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor = 'green', edgecolor = 'None', alpha = 0.7))

plt.show()