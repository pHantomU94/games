import pygame
import sys

pygame.init()  # 初始化pygame

size = width, height = 640,480    # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口
color = (0,0,0)
ball = pygame.image.load('D:/project/game/test/images/ball.png')
ballrect = ball.get_rect()

speed = [5,5]
clock =pygame.time.Clock()

while True:  # 死循环确保窗口一直显示
    clock.tick(60)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            pygame.display.quit()
            sys.exit(0)
    # 碰到左右边缘
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill(color)
    screen.blit(ball,ballrect)
    pygame.display.flip()
            


pygame.quit()
