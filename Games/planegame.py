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
# text
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))


pygame.init()
screenwidth=900
screenheight=900
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
bulletx=125
bullety=470
x=100
y=450
fire=False
while True:
    fire=False
    screen.fill((0,0,0))
    keypress=pygame.key.get_pressed()
    player=pygame.draw.rect(screen,(255,255,255),(x,y,50,50))
    bullet=pygame.draw.rect(screen,(255,0,0),(bulletx,bullety,10,10))
    pygame.display.update()
    if fire==True:
        bulletx+=25
    if keypress[pygame.K_UP] and y>=0:
        y-=10
        if fire==False:
            bullety-=10
    if keypress[pygame.K_DOWN] and y<=800:
        y+=10
        if fire==False:
            bullety+=10
    if keypress[pygame.K_SPACE]:
        fire=True
        if bulletx>=900:
            fire=False
            bulletx=x
            bullety=y+25
        