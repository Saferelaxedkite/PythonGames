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
x=450
y=450
step=10
pygame.display.set_caption(name)
while True:
    key_input=pygame.key.get_pressed()
    pygame.display.update()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,255,255),(x,y,100,100))
    if key_input[pygame.K_LEFT] and x!=0:
        x -= step
    if key_input[pygame.K_UP] and y!=0:
        y -= step
    if key_input[pygame.K_RIGHT] and x!=screenwidth-100:
        x += step
    if key_input[pygame.K_DOWN] and y!=screenheight-100:
        y += step
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()