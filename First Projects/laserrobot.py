import pygame
from random import randint
from pygame.locals import *
# color generator
def color():
    colors=[]
    for x in range(0,3):
        colors.append(randint(0,255))
    return tuple(colors)


pygame.init()
screenwidth=900
screenheight=900
name="laser robot"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x=0
y=0
while True:
    pygame.display.update()
    # face
    pygame.draw.rect(screen,(110, 106, 106),(x+200,y+100,500,250))
    # eyes
    pygame.draw.circle(screen,(255,0,0),(x+350,y+250),50)
    pygame.draw.circle(screen,(255,0,0),(x+550,y+250),50)
    # neck
    pygame.draw.rect(screen,(110, 106, 106),(x+325,y+350,250,100))
    # body
    pygame.draw.rect(screen,(110, 106, 106),(x+175,y+450,550,150))
    # legs
    pygame.draw.rect(screen,(110, 106, 106),(x+175,y+450,100,250))
    pygame.draw.rect(screen,(110, 106, 106),(x+725,y+450,100,250))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()