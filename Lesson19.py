#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019-05-31 15:28
# @Author  : zan
# @File    : Lesson19.py
# @Title   : 常用的三方模块

'Pillow'

from PIL import Image

# 打开一个jgp图像文件，注意是当前路径
im = Image.open('test.jpg')
# 获得图像尺寸：
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%：
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')


from PIL import Image, ImageFilter

im = Image.open('img_home_ad.jpg')
# 应用模糊滤镜
im1 = im.filter(ImageFilter.BLUR)
im1.save('blur.jpg', 'jpeg')


#生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母
def rndChar():
    return chr(random.randint(65, 90))

# 随机颜色1
def rndColor1():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 240 x 60
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor1())
# 输出文字:
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
















