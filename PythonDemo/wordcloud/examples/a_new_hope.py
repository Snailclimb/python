#!/usr/bin/env python
"""
Using custom colors
===================

使用重新着色方法和自定义着色功能。
"""

import numpy as np
from PIL import Image
from os import path
import matplotlib.pyplot as plt
import random

from wordcloud import WordCloud, STOPWORDS


def grey_color_func(word, font_size, position, orientation, random_state=None,
                    **kwargs):
    return "hsl(0, 0%%, %d%%)" % random.randint(60, 100)

d = path.dirname(__file__)

# 读取图片（图片来源：http://www.stencilry.org/stencils/movies/star%20wars/storm-trooper.gif）
mask = np.array(Image.open(path.join(d, "stormtrooper_mask.png")))

# 文字来源：“新希望”电影剧本（网址：http://www.imsdb.com/scripts/Star-Wars-A-New-Hope.html）
text = open(path.join(d, 'a_new_hope.txt')).read()

# 预处理一点点文本
text = text.replace("HAN", "Han")
text = text.replace("LUKE'S", "Luke")

# 添加电影剧本特定的停用词
stopwords = set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc = WordCloud(max_words=1000, mask=mask, stopwords=stopwords, margin=10,
               random_state=1).generate(text)
# 存储默认的彩色图像
default_colors = wc.to_array()
plt.title("Custom colors")
plt.imshow(wc.recolor(color_func=grey_color_func, random_state=3),
           interpolation="bilinear")
wc.to_file("a_new_hope.png")
plt.axis("off")
plt.figure()
plt.title("Default colors")
plt.imshow(default_colors, interpolation="bilinear")
plt.axis("off")
plt.show()
