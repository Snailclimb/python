# -*- coding: utf-8 -*-
"""
动画
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


# 定义figure
fig, ax = plt.subplots()

# 定义数据
x = np.arange(0, 2 * np.pi, 0.01)
# line, 表示只取返回值中的第一个元素
line, = ax.plot(x, np.sin(x))

# 定义动画的更新
def update(i):
    line.set_ydata(np.sin(x + i/10))
    return line,

# 定义动画的初始值
def init():
    line.set_ydata(np.sin(x))
    return line,

# 创建动画
ani = animation.FuncAnimation(fig = fig, func = update, init_func = init, interval = 10, blit = False, frames = 200)

# 展示动画
plt.show()

# 动画保存
ani.save('sin.html', writer = 'imagemagick', fps = 30, dpi = 100)