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
topleft=(0,0)
width=0
height=0
bottomright=0
x=0
y=0
down=False
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
prev=[]
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type == MOUSEBUTTONDOWN:
            topleft=event.pos
            down=True
        if event.type==MOUSEBUTTONUP:
            down=False
            prev.append((x,y,width,height))
    if down==True:
        bottomright=event.pos
    if topleft!=bottomright!=0:
        x=topleft[0]
        y=topleft[1]
        width=bottomright[0]-x
        height=bottomright[1]-y
        if width<0:
            x=bottomright[0]
            width=-width
        if height<0:
            y=bottomright[1]
            height=-height
    screen.fill((0,0,0))
    pygame.draw.rect(screen,color(),(x,y,width,height),5)
    for z in prev:
        pygame.draw.rect(screen,color(),z,5)