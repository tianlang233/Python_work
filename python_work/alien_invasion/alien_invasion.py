# -*- coding: utf-8 -*-
# @Author: take
# @Date:   2017-10-22 21:24:50
# @Last Modified by:   take
# @Last Modified time: 2017-10-22 21:31:07
import sys
import pygame

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()
	screen = pygame.display.set_mode((1200, 800))
	pygame.display.set_caption("Alien Invasion")

	#设置背景色
	bg_color = (230, 230, 230)

	#开始游戏的主循环
	while True:

		#监视键盘和鼠标事件
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

		#每次循环时都重绘屏幕
		screen.fill(bg_color)
		#让最近绘制的屏幕可见
		pygame.display.flip()

run_game()