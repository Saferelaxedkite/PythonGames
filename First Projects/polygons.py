import pygame
from random import randint
from pygame.locals import *
pygame.init()
screenwidth=900
screenheight=900
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    pygame.draw.polygon(screen,(randint(0,255),randint(0,255),randint(0,255)),[[100,9],[100,400],[300,800]])
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()