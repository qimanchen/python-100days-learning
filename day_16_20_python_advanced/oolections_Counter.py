#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-21 10:37:28
# @Author  : Qiman Chen
# @Version : $Id$

"""
找出序列中出现次数最多的元素
"""


from collections import Counter

words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around',
	'the', 'eyes', "don't", 'look', 'around', 'the', 'eyes',
	'look', 'into', 'my', 'eyes', "you're", 'under'
]

# 创建计数对象
counter = Counter(words)
# 找出出现次数大于三的值
print(counter.most_common(3))
