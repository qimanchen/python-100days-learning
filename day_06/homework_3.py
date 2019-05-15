#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
判断是否为素数
"""

from homework_2 import is_palindrome


def is_prime(num):
	"""
	"""
	
	for factor in range(2, num):
		if num % factor == 0:
			return False
	return True if num != 1 else False
	
if __name__ == "__main__":
	num = int(input("请输入一个正整数："))
	
	if is_prime(num) and is_palindrome(num):
		print("%d是回文素数" % num)