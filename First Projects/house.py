import pygame
from random import randint
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((900,900))
clock=pygame.time.Clock()
pygame.display.set_caption("HI THERE")
while True:
    pygame.display.update()
    pygame.draw.rect(screen,(255,255,255),(450,450,300,300))
    pygame.draw.polygon(screen,(0,255,0),[[450,450],[600,300],[750,450]])
    pygame.draw.circle(screen,(0,0,255),(600,600),100)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()