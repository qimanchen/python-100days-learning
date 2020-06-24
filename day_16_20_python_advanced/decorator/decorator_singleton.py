#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
装饰器实现单例模式
"""
from functools import wraps
from threading import Lock


def singleton(cls):
	"""
	装饰类的装饰器 -- 传入的是类名
	"""
	instances = {}
	
	@wraps(cls)
	def wrapper(*args, **kwargs):
		if cls not in instances:
			instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return wrapper
	
@singleton
class President():
	"""
	单例类
	"""
	pass
	

# 实现线程安全的单例
def singleton_th(cls):
	"""
	线程安全的单例装饰器
	"""
	instances = {}
	locker = Lock()
	
	@wraps(cls)
	def wrapper(*args, **kwargs):
		if cls not in instances:
			with locker:
				if cls not in instances:
					instances[cls] = cls(*args, **kwargs)
		return instances[cls]
	return wrapper
	
	