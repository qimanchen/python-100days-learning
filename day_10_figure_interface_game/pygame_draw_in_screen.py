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

	# 设置窗口背景颜色
	screen.fill((242, 242, 242))

	# 绘制一个圆（参数分别为：屏幕，颜色，圆心位置，半径，0表示填充圆)
	pygame.draw.circle(screen, (255, 0, 0), (100, 100), 30, 0)

	# 刷新当前窗口
	pygame.display.flip()
	
	running = True

	# 开启一个事件循环处理发生的事件
	while running:
		# 从消息队列中获取事件并对事件进行处理
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False


if __name__ == '__main__':
	main()
