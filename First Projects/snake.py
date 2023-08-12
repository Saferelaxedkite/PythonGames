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

def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))


pygame.init()
screenwidth=1430
screenheight=800
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
x=0
y=0
step=10
enemy_x=500
gameover=False
pygame.display.set_caption(name)
while True:
    player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
    key_input=pygame.key.get_pressed()
    pygame.display.update()
    screen.fill((0,255,0))
    if gameover==False:
        if key_input[pygame.K_LEFT] and x!=0:
            x -= step
        if key_input[pygame.K_UP] and y!=0:
            y -= step
        if key_input[pygame.K_RIGHT] and x!=screenwidth-100:
            x += step
        if key_input[pygame.K_DOWN] and y!=screenheight-100:
            y += step