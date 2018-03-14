# -*- coding: utf-8 -*-
"""
figure图的嵌套
"""

import matplotlib.pyplot as plt

# 定义figure
fig = plt.figure()

# 定义数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]

# figure的百分比, 从figure 10%的位置开始绘制, 宽高是figure的80%
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# 获得绘制的句柄
ax1 = fig.add_axes([left, bottom, width, height])
# 绘制点(x,y)
ax1.plot(x, y, 'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('test')


# 嵌套方法一
# figure的百分比, 从figure 10%的位置开始绘制, 宽高是figure的80%
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
# 获得绘制的句柄
ax2 = fig.add_axes([left, bottom, width, height])
# 绘制点(x,y)
ax2.plot(x, y, 'r')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('part1')


# 嵌套方法二
plt.axes([bottom, left, width, height])
plt.plot(x, y, 'r')
plt.xlabel('x')
plt.ylabel('y')
plt.title('part2')

plt.show()