#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-21 10:14:01
# @Author  : Qiman Chen
# @Version : $Id$

"""
顺序查找
"""


def seq_search(items, key):
	"""
	顺序查找
	"""

	for index, item in enumerate(items):
		if item == key:
			return index
	return -1
