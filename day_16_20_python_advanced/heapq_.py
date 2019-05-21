#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-21 10:22:35
# @Author  : Qiman Chen
# @Version : $Id$

"""
从列表中找出最大的或最小的N个元素
堆结构（大根堆/小根堆）
"""


import heapq


list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [{'name': 'IBM', 'shares': 100, 'price': 91.1},
	{'name': 'AAPL', 'shares': 50, 'price': 543.22},
	{'name': 'FB', 'shares': 200, 'price': 21.09},
	{'name': 'HPQ', 'shares': 35, 'price': 31.75},
	{'name': 'YHOO', 'shares': 45, 'price': 16.35},
	{'name': 'ACME', 'shares': 75, 'price': 115.65}]
# 找出序列中最大的三个元素
print(heapq.nlargest(3, list1))

# 找出序列中最小的三个元素
print(heapq.nsmallest(3,list1))

# 找出价格最高的两个公司
print(heapq.nlargest(2,list2, key=lambda x: x['price']))

# 找出共享度最高的两个公司
print(heapq.nlargest(2, list2, key=lambda x: x['shares']))
