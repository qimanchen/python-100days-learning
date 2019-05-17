#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
正则表达式的使用

(?=exp)  匹配exp前面的位置
(?<=exp)  匹配exp后面的位置
(?!exp)  匹配后面面不是exp的位置
(?<!exp)  匹配前面不是exp的位置
"""


"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
import re


def main():
	"""
	"""

	qqnum_pattern = re.compile(r'^[1-9]\d{4,11}$')
	username_pattern= re.compile(r'^\w{6,20}$')

	username = input("请输入用户名：")
	while not username_pattern.match(username):
		print("输入用户名格式不符合，请重新输入！")
		username = input("请输入用户名：")

	qq_number = input("请输入QQ号：")
	while not qqnum_pattern.match(qq_number):
		print("输入QQ号格式不符合，请重新输入！")
		qq_number = input("请输入QQ号：")
	


if __name__ == '__main__':
	main()
