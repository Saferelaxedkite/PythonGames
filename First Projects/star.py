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
cords=((150,400),(550,275),(125,275),(550,400),(350,150))
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    pygame.display.update()
    for x in range(0,len(cords)):
        y=x+1
        if x==len(cords)-1:
            y=0
        pygame.draw.line(screen,color(),cords[x],cords[y],3)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()