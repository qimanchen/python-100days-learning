#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2019-05-20 14:54:57
# @Author  : Qiman Chen
# @Version : $Id$

"""
使用简单邮件传输协议（SMTP）
实现一个电子邮件发送的应用

"""


from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():

	# 发送者
	sender = 'abcdefg@126.com'
	receivers = ['hijk123@qq.com', 'testtest@gmail.com']

	# 编辑要发送的信息和信息格式
	message = MIMEText('用Python发送邮件的实例代码.', 'plain', 'utf-8')
	message['From'] = Header('qiman_qq', 'utf-8')
	message['To'] = Header('qiman_phone', 'utf-8')
	message['Subject'] = Header('示例代码邮件', 'utf-8')
	smtper = SMTP('mail.qq.com')

	# 设置发送者的登录口令
	# 这里要登录到smtp服务器上
	smtper.login(sender, 'password')
	smtper.sendmail(sender, receivers, message.as_string())
	smtper.quit()
	print('邮件发送完成')


if __name__ == "__main__":
	main()
