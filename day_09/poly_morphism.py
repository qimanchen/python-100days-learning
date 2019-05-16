#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-16 21:48:05
# @Author  : Qiman Chen
# @Version : $Id$


from abc import ABCMeta, abstractmethod

"""
ABCMeta -- 定义一个虚类
abstractmethod -- 表示子类必须有此方法，否则会报错
abstractproperty -- 表示子类中必须有property属性

"""


class Pet(object, metaclass=ABCMeta):
	"""
	宠物
	"""

	def __init__(self, nickname):
		self._nickname = nickname

	@abstractmethod
	def make_voice(self):
		"""
		发出声音
		"""
		pass


class Dog(Pet):
	"""
	狗
	"""
	def make_voice(self):
		print('%s: 汪汪汪...' % self._nickname)


class Cat(Pet):
	"""
	猫
	"""

	def make_voice(self):
		print('%s: 喵...喵...' % self._nickname)


def main():

	pets = [Dog('旺财'), Cat('凯蒂'), Dog('大黄')]
	for pet in pets:
		pet.make_voice()


if __name__ == "__main__":
	main()
