#!/usr/bin/env python
"""
Minimal Example
===============

Generating a square wordcloud from the US constitution using default arguments.
"""

from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# 读取整个文本
text = open(path.join(d, 'constitution.txt')).read()

# 生成一个词云图像
wordcloud = WordCloud().generate(text)

# matplotlib的方式展示生成的词云图像
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

#设定生成词云中的文字最大大小
wordcloud = WordCloud(max_font_size=66).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# pil方式展示生成的词云图像（如果你没有matplotlib）
# image = wordcloud.to_image()
# image.show()
