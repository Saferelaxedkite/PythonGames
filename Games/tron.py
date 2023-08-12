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
name="TRON"
score=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
snakex=680
snakey=680
snakepos=[(snakex,snakey)]
snakex1=0
snakey1=0
snakepos1=[(snakex1,snakey1)]
direction=""
direction1=""
canmove=False
gameover=False
while True:
    key=pygame.key.get_pressed()
    if key[K_SPACE] and direction==direction1=="":
        direction="up"
        direction1="down"
        canmove=True
    if direction != "":
        snakepos.append((snakex,snakey))
    if direction1 != "":
        snakepos1.append((snakex1,snakey1))
    if gameover==False:
        clock.tick(15)
        screen.fill((0,255,0))
        for a in range(0,45):
            for b in range(0,45):
                pygame.draw.rect(screen,(255,255,255),(a*20,b*20,20,20),1)
        snakepos.pop()
        snakepos.insert(0,(snakex,snakey))
        snakepos1.pop()
        snakepos1.insert(0,(snakex1,snakey1))
        for x in snakepos:
            snake=pygame.draw.rect(screen,(0,0,255),x+(20,20))
        for y in snakepos1:
            snake1=pygame.draw.rect(screen,(255,0,0),y+(20,20))
        if direction=="right":
            snakex+=20
        elif direction=="left":
            snakex-=20
        elif direction=="up":
            snakey-=20
        elif direction=="down":
            snakey+=20
        if key[K_RIGHT] and direction != "left" and canmove==True:
            direction="right"
        if key[K_LEFT] and direction != "right" and canmove==True:
            direction="left"
        if key[K_UP] and direction != "down" and canmove==True:
            direction="up"
        if key[K_DOWN] and direction != "up" and canmove==True:
            direction="down"


        if direction1=="right":
            snakex1+=20
        if direction1=="left":
            snakex1-=20
        if direction1=="up":
            snakey1-=20
        if direction1=="down":
            snakey1+=20
        if key[K_d] and direction1 != "left" and canmove==True:
            direction1="right"
        if key[K_a] and direction1 != "right" and canmove==True:
            direction1="left"
        if key[K_w] and direction1 != "down" and canmove==True:
            direction1="up"
        if key[K_s] and direction1 != "up" and canmove==True:
            direction1="down"
        if snakepos[0] in snakepos[2:]or snakepos[0] in snakepos1[0:]:
            show_text("Red WINS!!!!!",150,350,(0,0,0),50)
            gameover=True
        if snakex in (-20,700) or snakey in (-20,700):
            show_text("Red WINS!!!!!",150,350,(0,0,0),50)
            gameover=True
        if snakepos1[0] in snakepos1[2:]or snakepos1[0] in snakepos[0:]:
            show_text("Blue WINS!!!!!",150,350,(0,0,0),50)
            gameover=True
        if snakex1 in (-20,700) or snakey1 in (-20,700):
            show_text("Blue WINS!!!!!",150,350,(0,0,0),50)
            gameover=True
        pygame.display.update()
    if key[pygame.K_r]:
        snakepos=[]
        snakepos1=[]
        snakex=680
        snakey=680
        snakepos=[(snakex,snakey)]
        snakex1=0
        snakey1=0
        snakepos1=[(snakex1,snakey1)]
        direction=""
        direction1=""
        canmove=False
        gameover=False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()