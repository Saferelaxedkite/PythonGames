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
move=0
name="wagon"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    if move==screenwidth:
        move=0
    pygame.display.update()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(79, 74, 66),(move+50,100,200,100))
    pygame.draw.circle(screen,(79, 74, 66),(move+50,200),50)
    pygame.draw.circle(screen,(79, 74, 66),(move+250,200),50)
    move+=10
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()