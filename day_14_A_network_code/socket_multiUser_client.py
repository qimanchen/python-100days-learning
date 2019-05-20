#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 11:08:16
# @Author  : Qiman Chen
# @Version : $Id$

"""
多用户socket - 客服端
"""


from socket import socket
from json import loads
from base64 import b64decode


def main():
	client = socket()
	client.connect(('192.168.0.37', 6789))
	# 定义一个保存二进制数据的对象
	in_data = bytes()

	# 由于不知道要接收的数据量的大小，定义每次最大接收为1024
	data = client.recv(1024)

	while data:
		# 拼接数据
		in_data += data
		data = client.recv(1024)

		# 将接收到的二进制数据解码成json字符串，并转换成字典
		# loads函数的作用就是将json字符转换成字典对象
	my_dict = loads(in_data.decode('utf-8'))
	filename = my_dict['filename']
	filedata = my_dict['filedata'].encode('utf-8')
	with open(filename, 'wb') as f:
		f.write(b64decode(filedata))
	print('图片已保存')
	client.close()


if __name__ == "__main__":
	main()
