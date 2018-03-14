# -*- coding: utf-8 -*-
"""
figure绘制多图 
"""
import matplotlib.pyplot as plt

# 定义figure
plt.figure()
# figure分成3行3列, 取得第一个子图的句柄, 第一个子图跨度为1行3列, 起点是表格(0, 0)
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan = 3, rowspan = 1)
ax1.plot([0, 1], [0, 1])
ax1.set_title('Test')

# figure分成3行3列, 取得第二个子图的句柄, 第二个子图跨度为1行3列, 起点是表格(1, 0)
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan = 2, rowspan = 1)
ax2.plot([0, 1], [0, 1])

# figure分成3行3列, 取得第三个子图的句柄, 第三个子图跨度为1行1列, 起点是表格(1, 2)
ax3 = plt.subplot2grid((3, 3), (1, 2), colspan = 1, rowspan = 1)
ax3.plot([0, 1], [0, 1])

# figure分成3行3列, 取得第四个子图的句柄, 第四个子图跨度为1行3列, 起点是表格(2, 0)
ax4 = plt.subplot2grid((3, 3), (2, 0), colspan = 3, rowspan = 1)
ax4.plot([0, 1], [0, 1])

plt.show()
