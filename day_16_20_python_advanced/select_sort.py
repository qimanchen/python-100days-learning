#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 21:49:55
# @Author  : Qiman Chen
# @Version : $Id$

"""
选择排序
"""


def select_sort(origin_items, comp=lambda x, y: x<y):
	"""
	简单选择排序
	每一轮循环找出最小一个插入到已排序好的序列内
	:param origin_items : 目标数列
	"""

	# 取得目标数列的copy
	items = origin_items[:]

	for i in range(len(items) - 1):
		min_index = i
		for j in range(i+1, len(items)):
			# 比较出较小的元素
			if comp(itmes[j], items[min_index]):
				min_index = j

		items[i], itmes[min_index] = itmes[min_index], items[i]

	return itmes
