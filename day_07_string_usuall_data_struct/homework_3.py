#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""

def get_suffix(filename, has_dot=False):
	"""
	取得文件名的后缀
	
	:param filename:文件名
	:param has_dot: 返回后缀名是否需要带点
	:return: 文件后缀名
	"""
	
	pos = filename.rfind('.')
	if 0 < pos < len(filename) - 1:
		index = pos if has_dot else pos + 1
		return filename[index:]
	else:
		return ""
		
def get_suffix_split(filename):
	"""
	"""
	name_list = filename.split(".")
	return name_list[-1]
	
if __name__ == "__main__":
	print(get_suffix("manman.txt"))
	print(get_suffix_split("manman.txt"))
	
	