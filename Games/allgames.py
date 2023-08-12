import pygame
from random import randint
from pygame.locals import *
import time
# text
def show_text(msg, x, y, color, size,screen):
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))
def color():
    colors=[]
    for x in range(0,3):
        colors.append(randint(0,255))
    return tuple(colors)
def menu():
    pygame.init()
    screenwidth=900
    screenheight=900
    name="MENU"
    cords=(0,0)
    screen=pygame.display.set_mode((screenwidth,screenheight))
    clock=pygame.time.Clock()
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
def snake():
    pygame.init()
    size=5
    screenwidth=700
    screenheight=700
    name="SNAKE"
    score=0
    screen=pygame.display.set_mode((screenwidth,screenheight))
    clock=pygame.time.Clock()
    pygame.display.set_caption(name)
    foodx=(randint(0,700)//size)*size
    foody=(randint(0,700)//size)*size
    snakex=(randint(0,700)//size)*size
    snakey=(randint(0,700)//size)*size
    snakepos=[(snakex,snakey)]
    direction=""
    gameover=False
    while True:
        key=pygame.key.get_pressed()
        if gameover==False:
            screen.fill((0,255,0))
            for a in range(0,700//size):
                for b in range(0,700//size):
                    pygame.draw.rect(screen,(255,255,255),(a*size,b*size,size,size),1)
            clock.tick(15)
            show_text(str(score),400,10,(0,0,0),30,screen)
            snakepos.pop()
            snakepos.insert(0,(snakex,snakey))
            for x in snakepos:
                snake=pygame.draw.rect(screen,(0,0,255),x+(size,size))
            if direction=="right":
                snakex+=size
            elif direction=="left":
                snakex-=size
            elif direction=="up":
                snakey-=size
            elif direction=="down":
                snakey+=size
            if key[K_RIGHT] and direction != "left":
                direction="right"
            elif key[K_LEFT] and direction != "right":
                direction="left"
            elif key[K_UP] and direction != "down":
                direction="up"
            elif key[K_DOWN] and direction != "up":
                direction="down"
            food=pygame.draw.rect(screen,(255,0,0),(foodx,foody,size,size))
            if snakex==foodx and snakey==foody:
                foodx=(randint(0,700)//size)*size
                foody=(randint(0,700)//size)*size
                score+=1
                snakepos.append((snakex,snakey))
            if snakepos[0] in snakepos[1:]:
                show_text("GAME OVER.",150,350,(0,0,0),50,screen)
                show_text("Press R to restart.",50,450,(0,0,0),30,screen)
                show_text("Press B to go back to Home.",50,500,(0,0,0),30,screen)
                gameover=True
            if snakex in (-size,700) or snakey in (-size,700):
                show_text("GAME OVER.",150,350,(0,0,0),50,screen)
                show_text("Press R to restart.",50,450,(0,0,0),30,screen)
                show_text("Press B to go back to Home.",50,500,(0,0,0),30,screen)
                gameover=True
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        if key[pygame.K_r]:
            gameover=False
            foodx=(randint(0,700)//size)*size
            foody=(randint(0,700)//size)*size
            snakex=(randint(0,700)//size)*size
            snakey=(randint(0,700)//size)*size
            snakepos=[(snakex,snakey)]
            direction=""
            score=0
        if key[pygame.K_b]:
            menu()
def flappy_bird():
    pygame.init()
    screenwidth=900
    screenheight=770
    name="FLAPPY BIRD"
    screen=pygame.display.set_mode((screenwidth,screenheight))
    clock=pygame.time.Clock()
    pygame.display.set_caption(name)
    pipex=800
    x=300
    y=450
    can_score=True
    top_pipe=randint(10,300)
    bottom_pipe=top_pipe+200
    gravity=7
    gameover=False
    score=0
    pipechange=5
    canchange=True
    gamestart=False
    high=0
    tryagain=True
    pygame.display.set_caption(name)
    while tryagain==True:
        key_input=pygame.key.get_pressed()
        if gameover==False: 
            if score%5==0 and score!=0 and canchange==True:
                pipechange+=0.3
                canchange=False
            if gamestart==True:
                pipex-=pipechange
                y+=gravity  
            else:
                show_text("Press SPACE to start.",100,350,(0,0,0),50,screen)
            if score>high:
                high=score
            player=pygame.draw.rect(screen,(245, 225, 0),(x,y,50,50))
            top=pygame.draw.rect(screen,(245, 118, 0),(pipex,0,100,top_pipe))
            bottom=pygame.draw.rect(screen,(245, 118, 0),(pipex,bottom_pipe,100,900))
            score1="SCORE: "+str(score)
            show_text(str(score1),200,10,(0,0,0),50,screen)
            high1="HIGH: "+str(high)
            show_text(str(high1),650,10,(0,0,0),50,screen)
            pygame.display.update()
            screen.fill((61, 191, 178))
            if key_input[pygame.K_SPACE]:
                gravity=-7
            else:
                gravity=7
            if y<=0 or y>=800 or pygame.Rect.colliderect(player,top) or pygame.Rect.colliderect(player,bottom):
                show_text("GAME OVER. Press R to restart.",50,350,(0,0,0),50,screen)
                show_text("Press B to go back to Home",400,400,(0,0,0),30,screen)
                show_text(str(score1),350,10,(0,0,0),50,screen)
                show_text(str(high1),650,10,(0,0,0),50,screen)
                pygame.display.update()
                gameover=True
            if pipex<=-100:
                pipex=900
                top_pipe=randint(10,700)
                bottom_pipe=top_pipe+300
                can_score=True
                canchange=True
            if pipex<=200 and can_score==True:
                score+=1
                can_score=False
            if key_input[pygame.K_SPACE]:
                gamestart=True
            if key_input[pygame.K_p]:
                gamestart=False
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        if key_input[pygame.K_r]:
            gameover=False
            gamestart=False
            x=300
            y=450
            pipex=800
            score=0
            pipechange=5
            can_score=True
            top_pipe=randint(10,700)
            bottom_pipe=top_pipe+300
        if key_input[pygame.K_b]:
            tryagain=False
    menu()
def pong():
    pygame.init()
    screenwidth=900
    screenheight=800
    name="PONG"
    rightpaddle=350
    leftpaddle=350
    ballx=450
    bally=450
    ballspeed=10
    ballangle=0
    rightscore=0
    leftscore=0
    gameover=False
    screen=pygame.display.set_mode((screenwidth,screenheight))
    clock=pygame.time.Clock()
    step=10
    pygame.display.set_caption(name)
    while True:
        key=pygame.key.get_pressed()
        if gameover==False:
            screen.fill((44, 184, 81))
            show_text(str(leftscore),350,100,(0,0,0),50,screen)
            show_text(str(rightscore),550,100,(0,0,0),50,screen)
            pygame.draw.line(screen,(0,0,0),(450,0),(450,800),5)
            ball=pygame.draw.circle(screen,(255,255,255),(ballx,bally),25)
            right=pygame.draw.rect(screen,(255,0,0),(800,rightpaddle,50,200))
            left=pygame.draw.rect(screen,(0,0,255),(50,leftpaddle,50,200))
            ballx+=ballspeed
            bally+=ballangle
            #collide
            if pygame.Rect.colliderect(ball,right):
                ballspeed=-ballspeed
                ballangle=randint(-10,10)
                ballx=750
            elif pygame.Rect.colliderect(ball,left):
                ballspeed=-ballspeed
                ballx=150
                ballangle=randint(-10,10)
            #controls
            if key[pygame.K_UP] and rightpaddle!=0:
                rightpaddle-=step
            if key[pygame.K_DOWN] and rightpaddle!=600:
                rightpaddle+=step
            if key[pygame.K_w] and leftpaddle!=0:
                leftpaddle-=step
            if key[pygame.K_s] and leftpaddle!=600:
                leftpaddle+=step
            if bally<=0 or bally>=800:
                ballangle=-ballangle
            #reset
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
            #win
            if rightscore==11:
                gameover=True
                show_text("Red Wins! Press R to restart and B to go home.",200,400,(0,0,0),30,screen)
            elif leftscore==11:
                gameover=True
                show_text("Blue Wins! Press R to restart and B to go home.",200,400,(0,0,0),30,screen)
            pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        if key[pygame.K_r]:
            gameover=False
            bally=450
            ballx=400
            ballspeed=10
            ballangle=0
            rightpaddle=400
            leftpaddle=400
            leftscore=0
            rightscore=0
            pygame.display.update()
            pygame.time.delay(1000)
        if key[pygame.K_b]:
            menu()
def bombdodge():
    pygame.init()
    screenwidth=900
    screenheight=900
    name="DODGE THE BOMBS"
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
        show_text(f"LIVES:{lives}",750,50,(0,0,0),30,screen)
        show_text(f"SCORE:{score}",500,50,(0,0,0),30,screen)
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
                show_text("Press SPACE to start.",200,400,(0,0,0),50,screen)
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
                show_text("KABOOM!",150,250,(255,0,0),70,screen)
                show_text("OH NO! A bomb fell on you! :( Press R to restart and B to go home.",10,350,(0,0,0),25,screen)
                show_text(f"LIVES:{lives}",750,50,(0,0,0),30,screen)
                show_text(f"SCORE:{score}",500,50,(0,0,0),30,screen)
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
        if key_input[K_b]:
            menu()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
def tron():
    pygame.init()
    size=50
    screenwidth=700
    screenheight=700
    name="TRON"
    score=0
    screen=pygame.display.set_mode((screenwidth,screenheight))
    clock=pygame.time.Clock()
    pygame.display.set_caption(name)
    snakex=700-size
    snakey=700-size
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
        if key[K_b]:
            menu()
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
                    pygame.draw.rect(screen,(255,255,255),(a*size,b*size,size,size),1)
            snakepos.pop()
            snakepos.insert(0,(snakex,snakey))
            snakepos1.pop()
            snakepos1.insert(0,(snakex1,snakey1))
            for x in snakepos:
                snake=pygame.draw.rect(screen,(0,0,255),x+(size,size))
            for y in snakepos1:
                snake1=pygame.draw.rect(screen,(255,0,0),y+(size,size))
            if direction=="right":
                snakex+=size
            elif direction=="left":
                snakex-=size
            elif direction=="up":
                snakey-=size
            elif direction=="down":
                snakey+=size
            if key[K_RIGHT] and direction != "left" and canmove==True:
                direction="right"
            if key[K_LEFT] and direction != "right" and canmove==True:
                direction="left"
            if key[K_UP] and direction != "down" and canmove==True:
                direction="up"
            if key[K_DOWN] and direction != "up" and canmove==True:
                direction="down"


            if direction1=="right":
                snakex1+=size
            if direction1=="left":
                snakex1-=size
            if direction1=="up":
                snakey1-=size
            if direction1=="down":
                snakey1+=size
            if key[K_d] and direction1 != "left" and canmove==True:
                direction1="right"
            if key[K_a] and direction1 != "right" and canmove==True:
                direction1="left"
            if key[K_w] and direction1 != "down" and canmove==True:
                direction1="up"
            if key[K_s] and direction1 != "up" and canmove==True:
                direction1="down"
            if snakepos[0] in snakepos[2:]or snakepos[0] in snakepos1[0:]:
                show_text("Red WINS!!!!!",150,350,(0,0,0),50,screen)
                show_text("Press R to restart and B to go back.",150,450,(0,0,0),30,screen)
                gameover=True
            if snakex in (-size,700) or snakey in (-size,700):
                show_text("Red WINS!!!!!",150,350,(0,0,0),50,screen)
                show_text("Press R to restart and B to go back.",150,450,(0,0,0),30,screen)
                gameover=True
            if snakepos1[0] in snakepos1[2:]or snakepos1[0] in snakepos[0:]:
                show_text("Blue WINS!!!!!",150,350,(0,0,0),50,screen)
                show_text("Press R to restart and B to go back.",150,450,(0,0,0),30,screen)
                gameover=True
            if snakex1 in (-size,700) or snakey1 in (-size,700):
                show_text("Blue WINS!!!!!",150,350,(0,0,0),50,screen)
                show_text("Press R to restart and B to go back.",150,450,(0,0,0),30,screen)
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
menu()