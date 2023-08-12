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
clickcount=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
colorz=(255,255,255)
pygame.display.set_caption(name)
while True:
    pygame.draw.circle(screen,colorz,(450,450),100)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONDOWN:
            clickcount+=1
            if 350<=event.pos[0]<=550 and 350<=event.pos[1]<=550 and clickcount%2==0:
                colorz=color()