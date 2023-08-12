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
changewrong=True
wrong=0
door1=pygame.draw.rect(screen,(255,255,255),(350,350,200,300))
door2=pygame.draw.rect(screen,(255,255,255),(50,350,200,300))
door3=pygame.draw.rect(screen,(255,255,255),(650,350,200,300))
lst=[door1,door2,door3]
choice=""
dead=False
score=0
bgcolor=(255,255,255)
while True:
    if changewrong==True:
        wrong=lst[randint(0,2)]
        changewrong=False
    if dead==False:
        screen.fill(bgcolor[0])
        door1=pygame.draw.rect(screen,(255,255,255),(350,350,200,300))
        door2=pygame.draw.rect(screen,(255,255,255),(50,350,200,300))
        door3=pygame.draw.rect(screen,(255,255,255),(650,350,200,300))
    mouse=pygame.Rect(cords[0],cords[1],10,10)
    show_text(str(score),400,100,(255,255,255),30)
    pygame.display.update()
    if pygame.Rect.colliderect(mouse,wrong):
        bgcolor=(0,0,0)
    else:
        bgcolor=(255,255,255)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEMOTION:
            cords=event.pos
        if event.type==MOUSEBUTTONDOWN:
            if pygame.Rect.colliderect(door1,mouse):
                choice=door1
            elif pygame.Rect.colliderect(door2,mouse):
                choice=door2
            elif pygame.Rect.colliderect(door3,mouse):
                choice=door3
        if wrong!=choice and choice!="":
            choice=""
            changewrong=True
            score+=1
        elif wrong==choice and choice!="":
            screen.fill((255,0,0))
            show_text("You Died.",350,350,(0,0,0),50)
            dead=True