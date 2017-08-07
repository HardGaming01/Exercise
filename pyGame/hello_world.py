# -*- coding: utf-8 -*-
import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((770, 433), 0, 32)
# 设置窗口
pygame.display.set_caption("Hello World")
# 设置标题
background = pygame.image.load("img.jpg").convert()
# 加载图片
while True:
    # 主循环
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # 接收退出事件
            pygame.quit()
            exit()
    screen.blit(background, (0, 0))
    pygame.display.update()
