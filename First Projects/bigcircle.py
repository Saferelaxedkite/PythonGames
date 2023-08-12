import pygame
from random import randint
from pygame.locals import *
import time
# color generator
def color():
    colors=[]
    for x in range(0,3):
        colors.append(randint(0,255))
    return tuple(colors)


pygame.init()
screenwidth=900
screenheight=900
name="big circle"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x=0
up=True
while True:
    pygame.display.update()
    screen.fill((0,0,0))
    clock.tick(30)
    if up==True:
        if x>=screenwidth/2:
            up=False
        pygame.draw.circle(screen,color(),(450,450),x,200)
        x+=10
    elif up==False:
        pygame.draw.circle(screen,color(),(450,450),x,200)
        x-=10
        if x<=0:
            up=True
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    