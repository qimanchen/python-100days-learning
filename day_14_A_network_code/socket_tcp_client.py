#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 10:45:07
# @Author  : Qiman Chen
# @Version : $Id$

"""
TCP套接字客服端
"""


from socket import socket


def main():

	# 1.创建套接字对象，默认使用IPv4和TCP协议
	client = socket()

	# 2.连接到服务器（需要指定服务器ip和端口）
	client.connect(('192.168.0.37', 6789))

	# 3.从服务器接收数据
	print(client.recv(1024).decode('utf-8'))
	client.close()


if __name__ == "__main__":
	main()
