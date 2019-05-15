#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
百鸡百钱
鸡翁 5钱
鸡母 3钱
鸡雏 三值一钱
"""

def hundred_chick_hundred_money():
	# 鸡公 x
	
	# 母鸡 y
	
	# 小鸡 k
	for x in range(20):
		for y in range(33):
			count = 3*y + 5*x + (100-x-y)/3
			if count == 100:
				print("鸡公 %d只，母鸡 %d只，小鸡 %d只" % (x,y,100-x-y))
				
if __name__ == "__main__":
	hundred_chick_hundred_money()
