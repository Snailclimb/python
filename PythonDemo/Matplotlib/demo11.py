# -*- coding: utf-8 -*-
"""
绘制Image 
"""
import matplotlib.pyplot as plt
import numpy as np

# 定义图像数据
a = np.linspace(0, 1, 9).reshape(3, 3)
# 显示图像数据
plt.imshow(a, interpolation = 'nearest', cmap = 'bone', origin = 'lower')
# 添加颜色条
plt.colorbar()
# 去掉坐标轴
plt.xticks(())
plt.yticks(())
plt.show()
