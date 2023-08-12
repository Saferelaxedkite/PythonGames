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
long=0
def show_text(msg, x, y, color, size):
    global long
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
    long=msgobj.get_width()

pygame.init()
screenwidth=900
screenheight=900
y=0
name="HI"
text=""
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    pygame.display.update()
    screen.fill((0,0,0))
    show_text(text,0,y,(255,255,0),50)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            key=pygame.key.get_pressed()
            if key[pygame.K_BACKSPACE] and len(text)!=0:
               text1=list(text)
               text1.pop() 
               text="".join(text1)
            else:
                text+=(chr(event.key))
            if long>=850:
                text+="\n"