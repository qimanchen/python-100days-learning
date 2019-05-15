#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
寻找1000以内的水仙花数
"""

def find_narcissistic(num_range):
	for i in range(num_range+1):
		str_i = str(i)
		count = 0
		for j in str_i:
			count += int(j) ** 3
		if count == i:
			print("%d 是水仙花数" % count)
			
			
if __name__ == "__main__":
	find_narcissistic(1000)
	
		
			