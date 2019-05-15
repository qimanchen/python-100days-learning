#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

def max2(x):
	"""
	返回传入列表的最大值和第二大元素的值
	"""
	m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
	
	for index in range(2, len(x)):
		if x[index] > m1:
			m2 = m1
			m1 = x[index]
		elif x[index] > m2:
			m2 = x[index]
			
	return m1, m2