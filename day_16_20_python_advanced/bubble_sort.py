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
		# 在序列中比较出最小的并交换
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

def bubble_sort_origin(origin_items, comp=lambda x, y: x>y):
	"""
	冒泡排序最初的实现
	从小到大排序
	"""

	items = origin_items[:]

	for i in range(len(items)-1):
		for j in range(i+1, len(items)-1):
			if comp(items[i], items[j]):
				items[i], items[j] = items[j], items[i]

def bubble_sort_improve(origin_items, comp=lambda x, y: x>y):
	"""
	冒泡排序，排除已排序好的序列
	"""

	items = origin_items[:]

	for i in range(len(items)-1):
		count = 0
		for j in range(i+1, len(items)-1):
			if comp(items[i], items[j]):
				items[i], items[j] = items[j], items[i]
				count += 1
		# 去除已排序好的序列
		if count == 0:
			break
	return items

def main():
	"""
	"""
	test_list = [78,45,3,8,90,24,32,9]
	print(test_list)
	print(bubble_sort(test_list))


if __name__ == "__main__":
	main()
