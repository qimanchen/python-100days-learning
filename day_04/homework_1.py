#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
判断一个数是否是一个素数
"""
from math import sqrt


def is_prime(num):
	"""
	判断一个数是否是素数
	"""
	if isinstance(num, str):
		num = int(num)
	end = int(sqrt(num))
	
	is_pri = True
	
	for x in range(2, end+1):
		if num % x == 0:
			is_pri = False
			break
	if is_pri and num != 1:
		print("%d是素数" % num)
	else:
		print("%d不是素数" % num)
		
		
if __name__ == "__main__":
	num = input("请输入一个正整数: ")
	is_prime(num)
