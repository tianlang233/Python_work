# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-11-06 17:57:01
# @Last Modified by:   take
# @Last Modified time: 2017-11-06 18:36:34
class Word(str):
	def __init__(self, arg=''):
		total = 0
		arg = arg.strip()
		for each in arg:
			if each == ' ':
				break
			total += 1
		self.total = total

	def __ge__(self, other):
		return int.__ge__(self.total, other.total)

	def __gt__(self, other):
		return int.__gt__(self.total, other.total)

	def __le__(self, other):
		return int.__gt__(self,total, other.total)

	def __eq__(self, other):
		return int.__eq__(self.total, other.total)

	def __lt__(self, other):
		return int.__lt__(self.total, other.total)

a = Word('a      sfhjkaskf=')
b = Word('fishc')
print(a < b)

# if ' ' in word:
# 	word = word[:word.index(' ')]
