#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
输入年份：如果是闰年输出True，否则输出False
2019/05/14
"""

if __name__ == "__main__":
	year = int(input("请输入年份："))
	# 如果代码太长，单行不便于阅读，可以使用\或()折行
	is_leap = (year % 4 == 0 and year % 100 != 0 or
					   year % 400 == 0)
	print(is_leap)
	