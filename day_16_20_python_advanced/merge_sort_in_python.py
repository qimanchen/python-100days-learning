#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
归并排序
"""
class MergeSort(object):
	"""
	归并排序
	"""
	
	def __init__(self, array):
		self.array = array
		
	def merge_sort(self, array):
		if len(array) < 2:
			return self.array
		middle = int(len(array)/2)
		left, right = array[0:middle], array[middle:]
		return self.merge(self.merge_sort(left), self.merge_sort(right))
		
	def merge(self, left, right):
		# 归并处理
		result = []
		while left and right:
			if left[0] <= right [0]:
				result.append(left.pop(0))
			else:
				result.append(right.pop(0))
		# 处理剩余的左段
		while left:
			result.append(left.pop(0))
		# 处理剩余的右段
		while right:
			result.append(right.pop(0))
		return result

# 排序
def merge(lfrom, lto, low, mid, high):
	i, j, k = low, mid, low
	
	while i < mid and j < high:
		# 反复复制两分段中较小的
		if lfrom[i] <= lfrom[j]:
			lto[k] = lfrom[i]
			i += 1
		else:
			lto[k] = lfrom[j]
			j += 1
		k += 1
	while i < mid:
		# 复制第一段中剩余记录
		lto[k] = lfrom[i]
		i += 1
		k += 1
	while j < high:
		# 复制第二段中剩余的记录
		lto[k] = lfrom[j]
		j += 1
		k += 1
		
# 分段和合并
def merge_pass(lfrom, lto, llen, slen):
	i = 0
	while i + 2*slen < llen:
		merge(lfrom, lto, i, i+slen, i+2*slen)
		i += 2*slen
	if i + slen < llen:
		merge(lfrom, lto, i, i+slen, llen)
	else:
		for j in range(i, llen):
			lto[j] = lfrom[j]
			
# 主函数
def merge_sort(lst):
	slen, llen = 1, len(lst)
	templst = [None]*llen
	while slen < llen:
		merge_pass(lst, templst, llen, slen)
		slen *= 2
		merge_pass(templst, lst, llen, slen)
		slen *= 2
	return lst
	
def main():
	testList = [2,4,7,5,8,1,3,6]
	print(merge_sort(testList))
	s = MergeSort(testList)
	print(s.merge_sort(s.array))
	
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        while not pHead1 or not pHead2:
            return None
        
        cpHead1 = pHead1
        cpHead2 = pHead2
        
        listHead1 = []
        listHead2 = []
        while cpHead1:
            listHead1.append(cpHead1.val)
            cpHead1 = cpHead1.next
        while cpHead2:
            listHead2.append(cpHead2.val)
            cpHead2 = cpHead2.next
        
        result = []
        while listHead1 and listHead2:
            if listHead1[-1] == listHead2[-1]:
                result.append(listHead1[-1])
                listHead1.pop()
                listHead2.pop()
            else:
                break
        if len(result) == 0:
            return None
        # result = result[::-1]
        
        resultHead = None
        for i in result:
            # 注意这里时首端插入
            midHead = ListNode(i)
            midHead.next = resultHead
            resultHead = midHead
        return resultHead
		
if __name__ == "__main__":
	main()
