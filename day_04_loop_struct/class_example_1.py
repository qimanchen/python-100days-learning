#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
九九乘法表
"""


def nine_nine_multi_list():
	"""
	"""
	for i in range(1, 10):
		for j in range(1, i+1):
			print('{} * {} = {}'.format(i, j, i*j), end="\t")
		print("")
		
		
if __name__ == "__main__":
	nine_nine_multi_list()