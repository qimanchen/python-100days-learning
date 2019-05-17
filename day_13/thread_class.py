#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 21:53:03
# @Author  : Qiman Chen
# @Version : $Id$

"""
继承Thread，创建线程类

"""


from threading import Thread
from random import randint
from time import time, sleep


class DownloadTask(Thread):
	"""
	创建线程类
	"""
	def __init__(self, filename):
		super().__init__()
		self._filename = filename

	def run(self):
		"""
		线程运行实例方法
		"""
		print('开始下载%s...' % self._filename)
		time_to_download = randint(5, 10)
		sleep(time_to_download)
		print('%s下载完成！耗费了%d秒' % (self._filename, time_to_download))


def main():
	start = time()
	t1 = DownloadTask('Python从入门到住院.pdf')
	t1.start()
	t2 = DownloadTask('peking Hot.avi')
	t2.start()
	t1.join()
	t2.join()
	end = time()
	print('总共耗费了%.2f秒.' % (end-start))


if __name__ == "__main__":
	main()
