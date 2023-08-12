import pygame
from random import randint
from pygame.locals import *
clock=pygame.time.Clock()
pygame.init()
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("HI THERE")
while True:
    pygame.draw.rect(screen,(randint(0,255),randint(0,255),randint(0,255)),(0,0,900,900))
    # clock.tick(30)
    # pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(450,450),450,100)
    # clock.tick(30)
    # pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(450,450),350,100)
    # clock.tick(30)
    # pygame.draw.circle(screen,(randint(0,255),randint(0,255),randint(0,255)),(450,450),250)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()