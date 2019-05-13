#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
华氏温度转摄氏温度
student: Qiman chen

time: 2019/05/14
"""

if __name__ == "__main__":
	f = float(input("请输入华氏温度："))
	c = (f - 32) / 1.8
	# %.1f表示保留小数点后1位
	print('%.1f华氏度 = %.1f摄氏度'%(f,c))