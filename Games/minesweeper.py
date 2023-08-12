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
screenwidth=700
screenheight=700
name="Minesweeper"
cords=(0,0)
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
tiles=[[]]
gridcolor=[(167,122,52),(95,81,60)]
mouse=pygame.Rect(cords[0],cords[1],10,10)
for y in range(0,7):
    for x in range(0,7):
        gridcolor.reverse()
        draw=(screen,gridcolor[0],(100*x,100*y,100,100))
        pygame.draw.rect(screen,gridcolor[0],(100*x,100*y,100,100))
        tiles[0].append(draw)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEMOTION:
            cords=event.pos