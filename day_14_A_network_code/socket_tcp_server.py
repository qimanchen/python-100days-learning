#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 10:28:52
# @Author  : Qiman Chen
# @Version : $Id$

"""
流套接字 --TCP -- 服务器端
"""


from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime


def main():
	# 1.创建套接字对象并指定使用哪种服务
	# family=AF_INET - IPv4地址
	# family=AF_INET6 - IPv6地址
	# type=SOCK_STREAM - TCP套接字
	# type=SOCK_DGRAM - UDP套接字
	# type=SOCK_RAW - 原始套接字
	server = socket(family=AF_INET, type=SOCK_STREAM)

	# 2.创建IP地址和端口(端口用于区分不同的服务)
	# 同一时间在同一端口上只能绑定一个服务，否则会报错
	server.bind(('192.168.0.37', 6789))

	# 3.开启监听 - 监听客服端连接到服务器
	# 参数512可以理解为连接队列的大小
	server.listen(512)
	print('服务器启动开始监听')

	while True:
		# 4.通过循环接收客服端的连接并做出相应的处理（提供服务）
		# accept方法是一个阻塞的方法，如果没有客服端连接到服务器代码就不会向下执行
		# accept方法返回一个元组，启动第一个元素是客服端对象
		# 第二个元素是连接到服务器的客服端的地址（由IP和端口两部分组成）
		client, addr = server.accept()

		print(str(addr) + '连接到了服务器')

		# 5.发送数据
		client.send(str(datetime.now()).encode('utf-8'))

		# 6.断开连接
		client.close()


if __name__ == "__main__":
	main()
