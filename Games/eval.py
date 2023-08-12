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
x=450
y=450
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
show=1
cords=(0,0)
canmove=True
change=True
step=10
colors=(0,0,0)
while True:
    screen.fill((255,255,255))
    pygame.draw.circle(screen,colors,(x,450),50)
    if x>=900 or x<=0:
        step=-step
        colors=color()
    x+=step
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEMOTION:
            if canmove==True:
                cords=event.pos