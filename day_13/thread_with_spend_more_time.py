#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 22:36:06
# @Author  : Qiman Chen
# @Version : $Id$

"""
将耗时间的任务放入线程中以获得更好的用户体验
"""


import time
import tkinter
import tkinter.messagebox
from threading import Thread


def main()
	class DownloadTaskHandler(Thread):
		"""
		"""
		def run(self):
			time.sleep(10)
			tkinter.messagebox.showinfo('提示', '下载完成！')
			# 启用下载按钮
			button1.config(state=tkinter.NORMAL)

	def download():
		"""
		"""
		# 模拟下载任务需要花费10秒钟的时间
		time.sleep(10)
		tkinter.messagebox.showinfo('提示', '下载完成！')


	def show_about():
		"""
		"""
		tkinter.messagebox.showinfo('关于', '作者：骆昊')


def main():
	"""
	"""
	top = tkinter.Tk()
	top.title('单线程')
	top.geometry('200x150')
	top.wm_attributes('-topmost', True)

	panel = tkinter.Frame(top)
	button1 = tkinter.Button(panel, text='下载', command=download)
	button1.pack(side='left')
	button2 = tkinter.Button(panel, text='关于', command=show_about)
	button2.pack(side='right')
	panel.pack(side='bottom')

	tkinter.mainloop()


if __name__ == '__main__':
	main()
