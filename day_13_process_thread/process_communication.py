#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 21:25:56
# @Author  : Qiman Chen
# @Version : $Id$

"""
多进程之间的通信

"""


from multiprocessing import Process, Queue
from time import sleep


counter = 0


def sub_task(q, string):
	while not q.empty():
		q.get(True)
		print(string, end=' ', flush=True)
		sleep(0.01)


def main():
	q = Queue(10)
	for _ in range(10):
		q.put('Pong')
	Process(target=sub_task, args=(q, 'Ping')).start()
	Process(target=sub_task, args=(q, 'Pong')).start()


if __name__ =='__main__':
	main()
