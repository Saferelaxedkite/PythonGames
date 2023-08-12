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
cords=[]
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
colors=[color(),color()]
colors.reverse()
for x in range(0,10000):
        cords.append([randint(0,900),randint(0,900)])
while True:
    key=pygame.key.get_pressed()
    pygame.display.update()
    # screen.fill((0,0,0))
    if key[K_SPACE]:
        colors.reverse()
    for x in cords:
        pygame.draw.circle(screen,(colors[0]),(x[0],x[1]),3)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()