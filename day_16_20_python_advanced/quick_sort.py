#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-21 14:36:25
# @Author  : Qiman Chen
# @Version : $Id$

"""
分治法实例： 快速排序
"""


"""
快速排序 - 选择枢轴对元素进行划分，左边都比枢轴小右边都比枢轴大
"""


def quick_sort(origin_items, comp=lambda x, y: x<=y):
	"""
	快速排序
	"""
	items = origin_items[:]
	_quick_sort(items, 0, len(items)-1, comp)
	return items

def _quick_sort(items, start, end, comp):
	"""
	执行快速排序搜索
	"""
	if start < end:
		# 设置基准数
		pos = _partition(items, start, end, comp)
		# 后向前操作
		_quick_sort(items, start, pos-1, comp)
		# 前向后操作
		_quick_sort(items, pos+1, end, comp)

def _partition(items, start, end, comp):
	"""
	找出中间位置
	"""
	# 假设移动指针从最后的元素开始
	pivot = items[end]
	i = start - 1
	for j in range(start, end):
		if comp(items[j], pivot):
			i += 1
			items[i], items[j] = items[j], items[i]
	items[i+1], items[end] = items[end], items[i+1]
	return i + 1


def __quick_sort(origin_items, start, end):
	items = origin_items[:]

	if start < end:
		# 确定操作范围
		i, j = start, end

		# 设置基准数
		base = items[i]

		while i < j:
			# 找出大区的小数
			while (i<j) and (items[j] >= base):
				j = j - 1

			items[i] = items[j]

			# 找出小区的大数
			while (i<j) and (items[i] <= base):
				i = i + 1
			items[j] = items[i]
		# 基准复原
		items[i] = base

		__quick_sort(items, start, i-1)
		__quick_sort(items, j+1, end)
	return items

def mergeSort(lst):
	# 
	if len(lst) < 2:
		return lst
	midIndex = int(len(lst)/2)
	left, right = lst[:midIndex], lst[midIndex:]
	return merge(mergeSort(left),mergeSort(right))
	
def merge(left, right):
	result = []
	
	while left and right:
		if left[0] <= right[0]:
			result.append(left.pop(0))
		else:
			result.append(right.pop(0))
	while left:
		result.append(left.pop(0))
	while right:
		result.append(right.pop(0))
	return result
	
def quickSort(lst):
	# 快排
	if len(lst) < 2:
		return lst
	
	midNum = lst[0]
	
	less = [lst[i] for i in range(1, len(lst)) if lst[i] <= midNum]
	large = [lst[i] for i in range(1, len(lst)) if lst[i] > midNum]
	
	return quickSort(less) + [midNum] + quickSort(large)

def main():
	a = [3,1,34,4,2,56,98,0]
	print(mergeSort(a))
	
if __name__ == "__main__":
	main()
