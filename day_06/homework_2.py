#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
判断是否为回文数
"""

def is_palindrome(num):
	"""
	"""
	temp = num
	total = 0
	
	while temp > 0:
		total = toatl * 10 + temp % 10
		temp //= 10
	return total == num