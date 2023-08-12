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
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
move1=0
move2=900
up1=True
up2=True
while True:
    pygame.display.update()
    screen.fill((0,0,0))
    x=pygame.draw.circle(screen,(255,255,255),(move1,450),51)
    y=pygame.draw.circle(screen,(0,255,0),(move2,450),51)
    if x.colliderect(y):
        print("sdjfkhsdkjfhsdkjfhjksdhfkjsdhfjksdh")
    if up1==False:
        move1-=10
        if move1==50:
            up1=True
    if up1==True:
        move1+=10
        if move1==400:
            up1=False
    if up2==False:
        move2+=10
        if move2==850:
            up2=True
    if up2==True:
        move2-=10
        if move2==500:
            up2=False
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()