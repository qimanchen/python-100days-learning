#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
多进程进行求和运算
multiprocessing中的manager内的
quque模块可以用于爬虫
"""


from multiprocessing import Process, Queue
from random import randint
from time import time


def task_handler(curr_list, result_queue):
	"""
	任务队列处理
	"""
	total = 0
	for number in curr_list:
		total += number
	result_queue.put(total)
	
def main():
	processes = []
	number_list = [x for x in range(1, 10000001)]
	result_queue = Queue()
	index = 0
	# 启动8个进程将数据切片后进行运算
	for _ in range(8):
		p = Process(target=task_handler, args=(number_list[index:index + 12500000], result_queue))
		index += 12500000
		processes.append(p)
		p.start()
	# 开始记录所有进程执行完成消耗的时间
	start = time()
	for p in processes:
		p.join()
	total = 0
	while not result_queue.empty():
		total += result_queue.get()
	print(total)
	end = time()
	print('Execution time: ', (end - start), 's', sep='')
	
	
if __name__ == '__main__':
	main()
