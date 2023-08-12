import pygame
from random import randint
from pygame.locals import *
pygame.init()

clock=pygame.time.Clock()
screen=pygame.display.set_mode((3000,800))
pygame.display.set_caption("HI THERE")
while True:
    pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(0,0,1500,1500))
    clock.tick(30)
    pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(750,750),750,100)
    clock.tick(30)
    pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(750,750),650,100)
    clock.tick(30)
    pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(750,750),550,250)
    clock.tick(30)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()