# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-11-28 22:28:42
# @Last Modified by:   take
# @Last Modified time: 2017-11-28 23:25:49

for i in range(3163, 10001):
	num = i ** 2
	result = num
	#通过地板除法和取余获得各位数
	num_list = []
	while num:
		num_list.append(num % 10)
		num = num // 10
	org = 0 #检测各位数字是否相等
	for each in num_list:
		if (num_list.count(each) != 1):
			org = 1
	if org == 0:
		a1 = num_list[1] + num_list[3] + num_list[5] + num_list[7]
		a2 = num_list[0] + num_list[2] + num_list[4] + num_list[6]
		if a1 == a2:
			print(result)
