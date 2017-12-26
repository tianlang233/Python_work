# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-10-14 13:15:23
# @Last Modified by:   take
# @Last Modified time: 2017-11-04 13:36:19
class Stack:
	def __init__(self, start=[]):
		self.stack = []
		for x in start:
			self.stack.push(x)

	def isEmpty(self):
		return not self.stack

	def push(self, obj):
		self.stack.append(obj)

	def pop(self):
		if not self.stack:
			print("警告：栈为空！")
		else:
			return self.stack.pop()

	def bottom(self):
		if not self.stack:
			print("警告：栈为空！")
		else:
			return self.stack[0]

	def top(self):
		if not self.stack:
			print("警告：栈为空！")
		else:
			return self.stack[-1]

