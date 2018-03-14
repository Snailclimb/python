#!/usr/bin/env python
"""
Image-colored wordcloud
=======================
您可以在ImageColorGenerator中实现使用基于图像的着色策略对文字云进行着色，它使用由源图像中的单词占用的区域的平均颜色。

"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

d = path.dirname(__file__)

# 读取整个文本
text = open(path.join(d, 'alice.txt')).read()

# 读取蒙板/彩色图像（图片是从http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010下载的）
alice_coloring = np.array(Image.open(path.join(d, "alice_color.png")))
stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
               stopwords=stopwords, max_font_size=40, random_state=42)
# 生成词云
wc.generate(text)

# 从图像创建着色
image_colors = ImageColorGenerator(alice_coloring)

# 显示
plt.imshow(wc, interpolation="bilinear")
plt.axis("off") #不显示坐标尺寸
plt.figure()
# 重新着色词云并显示
# 我们也可以直接在构造函数中给使用：color_func=image_colors 
plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off") #不显示坐标尺寸
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
plt.axis("off") #不显示坐标尺寸
plt.show()#一次绘制三张图
