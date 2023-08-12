import pygame
from random import randint
from pygame.locals import *
# color generator
def color():
    colors=[]
    for x in range(0,3):
        colors.append(randint(0,255))
    return tuple(colors)

# two colors
pygame.init()
screenwidth=1300
screenheight=1300
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    pygame.display.update()
    colors=[(255,255,255),(70, 92, 67)]
    for y in range(0,screenwidth,100):   
        for x in range(0,screenwidth,100):
            colors.reverse()
            pygame.draw.rect(screen,colors[0],(x,y,100,100))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()