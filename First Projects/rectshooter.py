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
screenwidth=700
screenheight=700
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
x=0
y=600
bulletx=0
bullety=600
step=5
fire=False
pygame.display.set_caption(name)
while True:
    if fire==True:
        bullety-=10
    if bullety==0:
        bullety=600
        bulletx=x+25
        fire=False
    pygame.display.update()
    screen.fill((0,0,0))
    gun=pygame.draw.rect(screen,(255,255,255),(x,y,50,100))
    bullet=pygame.draw.rect(screen,(255,0,0),(bulletx,bullety,30,30))
    key=pygame.key.get_pressed()
    if key[pygame.K_LEFT]and x!=0:
        x-=step
        if fire==False:
            bulletx-=step
    if key[pygame.K_RIGHT] and x!=650:
        x+=step
        if fire==False:
            bulletx+=step
    if key[pygame.K_SPACE] and fire==False:
        fire=True
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()