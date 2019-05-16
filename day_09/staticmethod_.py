#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
静态方法
"""
import math


class Triangle(object):
	"""
	三角形
	"""
	
	def __init__(self, a, b, c):
		self._a = a
		self._b = b
		self._c = c
		
	@staticmethod
	def is_valid(a, b, c):
		return a+b>c and a+c > b and b+c > a
		
	def perimeter(self):
		"""
		求周长
		"""
		return self._a + self._b + self._b
		
	def area(self):
		"""
		求面积
		"""
		half = self.perimeter() / 2
		return math.sqrt(half * (half - self._a) * (half - self._b) *(half - self._c))
		

def main():
	"""
	"""
	a, b, c = 3, 4, 5
	# 静态方法和类方法都是通过给类发消息来调用的
	if Triangle.is_valid(a, b, c):
		t = Triangle(a, b, c)
		print(t.perimeter())
		
		# 同样可以通过类发消息来调用对象方法，但要传入接收消息的对象作为参数
		# print(Triangle.perimeter(t))
		print(t.area())
		# print(Triangle.area(t))
	else:
		print('无法构成三角形')
		

if __name__ == "__main__":
	main()
