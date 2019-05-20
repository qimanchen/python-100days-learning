#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
实现求最大公约数和最小公倍数
"""

def gcd(x, y):
	"""
	最大公约数
	"""
	if x>y:
		x, y = y, x
	# (x,y) = (y,x) if (x>y) else (x,y)
	for factor in range(x,0, -1):
		if x % factor == 0 and y % factor == 0:
			return factor
			
def lcm(x,y):
	"""
	最小公倍数
	"""
	return x*y//gcd(x,y)
	
