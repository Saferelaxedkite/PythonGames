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
points=[]
counter=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONDOWN and counter!=2:
            points.append(list(event.pos))
            pygame.draw.circle(screen,(255,255,255),event.pos,5)
            counter+=1
        if counter==2:
            pygame.draw.line(screen,(255,255,255),points[0],points[1],5)
            pygame.display.update()
            counter=0
            points=[]