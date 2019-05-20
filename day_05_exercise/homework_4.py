#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
生成斐波那契数列
"""

def fib(n):
	"""
	非迭代版
	"""
	a, b = 1,1
	while a <= n:
		print(a, end=" ")
		a, b = b, a+b
		
def fib_gene(n):
	"""
	生成器版
	"""
	a, b = 0, 1
	while n > 0:
		a, b = b, a+b
		yield a
		n -= 1
		
def fib_ite(n):
	"""
	迭代版
	"""
	if n == 1 or n == 2:
		return 1
	return fib_ite(n-1) + fib_ite(n-2)
	
if __name__ == "__main__":
	result = [i for i in fib_gene(5)]
	print(result)