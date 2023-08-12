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
name="Dodge the Bombs!"
canmove=True
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
step=10
lane=1
lanes=[(100,700),(700,700)]
previous=""
changex=True
bomby=-350
gameover=False
gamestart=False
x=400
y=700
lives=3
canhurt=True
score=0
pygame.display.set_caption(name)
while True:
    show_text(f"LIVES:{lives}",750,50,(0,0,0),30)
    show_text(f"SCORE:{score}",500,50,(0,0,0),30)
    key_input=pygame.key.get_pressed()
    if gameover==False:
        if changex==True:
            bombx=randint(0,800)
            changex=False
        player=pygame.draw.rect(screen,(255,0,0),(x,y,50,50))
        bomb=pygame.draw.rect(screen,(0,0,0),(bombx-25,bomby,100,100))
        pygame.display.update()
        screen.fill((161,123,48))
        if gamestart==True:
            bomby+=40
            if key_input[pygame.K_LEFT]and x>0:
                x-=7
            if key_input[pygame.K_RIGHT]and x<850:
                x+=7
        else:
            show_text("Press SPACE to start.",200,400,(0,0,0),50)
        if key_input[pygame.K_SPACE]:
            gamestart=True
        if pygame.Rect.colliderect(player, bomb) and canhurt==True:
            lives-=1
            canhurt=False
        if bomby>=900:
            bomby=-350
            changex=True
            canhurt=True
            score+=1
        if lives<=0:
            gameover=True
            show_text("KABOOM!",150,250,(255,0,0),70)
            show_text("OH NO! A bomb fell on you! :( Press R to restart.",150,350,(0,0,0),30)
            show_text(f"LIVES:{lives}",750,50,(0,0,0),30)
            show_text(f"SCORE:{score}",500,50,(0,0,0),30)
            pygame.display.update()
    if key_input[K_r]:
        if gameover==True:
            gameover=False
            gamestart=False
            bomby=-350
            bombx=randint(0,800)
            lives=3
            score=0
            x=400
            y=700
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()