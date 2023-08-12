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
movex=0
movey=0
name="moving square"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    if movex+50<=screenwidth:
        pygame.draw.rect(screen,color(),(movex,movey,50,50))
        time.sleep(0.1)
    else:
        movex=0
        movey+=50
    pygame.display.update()
    movex+=50
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()