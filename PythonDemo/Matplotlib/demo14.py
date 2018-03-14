# -*- coding: utf-8 -*-
"""
subplot绘制多图 
"""

import matplotlib.pyplot as plt

plt.figure()

# 绘制第一个图
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
# 绘制第二个图
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])
# 绘制第三个图
plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])
# 绘制第四个图
plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 1])
plt.show()