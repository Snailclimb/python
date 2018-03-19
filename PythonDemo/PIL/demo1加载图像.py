# -*- coding: utf-8 -*-
"""
使用 Image 类
"""

from PIL import Image
im = Image.open("alice_color.png")
#format 这个属性标识了图像来源
#size属性是一个二元tuple，(600, 800)：宽：600px，高：800px
# mode 属性定义了图像bands的数量和名称，以及像素类型和深度。常见的modes 有 “L” (luminance) 表示灰度图像, “RGB” 表示真彩色图像, and “CMYK” 表示出版图像。
print(im.format, im.size, im.mode)#PNG (600, 800) RGBA
im.show()#显示图像