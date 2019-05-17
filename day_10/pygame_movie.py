#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 09:11:49
# @Author  : Qiman Chen
# @Version : $Id$

"""
pygame 游戏模块

"""


import pygame


def main():
	# 初始化导入pygame中的模块
	pygame.init()

	# 初始化用于显示的窗口并设置窗口尺寸
	screen = pygame.display.set_mode((800, 600))

	# 设置当前窗口标题
	pygame.display.set_caption('打球吃小球')

	# 定义变量表示小球在屏幕上的位置
	x, y = 50, 50

	running = True

	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
		# 设置窗口背景颜色
		screen.fill((245, 245, 245))

		# 通过指定文件名加载图像
		ball_image = pygame.image.load('ball.png')

		# 在窗口上渲染图像
		screen.blit(ball_image, (x, y))

		# 刷新当前窗口
		pygame.display.flip()

		# 每隔50毫秒就改变小球的位置再刷新窗口
		pygame.time.delay(50)
		x, y = x+5, y+5


if __name__ == '__main__':
	main()
