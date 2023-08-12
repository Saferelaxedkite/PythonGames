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
    fontobj= pygame.font.SysFont('comic_sans', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))


pygame.init()
screenwidth=900
screenheight=800
name="Pong"
rightpaddle=350
leftpaddle=350
ballx=450
bally=450
ballspeed=10
ballangle=0
rightscore=0
leftscore=0
gameover=False
length=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
while True:
    if gameover==False:
        key=pygame.key.get_pressed()
        key1=pygame.key.get_pressed()
        screen.fill((0,200,35))
        pygame.draw.line(screen,(0,0,0),(450,0),(450,800),5)
        show_text(str(leftscore),100,100,(0,0,0),50)
        show_text(str(rightscore),800,100,(0,0,0),50)
        ball=pygame.draw.circle(screen,(255,255,255),(ballx,bally),25)
        right=pygame.draw.rect(screen,(255,0,0),(800,rightpaddle,50,200))
        left=pygame.draw.rect(screen,(255,0,0),(50,leftpaddle,50,200))
        ballx+=ballspeed
        bally+=ballangle
        if bally>leftpaddle+100:
            leftpaddle+=10
        if bally<leftpaddle+100:
            leftpaddle-=10
        if pygame.Rect.colliderect(ball,right):
            ballspeed=-ballspeed
            ballangle=randint(-10,10)
            ballx=750
            length+=1
        elif pygame.Rect.colliderect(ball,left):
            ballspeed=-ballspeed
            ballangle=randint(-10,10)
            ballx=150
        if key[pygame.K_UP] and rightpaddle!=0:
            rightpaddle-=10
        elif key[pygame.K_DOWN] and rightpaddle!=600:
            rightpaddle+=10
        if bally<=0 or bally>=800:
            ballangle=-ballangle
        if ballx==0:
            rightscore+=1
            ballx=400
            bally=450
            ballspeed=-10
            ballangle=0
            rightpaddle=400
            leftpaddle=400
            pygame.display.update()
            pygame.time.delay(1000)
        elif ballx==900:
            leftscore+=1
            bally=450
            ballx=400
            ballspeed=10
            ballangle=0
            rightpaddle=400
            leftpaddle=400
            pygame.display.update()
            pygame.time.delay(1000)
            print(length)
        if rightscore==11:
            gameover=True
            show_text(str(leftscore),100,100,(0,0,0),50)
            show_text(str(rightscore),800,100,(0,0,0),50)
        elif leftscore==11:
            gameover=True
            show_text(str(leftscore),100,100,(0,0,0),50)
            show_text(str(rightscore),800,100,(0,0,0),50)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()