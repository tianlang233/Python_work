# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-11-05 13:22:45
# @Last Modified by:   take
# @Last Modified time: 2017-11-05 14:01:24
#字符窜的减法
# class Nstr(str):
# 	def __sub__(self, other):
# 		return self.replace(other, '')
# a = Nstr("I love FishC.com!iiiiiiiiiii")
# b = Nstr('i')
# print(a - b)
#字符窜的移位操作符
# class Nstr(str):
# 	def __lshift__(self, other):
# 		return self[other: ] + self[: other]
# 	def __rshift__(self, other):
# 		return self[:-other] + self[-other:]
# a = Nstr("I love FishC.com!")
# print(a << 3)
# print(a >> 3)

#计算字符窜的ASCII码
# class Nstr(str):
# 	def __init__(self, string=''):
# 		if isinstance(string, str):
# 			self.total = 0
# 			for each in string:
# 				self.total += ord(each)
# 		else:
# 			pirnt('参数错误!')

# 	def __sub__(self, other):
# 		return self.total - other.total
# 	def __add__(self, other):
# 		return self.total + other.total
# 	def __mul__(self, other):
# 		return self.total * other.total
# 	def __floordiv__(self, other):
# 		return self.total // other.total
# 	def __truediv__(self, other):
# 		return self.total / other.total
class Nstr(int):
	def __new__(cls, arg=0):
		if isinstance(arg, str):
			total = 0
			for each in arg:
				total += ord(each)
			arg = total
		return int.__new__(cls, arg)

a = Nstr("FishC")
b = Nstr("love")
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)