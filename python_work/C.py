# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-11-06 17:38:37
# @Last Modified by:   take
# @Last Modified time: 2017-11-06 17:55:14
class C:
	def __init__(self, *arg):
		if not len(arg):
			print("并没有传入参数")
		else:
			print("传入了 %d 个参数,分别是:" % (len(arg)), end = " ")
			print(*arg)

test = C()
test = C(1, 2, 3)