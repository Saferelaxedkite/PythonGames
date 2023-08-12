import pygame
from random import randint
from pygame.locals import *
import time
# color generator
def color():
    colors=[]
    for x1 in range(0,3):
        colors.append(randint(0,255))
    return tuple(colors)


pygame.init()
screenwidth=700
screenheight=700
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x1=600
y=0
x=0
up=True
up1=True
while True:
    pygame.display.update()
    time.sleep(0.1)
    screen.fill((0,0,0))
    if up1==True:
        pygame.draw.rect(screen,color(),(x1,y,100,100))
        x1-=100
        y+=100
        if x1==0:
            up1=False
    elif up1==False:
        pygame.draw.rect(screen,color(),(x1,y,100,100))
        x1+=100
        y-=100
        if x1==screenwidth:
            up1=True
    

    
    pygame.display.update()
    screen.fill((0,0,0))
    if up==True:
        pygame.draw.rect(screen,color(),(x,x,100,100))
        x+=100
        if x==screenwidth:
            up=False
    elif up==False:
        pygame.draw.rect(screen,color(),(x,x,100,100))
        x-=100
    if x==0:
        up=True
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()