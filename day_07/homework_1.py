#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""
import os
import time


def main():
	"""
	跑马灯
	"""
	content = '广州欢迎您。。。'
	content = content.center(50, " ")
	while True:
		# 清理屏幕的输出
		os.system('cls')
		print(content)
		time.sleep(0.2)
		content = content[1:] + content[0]
		
if __name__ == "__main__":
	main()
