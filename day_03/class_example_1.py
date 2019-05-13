#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
用户身份验证
"""

if __name__ == "__main__":
	username = input("请输入用户名：")
	password = input("请输入口令：")
	# 如果希望输入口令时，终端没有回显，可以使用getpass模块中的getpass函数
	# import getpass
	# password = getpass.getpass('请输入口令：')
	if username == 'admin' and password == '123456':
		print('身份验证成功！')
	else:
		print('身份验证失败！')
		
		