#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装饰器输出程序的运行时间
"""
from functools import wraps
import time


def record_time(func):
	"""
	输出 func 的运行时间
	不带输入参数
	"""
	@wraps(func)
	def wrapper(*args, **kwargs):
		
		start = time.time() # 函数运行开始的运行时间
		# 被装饰函数的返回值
		result = func(*args, **kwargs)
		# 计算函数的运行时间
		print(f'{func.__name__}:{time.time()-start)秒')
		return result
	return wrapper
	
	
# 带参数的装饰器
def record_time_with_param(output):
	"""
	"""
	def decorator(func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			start = time.time()
			result = func(*args, **kwargs)
			output(func.__name__, time.time()-start)
			return result
		return wrapper
	return decorator
	

# 装饰器类
class RecordTime():
	"""
	通过__call__魔法方法使得对象可以当成函数调用
	"""
	
	def __init__(self, output):
		self.output = output
		
	def __call__(self, func):
		@wraps(func)
		def wrapper(*args, **kwargs):
			start = time.time()
			result = func(*args, **kwargs)
			self.output(func.__name__, time.time()-start)
			return result
		return wrapper
		
	