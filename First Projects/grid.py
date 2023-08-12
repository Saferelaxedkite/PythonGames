import pygame
from random import randint
from pygame.locals import *
import time
def color():
    colors=[]
    for x in range(0,3):
        colors.append(randint(0,255))
    return colors


pygame.init()
screenwidth=1700
screenheight=1700
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption("HI THERE")
x=0
up=True
while True:
    pygame.display.update()
    for x in range(0,1700,2):
        pygame.draw.line(screen,color(),[x,0],[x,1700],1)
    for y in range(0,1700,2):
        pygame.draw.line(screen,color(),[0,y],[1700,y],1)
    if up==True:
        if x>=screenwidth/2:
            up=False
        pygame.draw.circle(screen,color(),(450,450),x,300)
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
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()

    