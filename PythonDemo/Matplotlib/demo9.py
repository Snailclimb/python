# -*- coding: utf-8 -*-
"""
绘制柱状图
"""

import matplotlib.pyplot as plt
import numpy as np

# 数据数目
n = 10
x = np.arange(n)
# 生成数据, 均匀分布(0.5, 1.0)之间
y1 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)
y2 = (1 - x / float(n)) * np.random.uniform(0.5, 1.0, n)

# 绘制柱状图, 向上
plt.bar(x, y1, facecolor = 'blue', edgecolor = 'white')
# 绘制柱状图, 向下
plt.bar(x, -y2, facecolor = 'green', edgecolor = 'white')


temp = zip(x, y2)
# 在柱状图上显示具体数值, ha水平对齐, va垂直对齐
for x, y in zip(x, y1):
    plt.text(x + 0.05, y + 0.1, '%.2f' % y, ha = 'center', va = 'bottom')

for x, y in temp:
    plt.text(x + 0.05, -y - 0.1, '%.2f' % y, ha = 'center', va = 'bottom')

# 设置坐标轴范围
plt.xlim(-1, n)
plt.ylim(-1.5, 1.5)
# 去除坐标轴
plt.xticks(())
plt.yticks(())
plt.show()