#!/usr/bin/env python
"""
Masked wordcloud
================

使用蒙版图像可以生成任意形状的wordcloud。
"""

from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS

d = path.dirname(__file__)

# 读取整个文本.
text = open(path.join(d, 'alice.txt')).read()

#读取图片（图片来源：http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg）
alice_mask = np.array(Image.open(path.join(d, "alice_mask.png")))

stopwords = set(STOPWORDS)
stopwords.add("said")
#设置词云的一些属性
wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
               stopwords=stopwords)
# 生成词云
wc.generate(text)

#保存到本地
wc.to_file(path.join(d, "alice.png"))

#展示
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
