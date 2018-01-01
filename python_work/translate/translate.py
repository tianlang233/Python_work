#!/usr/bin/python３
# -*- coding: utf-8 -*-
#运行环境 python3
# 当前环境，archlinux
#必备环境，nodejs，需要运行一段js代码，
#需要的模组，PyExecJS, requests,urllib, easygui

import requests, re
import easygui as g
import urllib
from json import loads
from tk import Py4Js

def Translate(string):
	#通过将输入的内容转化为url编码，检测输入的字符是英文还是中文

	#由于在转换成URL编码时空格会转换成为 %20 ，在接下来的检测中英文这一步会出错，所以在这里把空格删除进行判断。为了不影
	#响之后的翻译内容，所以重新创建一个变量 string_test 作为检测用变量
	string_test = string
	while ' ' in string_test:
		count = string_test.index(' ')
		string_test = string_test[:count] + string_test[count + 1:]

	if urllib.parse.quote(string_test) == string_test:
		sl = 'en'
		tl = 'zh-CN'
	else:
		sl = 'zh-CN'
		tl = 'en'

	#根据输入的字符，返回相应的tk值
	js = Py4Js()
	tk = js.getTk(string)
	#将汉字转换为url编码
	text = urllib.parse.quote(string)

	url = 'https://translate.google.cn/translate_a/single?client=t&\
			sl=%s&tl=%s&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&\
			dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&\
			kc=1&tk=%s&q=%s' % (sl, tl, tk, text)

	html = requests.get(url).content
	html = str(html, encoding = "utf-8")
	json = loads(html)


	return json[0][0][0]

while True:
	string = g.enterbox('请输入要翻译的内容(苹果): ')
	try:
		msg = Translate(string)
	except TypeError:
		break
	if not g.ccbox(msg + '\n\n\n是否继续?', choices = ('继续', '退出')):
		break
