#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
动态规划 -- 斐波那契数列
"""

def fib(num, temp={}):
	"""
	递归实现fib
	"""
	if num in (1,2):
		return 1
	try:
		return temp[num]
	except KeyError:
		temp[num] = fib(num-1) + fib(num-2)
		return temp[num]
		
def fib_while(num):
	"""
	使用非递归构建fib
	"""
	temp = []
	count = 1
	while count <= num:
		if count in (1,2):
			temp.append(1)
			count+= 1
			continue
		temp.append(temp[-1] + temp[-2])
		count += 1
	return temp
	

if __name__ == "__main__":
	print(fib(1000))
	#print(fib_while(10000))
