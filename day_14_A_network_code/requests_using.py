#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 10:06:19
# @Author  : Qiman Chen
# @Version : $Id$

"""
requests模块的使用

"""

from time import time
from threading import Thread


import requests


# 继承Thread类创建自定义的线程类
class DownloadHandler(Thread):
	"""

	"""

	def __init__(self, url):
		super().__init__()
		self.url = url


	def run(self):
		"""
		通过url获取网页信息
		"""

		filename = self.url[self.url.rfind('/')+1:]
		resp = requests.get(self.url)
		with open(filename, 'wb') as f:
			f.write(resp.content)


def main():
	"""
	"""

	resp = requests.get('http://api.tianapi.com/meinv/?key=APIKey&num=10')
	data_model = resp.json()
	for mm_dict in data_model['newslist']:
		url = mm_dict['picUrl']
		DownloadHandler(url).start()


if __name__ == "__main__":
	main()
