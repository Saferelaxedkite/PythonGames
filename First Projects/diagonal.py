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
screenwidth=700
screenheight=700
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x=0
up=True
while True:
    pygame.display.update()
    time.sleep(0.1)
    if up==True:
        pygame.draw.circle(screen,color(),(x,x),30)
        x+=20
        if x==screenwidth:
            up=False
    elif up==False:
        pygame.draw.circle(screen,color(),(x,x),30)
        x-=20
        if x==0:
            up=True
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()