#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
输入圆的半径计算周长和面积
qimanchen
2019/05/14
"""

import math


if __name__ == "__main__":
	radius = float(input("请输入圆的半径："))
	perimeter = 2*math.pi *radius	# 周长
	area = math.pi * radius * radius	# 面积
	print('周长：%2.2f' % perimeter)
	print('面积：%1.f' % area)
	