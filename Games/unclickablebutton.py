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
cords=[0,0]
win=False
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    if win==False:
        x=cords[0]+100
        y=cords[1]+100
        screen.fill((0,0,0))
        mouse=pygame.Rect(cords[0],cords[1],10,10)
        button=pygame.draw.rect(screen,color(),(cords[0]+10,cords[1]+10,200,50))
        pygame.display.update()
    else:
        show_text("You Won! Wait... How?",350,350,(255,255,255),30)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEMOTION:
            cords=event.pos
        if event.type==MOUSEBUTTONDOWN:
            if pygame.Rect.colliderect(mouse,button):
                win=True