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
name="Flappy Square"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
pipex=800
x=300
y=450
can_score=True
top_pipe=randint(10,700)
bottom_pipe=top_pipe+300
gravity=7
gameover=False
score=0
pipechange=5
canchange=True
gamestart=False
high=0
pygame.display.set_caption(name)
while True:
    key_input=pygame.key.get_pressed()
    if gameover==False: 
        if score%5==0 and score!=0 and canchange==True:
            pipechange+=0.3
            canchange=False
        if gamestart==True:
            pipex-=pipechange
            y+=gravity  
        else:
            show_text("Press SPACE to start.",100,350,(0,0,0),50)
        if score>high:
            high=score
        player=pygame.draw.rect(screen,(245, 225, 0),(x,y,50,50))
        top=pygame.draw.rect(screen,(245, 118, 0),(pipex,0,100,top_pipe))
        bottom=pygame.draw.rect(screen,(245, 118, 0),(pipex,bottom_pipe,100,900))
        score1="SCORE: "+str(score)
        show_text(str(score1),200,10,(0,0,0),50)
        high1="HIGH: "+str(high)
        show_text(str(high1),650,10,(0,0,0),50)
        pygame.display.update()
        screen.fill((61, 191, 178))
        if key_input[pygame.K_SPACE]:
            gravity=-7
        else:
            gravity=7
        if y<=0 or y>=800 or pygame.Rect.colliderect(player,top) or pygame.Rect.colliderect(player,bottom):
            show_text("GAME OVER. Press R to restart.",50,350,(0,0,0),50)
            show_text(str(score1),350,10,(0,0,0),50)
            show_text(str(high1),650,10,(0,0,0),50)
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
        pipechange=7
        can_score=True
        top_pipe=randint(10,700)
        bottom_pipe=top_pipe+300