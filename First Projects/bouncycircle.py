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
# text
def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))


pygame.init()
screenwidth=900
screenheight=900
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x=50
y=450
step=10
while True:
    pygame.display.update()
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(0,255,0),(x,y),50)
    x+=step
    if x>850:
        step=-step
    if x<50:
        step=-step
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()