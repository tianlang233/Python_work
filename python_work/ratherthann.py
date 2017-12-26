# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-11-24 14:10:05
# @Last Modified by:   take
# @Last Modified time: 2017-11-24 15:02:30
# class Nint(str):
# 	def __init__(self,string):
# 		if ' ' in string:
# 			index = string.index(' ')
# 			string = string[:index]
# 		self.length = len(string)
# 	def __add__(self, other):
# 		return int.__add__(self.length, other.length)
class Word(str):
'''储存单词的类，定义比较单词的几种方法'''

	def __new__(cls, word):
		if ' ' in word:
			print("Value contains spaces.Truncating to first space.")
			word = word[:word.index(' ')]
		return str.__new__(cls, word)	

	def __gt__(self, other):
		return len(self) > len(other)
	def __lt__(self, other):
		return len(self) < len(other)
	def __ge__(self, other):
		return len(self) >= len(other)
	def __le__(self, other):
		return len(self) <= len(other)