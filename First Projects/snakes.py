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
name="Moving Circle"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x=0
y=0
sidestep=10
previous=""
side=True
up=False
pygame.display.set_caption(name)
while True:
    x+=sidestep
    player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
    if x>=900:
        x=0.1
    if x<=0:
        x=899
    pygame.display.update()
    screen.fill((0,255,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            sidestep=-sidestep