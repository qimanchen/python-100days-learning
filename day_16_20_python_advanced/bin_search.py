#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-21 10:15:44
# @Author  : Qiman Chen
# @Version : $Id$

"""
折半查找
"""


def bin_search(items, key):
	"""
	折半查找
	"""

	start, end = 0, len(items) - 1
	while start <= end:
		mid = (start + end) // 2
		if key > items[mid]:
			start = mid + 1
		elif key < items[mid]:
			end = mid - 1
		else:
			return mid
	return -1
