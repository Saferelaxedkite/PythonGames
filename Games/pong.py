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
screenwidth=1400
screenheight=800
name="Pong"
scores=[0,15,30,40,"AD","GAME"]
rightpaddlex=screenwidth-100
leftpaddlex=50
rightpaddley=screenheight/2-50
leftpaddley=screenheight/2-50
rightpower=15
leftpower=15
rightcontrol=15
leftcontrol=15
ballx=screenwidth/2
bally=screenheight/2
ballangle=0
rightscore=0
leftscore=0
gameover=False
rightgames=0
leftgames=0
ballspeed=10
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
rightstep=17
leftstep=17
counter=0
changeserve=True
pygame.display.set_caption(name)
while True:
    if changeserve==True:
        if counter%2==0:
            ballspeed=abs(ballspeed)
        else:
            ballspeed=-1*abs(ballspeed)
        changeserve=False
    key=pygame.key.get_pressed()
    if gameover==False:
        screen.fill((34, 78, 199))
        pygame.draw.line(screen,(255,255,255),(screenwidth/2,0),(screenwidth/2,800),5)
        ball=pygame.draw.circle(screen,(52, 209, 17),(ballx,bally),25)
        right=pygame.draw.rect(screen,(255,0,0),(rightpaddlex,rightpaddley,50,150))
        left=pygame.draw.rect(screen,(0,255,0),(leftpaddlex,leftpaddley,50,150))
        show_text(str(leftgames),screenwidth/2-50,100,(0,0,0),50)
        show_text(str(scores[leftscore]),50,50,(0,0,0),30)
        show_text(str(rightgames),screenwidth/2+50,100,(0,0,0),50)
        show_text(str(scores[rightscore]),screenwidth-50,50,(0,0,0),30)
        ballx+=ballspeed
        bally+=ballangle
        #collide
        if pygame.Rect.colliderect(ball,right):
            ballspeed=-rightpower
            ballangle=randint(-rightcontrol,rightcontrol)
            ballx=rightpaddlex-50
        elif pygame.Rect.colliderect(ball,left):
            ballspeed=leftpower
            ballx=leftpaddlex+100
            ballangle=randint(-leftcontrol,leftcontrol)
        #controls
        if key[pygame.K_UP] and rightpaddley>=0:
            rightpaddley-=rightstep
        if key[pygame.K_DOWN] and rightpaddley<=screenheight-150:
            rightpaddley+=rightstep
        if key[pygame.K_LEFT] and rightpaddlex>=screenwidth/2+50:
            rightpaddlex-=rightstep
        if key[pygame.K_RIGHT] and rightpaddlex<screenwidth-100:
            rightpaddlex+=rightstep
        if key[pygame.K_w] and leftpaddley>=0:
            leftpaddley-=leftstep
        if key[pygame.K_s] and leftpaddley<=screenheight-150:
            leftpaddley+=leftstep
        if key[pygame.K_d] and leftpaddlex<screenwidth/2-100:
            leftpaddlex+=leftstep
        if key[pygame.K_a] and leftpaddlex>50:
            leftpaddlex-=leftstep
        if bally<=0 or bally>=800:
            ballangle=-ballangle
        #reset
        if ballx<=0:
            ballx=screenwidth/2
            bally=screenheight/2
            ballangle=0
            rightpaddlex=screenwidth-100
            leftpaddlex=50
            rightpaddley=screenheight/2-50
            leftpaddley=screenheight/2-50
            changeserve=True
            if scores[leftscore]=="AD":
                leftscore-=1
            else:
                rightscore+=1
            pygame.display.update()
            pygame.time.delay(1000)
        elif ballx>=screenwidth:
            ballx=screenwidth/2
            bally=screenheight/2
            ballangle=0
            rightpaddlex=screenwidth-100
            leftpaddlex=50
            rightpaddley=screenheight/2-50
            leftpaddley=screenheight/2-50
            changeserve=True
            if scores[rightscore]=="AD":
                rightscore-=1
            else:
                leftscore+=1
            pygame.display.update()
            pygame.time.delay(1000)
        #win
        if rightscore>=4 and rightscore-leftscore>=2:
            rightgames+=1
            rightscore=0
            leftscore=0
            changeserve=True
            counter+=1
        if leftscore>=4 and leftscore-rightscore>=2:
            leftgames+=1
            rightscore=0
            leftscore=0
            counter+=1
            changeserve=True
        if rightgames>=6 and rightgames-leftgames>=2:
            gameover=True
            show_text("Red Wins!",screenwidth/2-100,300,(255,0,0),50)
        if leftgames>=6 and leftgames-rightgames>=2:
            gameover=True
            show_text("Green Wins!",screenwidth/2-100,300,(0,255,0),50)
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    if key[pygame.K_r]:
        gameover=False
        bally=450
        ballx=400
        ballspeed=15
        ballangle=0
        rightpaddle=400
        leftpaddle=400
        leftscore=0
        rightscore=0
        rightgames=0
        leftgames=0
        pygame.display.update()