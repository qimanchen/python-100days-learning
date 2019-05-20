#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
"""
import random

def create_auth(code_len=4):
	"""
	生成指定长度的验证码
	"""
	all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
	last_pos = len(all_chars) -1
	code = ''
	for _ in range(code_len):
		index = random.randint(0, last_pos)
		code += all_chars[index]
	return code
	
if __name__ =="__main__":
	print(create_auth())
