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
cords=(0,0)
colors=((255,255,255),(255,0,0))
index=[0,1]
while True:
    screen.fill((0,0,0))
    button=pygame.draw.rect(screen,colors[index[0]],(350,350,100,100))
    mouse=pygame.Rect(cords[0],cords[1],10,10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEMOTION:
            cords=event.pos
        if event.type==MOUSEBUTTONDOWN:
            if pygame.Rect.colliderect(button,mouse):
                index.reverse()