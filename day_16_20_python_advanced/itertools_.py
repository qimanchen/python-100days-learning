#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-21 10:29:05
# @Author  : Qiman Chen
# @Version : $Id$

"""
迭代工具 - 排列/组合/笛卡尔积
"""


import itertools


# 排列
print("****排列****")
for i in itertools.permutations('ABCD'):
	print(i)
print("*"*30)


# 组合
print("*****组合*****")
for i in itertools.combinations('ABCD', 3):
	print(i)
print("*"*30)


# 笛卡尔积
print("****笛卡尔积****")
for i in itertools.product('ABCD', '123'):
	print(i)
