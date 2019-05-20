#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 21:02:37
# @Author  : Qiman Chen
# @Version : $Id$

"""
拆分字符串
"""
import re


def main():
	poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
	pattern = re.compile(r'[,.，。]')

	sentence_list = re.split(pattern, poem)

	while '' in sentence_list:
		sentence_list.remove('')

	print(sentence_list)


if __name__ == "__main__":
	main()
