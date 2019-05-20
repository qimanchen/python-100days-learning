#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 15:27:08
# @Author  : Qiman Chen
# @Version : $Id$

"""
使用互亿无线短信平台实现短信发送功能
"""


import urllib.parse
import http.client
import json


def main():
	host = '106.ihuyi.com'
	sms_send_uri = "/webservice/sms.php?method=Submit"

	# 设置相应的注册账号和密码
	params = urllib.parse.urlencode({'account': '账号', 'password': '密码', 
		'content': '要发送的内容', 'mobile': '接收者的手机号', 'format': 'json'})

	print(params)
	headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept':'text/plain'}
	conn = http.client.HTTPConnection(host, port=80, timeout=30)
	conn.request('POST', sms_send_uri, params, headers)

	response = conn.getresponse()
	response_str = response.read()
	jsonstr =response_str.decode('utf-8')
	print(json.loads(jsonstr))
	conn.close()


if __name__ == "__main__":
	main()
