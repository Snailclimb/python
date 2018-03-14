# -*- coding: utf-8 -*-
"""
简单图形绘制

"""

import matplotlib.pyplot as plt
import numpy as np

#从-1-----1之间等间隔采66个数.也就是说所画出来的图形是66个点连接得来的
#注意：如果点数过小的话会导致画出来二次函数图像不平滑
x = np.linspace(-1, 1,66)
# 绘制y=2x+1函数的图像
y = 2 * x + 1
plt.plot(x, y)
plt.show()

# 绘制x^2函数的图像
y = x**2
plt.plot(x, y)
plt.show()