#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
寻找完全数：
一个数的真因子之和等于他自身
"""


def is_perfect(num):
	"""
	"""
	comment = []
	if num == 1:
		return False
	for i in range(1, num):
		if num % i == 0:
			comment.append(i)
	count = 0
	for x in comment:
		count += x
	if num == count:
		print("%d 是完全数" % num)
		return True
	else:
		print("%d 不是完全数" % num)
		return False
		
if __name__ == "__main__":
	is_perfect(496)
