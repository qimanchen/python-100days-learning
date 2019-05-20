#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 16:07:12
# @Author  : Qiman Chen
# @Version : $Id$

"""
操作图像
使用pillow模块
"""
from PIL import Image


def main():
	"""
	"""

	# 打开图像
	image = Image.open('图像名.jpg')
	print(image.format, image.size, image.mode)
	# 'JPEG', (500, 750), 'RGB'

	# 显示图像
	image.show()

	# 裁剪图像
	# 左上角，右下角坐标
	rect = 80, 20, 310, 360
	image.crop(rect).show()

	# 生成缩略图
	size = 128, 128
	image.thumbnail(size)
	image.show()

	# 缩放和粘贴
	image1 = Image.open('luohao.png')
	image2 = Image.open('guido.jpg')
	rect = 80, 20, 310, 360
	guido_head = image2.crop(rect)
	width, height = guido_head.size

	# 粘贴
	image1.paste(guido_head.resize((int(width/1.5), int(height/1.5))), (172, 40))

	# 旋转和翻转
	image.rotata(180).show()
	image.transpose(Image.FLIP_LEFT_RIGHT).show()

	# 操作像素 -- 指定区域填充颜色
	for x in range(80, 310):
		for y in range(20, 360):
			image.putpixel((x,y), (128, 128,128))

	# 滤镜效果
	from PIL import Image, ImageFilter

	image.filter(ImageFilter.CONTOUR).show()


if __name__ == "__main__":
	main()
