#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 10:57:10
# @Author  : Qiman Chen
# @Version : $Id$

"""
多用户支持的服务器端
"""


from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
from json import dumps
from threading import Thread
from datetime import datetime


def main():

	# 自定义线程类
	class FileTransferHandler(Thread):

		def __init__(self, cclient):
			super().__init__()
			self.cclinet = cclient


		def run(self):
			my_dict = {}
			my_dict['filename'] = 'test.jpg'
			# json是纯文本不能携带二进制数据
			# 所以图片的二进制数据要处理成JSON字符串
			# 注意这里data是类外部的数据
			my_dict['filedata'] = data

			# 通过dumps把字典处理成JSON字符串
			json_str = dumps(my_dict)

			# 发送json字符串
			self.cclinet.send(json_str.encode('utf-8'))
			self.cclinet.close()

	# 创建套接字，并确定是那种传输服务
	server = socket(family=AF_INET, type=SOCK_STREAM)

	# 2.绑定IP地址和端口（区分不同服务）
	server.bind(('192.168.0.37', 6789))
	# 3.开启监听 - 监听客服端连接到服务器
	server.listen(512)
	print('服务器启动开始监听')

	with open('browers.jpg', 'rb') as f:
		# 将二进制数据处理成base64再进行解码处理
		data = b64encode(f.read()).decode('utf-8')

	while True:
		client, addr = server.accept()
		print('%s:%s连接到服务器' % (str(datetime.now()), str(addr)))
		# 启动一个线程来处理客服端请求
		FileTransferHandler(client).start()


if __name__ == "__main__":
	main()
