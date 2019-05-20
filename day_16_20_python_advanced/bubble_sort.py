#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 21:57:13
# @Author  : Qiman Chen
# @Version : $Id$

"""
冒泡排序
"""


def bubble_sort(origin_items, comp=lambda x, y: x>y):
	"""
	冒泡排序
	"""

	items = origin_items[:]

	for i in range(len(items) - 1):
		swapped = False
		for j in range(i, len(items)-1-i):
			if comp(items[j], items[j+1]):
				items[j], items[j+1] = items[j+1], items[j]
				swapped = True
		if swapped:
			swapped = False
			for j in range(len(items)-2-i, i, -1):
				if comp(items[j-1], items[j]):
					items[j], items[j-1] = items[j-1], items[j]
					swapped = True

		if not swapped:
			break

	return items
