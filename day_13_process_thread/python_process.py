#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 21:16:24
# @Author  : Qiman Chen
# @Version : $Id$

"""
python中执行多进程任务
"""


from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep


def download_task(filename):
	"""
	下载文件任务
	"""
	print('启动下载进程，进程号[%d].' % getpid())
	print('开始下载%s...' % filename)
	time_to_download = randint(5, 10)
	sleep(time_to_download)
	print('%s下载完成！耗费了%d秒' % (filename, time_to_download))


def main():
	"""
	"""

	start = time()
	p1 = Process(target=download_task, args=('python从入门到住院.pdf',))
	p1.start()
	p2 = Process(target=download_task, args=('Peking Hot.avi',))
	p2.start()

	p1.join()
	p2.join()
	end = time()

	print('总共耗费了%.2f秒' % (end-start))


if __name__ == "__main__":
	main()
