#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 22:00:48
# @Author  : Qiman Chen
# @Version : $Id$

"""
多线程之间的通信
"""


from time import sleep
from threading import Thread, Lock


class Account(object):
	"""
	银行账户
	"""

	def __init__(self):
		self._balance = 0
		# 设置互斥锁
		self._lock = Lock()


	# def deposit(self, money):
	# 	"""
	# 	"""
	# 	# 计算存款后的余额
	# 	new_balance = self._balance + money
	# 	# 模拟受理存款业务需要0.01秒的时间
	# 	sleep(0.01)
	# 	# 修改账户余额
	# 	self._balance = new_balance

	# def deposit(self, money):
	# 	# 先获取锁才能执行后续的代码
	# 	self._lock.acquire()
	# 	try:
	# 		new_balance = self._balance + money
	# 		sleep(0.01)
	# 		self._balance = new_balance
	# 	finally:
	# 		# 在finally中执行释放锁保证操作的正常运行
	# 		self._lock.release()

	def deposit(self, money):
		# 先获取锁才能执行后续的代码
		with self._lock:
			new_balance = self._balance + money
			sleep(0.01)
			self._balance = new_balance

	@property
	def balance(self):
		return self._balance


class AddMoneyThread(Thread):
	"""
	增加银行账户金额
	"""

	def __init__(self, account, money):
		super().__init__()
		self._account = account
		self._money = money

	def run(self):
		self._account.deposit(self._money)


def main():
	"""
	"""

	account = Account()
	threads = []

	# 创建100个存款的线程向同一个账户存钱
	for _ in range(100):
		t = AddMoneyThread(account, 1)
		threads.append(t)
		t.start()

	# 等待所有存款的线程都执行完毕
	for t in threads:
		t.join()

	print('账户余额为： ￥%d元' % account.balance)


if __name__ == "__main__":
	main()

	