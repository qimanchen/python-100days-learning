#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
背包问题 -- 动态规划
"""

weight = [0, 1, 4, 3, 1] # n个物体的重量
price = [0, 1500, 3000, 2000, 2000] # n个物体的价格
n = len(weight) - 1 # 物品的个数

m = 4

x = []
v = 0

optp = [[0 for col in range(m+1)] for raw in range(n+1)]


def solution(weight, price,n, m, x):
	"""
	"""
	# 计算optp[i][j]

	# 遍历每个物品
	for i in range(1, n+1):
		# 遍历背包大小
		for j in range(1, m+1):
			if (j >= weight[i]):
				optp[i][j] = max(optp[i-1][j], optp[i-1][j-weight[i]] + price[i])
			else:
				optp[i][j] = optp[i-1][j]

	j = m
	for i in range(n, 0, -1):
		if optp[i][j] > optp[i-1][j]:
			x.append(i)
			j = j - weight[i]

	v = optp[n][m]
	return v

print(solution(weight, price, n, m, x))
print(x)