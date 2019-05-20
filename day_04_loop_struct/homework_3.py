#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
打印各种三角形
"""


def print_angle(lines):
	"""
	"""
	# 第一种
	for i in range(1, lines+1):
		print("*" * i)
		
	# 第二种
	for i in range(lines, 0, -1):
		for j in range(1, lines+1):
			if j>=i:
				print("*", end="")
			else:
				print(" ", end="")
		print()
	
	# 第三种
	# i * (i-1)*2
	# (lines-1), 
	
	for j in range(1, lines + 1):
		print(" "*(lines-j) + "*"* (1+(j-1)*2))
	
if __name__ == "__main__":
	lines = int(input("请输入行数："))
	print_angle(lines)
