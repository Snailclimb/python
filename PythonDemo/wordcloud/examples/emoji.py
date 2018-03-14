#!/usr/bin/env python
"""
Emoji Example
===============
一个简单的例子，显示如何包含表情符号。 请注意，这个例子似乎不适用于OS X（苹果系统），但是确实如此
在Ubuntu中正常工作
包含表情符号有3个重要步骤：
1) 使用io.open而不是内置的open来读取文本输入。 这确保它被加载为UTF-8
2) 重写词云使用的正则表达式以将文本解析为单词。 默认表达式只会匹配ascii的单词
3) 将默认字体覆盖为支持表情符号的东西。 包含的Symbola字体包括黑色和白色大多数表情符号的白色轮廓。 目前PIL / Pillow库存在的问题似乎可以预防
它在OS X上运行正常（https://github.com/python-pillow/Pillow/issues/1774）。
如果你有问题，试试在Ubuntu上运行
"""
import io
import string
from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

#使用io.open将文件正确加载为UTF-8非常重要
text = io.open(path.join(d, 'happy-emoji.txt')).read()

# the regex used to detect words is a combination of normal words, ascii art, and emojis
# 2+ consecutive letters (also include apostrophes), e.x It's
normal_word = r"(?:\w[\w']+)"
# 2+ consecutive punctuations, e.x. :)
ascii_art = r"(?:[{punctuation}][{punctuation}]+)".format(punctuation=string.punctuation)
# a single character that is not alpha_numeric or other ascii printable
emoji = r"(?:[^\s])(?<![\w{ascii_printable}])".format(ascii_printable=string.printable)
regexp = r"{normal_word}|{ascii_art}|{emoji}".format(normal_word=normal_word, ascii_art=ascii_art,
                                                     emoji=emoji)

# 生成一个词云图片
# Symbola字体包含大多数表情符号
font_path = path.join(d, 'fonts', 'Symbola', 'Symbola.ttf')
wordcloud = WordCloud(font_path=font_path, regexp=regexp).generate(text)

# 采用matplotlib方式：展示生成的图片
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
