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
def show_text(msg, x, y, color, size,screen):
    fontobj= pygame.font.SysFont('comic_sans', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

def menu():
    pygame.init()
    screenwidth=900
    screenheight=900
    name="MENU"
    cords=(0,0)
    screen=pygame.display.set_mode((screenwidth,screenheight))
    clock=pygame.time.Clock()
    rightpower=0
    leftpower=0
    rightcontrol=0
    leftcontrol=0
    pygame.display.set_caption(name)
    while True:
        screen.fill((0,0,0))
        show_text("ERIC'S GAMES",250,700,(0,0,0),50,screen)
        mouse=pygame.Rect(cords[0],cords[1],8,8)
        flappybirdbutton=pygame.draw.rect(screen,(255,0,0),(100,100,200,200))
        show_text("FLAPPY BIRD",110,150,(0,0,0),25,screen)
        snakebutton=pygame.draw.rect(screen,(0,255,0),(350,100,200,200))
        show_text("SNAKE",400,150,(0,0,0),25,screen)
        pongbutton=pygame.draw.rect(screen,(0,0,255),(600,100,200,200))
        show_text("PONG",650,150,(0,0,0),25,screen)
        bombbutton=pygame.draw.rect(screen,(255,100,0),(100,350,200,200))
        show_text("BOMB",150,400,(0,0,0),25,screen)
        tronbutton=pygame.draw.rect(screen,(255,200,0),(350,350,200,200))
        show_text("TRON",400,400,(0,0,0),25,screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEMOTION:
                cords=event.pos
            if event.type==MOUSEBUTTONDOWN:
                if pygame.Rect.colliderect(mouse,flappybirdbutton):
                    flappy_bird()
                elif pygame.Rect.colliderect(mouse,snakebutton):
                    snake()
                elif pygame.Rect.colliderect(mouse,pongbutton):
                    pong()
                elif pygame.Rect.colliderect(mouse,bombbutton):
                    bombdodge()
                elif pygame.Rect.colliderect(mouse,tronbutton):
                    tron()
def play():
    pygame.init()
    screenwidth=1400
    screenheight=800
    name="Pong"
    scores=[0,15,30,40,"AD","GAME"]
    rightpaddlex=screenwidth-100
    leftpaddlex=50
    rightpaddley=screenheight/2-50
    leftpaddley=screenheight/2-50
    rightpower=17
    leftpower=17
    rightcontrol=20
    leftcontrol=20
    ballx=screenwidth/2
    bally=screenheight/2
    ballangle=0
    rightscore=0
    leftscore=0
    gameover=False
    rightgames=0
    leftgames=0
    ballspeed=(abs(rightpower+leftpower))//2
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
            show_text(str(leftgames),screenwidth/2-50,100,(0,0,0),50,screen)
            show_text(str(scores[leftscore]),50,50,(0,0,0),30,screen)
            show_text(str(rightgames),screenwidth/2+50,100,(0,0,0),50,screen)
            show_text(str(scores[rightscore]),screenwidth-50,50,(0,0,0),30,screen)
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
                show_text("Red Wins!",screenwidth/2-100,300,(255,0,0),50,screen)
            if leftgames>=6 and leftgames-rightgames>=2:
                gameover=True
                show_text("Green Wins!",screenwidth/2-100,300,(0,255,0),50,screen)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        if key[pygame.K_r]:
            gameover=False
            bally=450
            ballx=400
            ballspeed=25
            ballangle=0
            rightpaddle=400
            leftpaddle=400
            leftscore=0
            rightscore=0
            rightgames=0
            leftgames=0
        if key[pygame.K_b]:
            menu()
            pygame.display.update()
play()