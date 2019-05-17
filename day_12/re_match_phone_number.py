#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-17 20:17:54
# @Author  : Qiman Chen
# @Version : $Id$

"""
匹配国内手机号

电信号段：133/153/180/181/189/177;
联通号段：130/131/132/155/156/185/186/145/176
移动号段： 134/135/136/137/138/139/150/151/152/157/158/159/182/183/184/187/188/147/178
"""
import re


def main():
    # 创建正则表达式对象
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    sentence = """重要的事情说8130123456789遍，
    我的手机号是13512346789这个靓号，
    不是15600998765，
    也是110或119，
    王大锤的手机号才是15600998765。"""
    print(sentence)
    # 查找所有匹配并保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    print('*'*50)
    # 通过迭代器取出匹配对象并获得匹配内容
    for temp in pattern.finditer(sentence):
        print(temp.group())

    print('*'*50)
    # 通过search函数指定搜索位置
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


if __name__ == "__main__":
    main()
    