import pygame
from random import randint
from pygame.locals import *
import time
#win

def win(board):
    winner=""
    #horizontal
    global gameover
    gameover=False
    if board[0]==board[1]==board[2]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[0]==board[1]==board[2]=="X":
        winner="Rectangle Wins!"
        gameover=True
    if board[3]==board[4]==board[5]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[3]==board[4]==board[5]=="X":
        winner="Rectangle Wins!"
        gameover=True
    if board[6]==board[7]==board[8]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[6]==board[7]==board[8]=="X":
        winner="Rectangle Wins!"
        gameover=True

    #vertical
    if board[0]==board[3]==board[6]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[0]==board[3]==board[6]=="X":
        winner="Rectangle Wins!"
        gameover=True
    if board[1]==board[4]==board[7]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[1]==board[4]==board[7]=="X":
        winner="Rectangle Wins!"
        gameover=True
    if board[2]==board[5]==board[8]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[2]==board[5]==board[8]=="X":
        winner="Rectangle Wins!"
        gameover=True
    
    #diagonal
    if board[0]==board[4]==board[8]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[0]==board[4]==board[8]=="X":
        winner="Rectangle Wins!"
        gameover=True
    if board[2]==board[4]==board[6]=="O":
        winner="Circle Wins!"
        gameover=True
    if board[2]==board[4]==board[6]=="X":
        winner="Rectangle Wins!"
        gameover=True
    return winner
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
board=[" "," "," "," "," "," "," "," "," "]
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
gameover=True
rect=False
while True:
    if gameover==False:
        for y in range(0,screenwidth,300):   
            for x in range(0,screenwidth,300):
                pygame.draw.rect(screen,(255,255,255),(x,y,300,300),5)
        cords=pygame.mouse.get_pos()
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
            if event.type==MOUSEBUTTONDOWN:

                # first row

                if 0<cords[0]<300 and 0<cords[1]<300:
                    if rect==True and board[0]==" ":
                        pygame.draw.rect(screen,(255,0,0),(50,50,200,200))
                        rect=False
                        board[0]="O"
                    elif rect==False and board[0]==" ":
                        pygame.draw.circle(screen,(0,0,255),(150,150),100)
                        rect=True
                        board[0]="X"
                    win(board)
                
                if 300<cords[0]<600 and 0<cords[1]<300:
                    if rect==True and board[1]==" ":
                        pygame.draw.rect(screen,(255,0,0),(350,50,200,200))
                        rect=False
                        board[1]="O"
                    elif rect==False and board[1]==" ":
                        pygame.draw.circle(screen,(0,0,255),(450,150),100)
                        rect=True
                        board[1]="X"
                    win(board)
                if 600<cords[0]<900 and 0<cords[1]<300:
                    if rect==True and board[2]==" ":
                        pygame.draw.rect(screen,(255,0,0),(650,50,200,200))
                        rect=False
                        board[2]="O"
                    elif rect==False and board[2]==" ":
                        pygame.draw.circle(screen,(0,0,255),(750,150),100)
                        rect=True
                        board[2]="X"
                    win(board)
                
                #second row

                if 0<cords[0]<300 and 300<cords[1]<600:
                    if rect==True and board[3]==" ":
                        pygame.draw.rect(screen,(255,0,0),(50,350,200,200))
                        rect=False
                        board[3]="O"
                    elif rect==False and board[3]==" ":
                        pygame.draw.circle(screen,(0,0,255),(150,450),100)
                        rect=True
                        board[3]="X"
                    win(board)

                if 300<cords[0]<600 and 300<cords[1]<600:
                    if rect==True and board[4]==" ":
                        pygame.draw.rect(screen,(255,0,0),(350,350,200,200))
                        rect=False
                        board[4]="O"
                    elif rect==False and board[4]==" ":
                        pygame.draw.circle(screen,(0,0,255),(450,450),100)
                        rect=True
                        board[4]="X"
                    win(board)
                if 600<cords[0]<900 and 300<cords[1]<600:
                    if rect==True and board[5]==" ":
                        pygame.draw.rect(screen,(255,0,0),(650,350,200,200))
                        rect=False
                        board[5]="O"
                    elif rect==False and board[5]==" ":
                        pygame.draw.circle(screen,(0,0,255),(750,450),100)
                        rect=True
                        board[5]="X"
                    win(board)

                #third row        

                if 0<cords[0]<300 and 600<cords[1]<900:
                    if rect==True and board[6]==" ":
                        pygame.draw.rect(screen,(255,0,0),(50,650,200,200))
                        rect=False
                        board[6]="O"
                    elif rect==False and board[6]==" ":
                        pygame.draw.circle(screen,(0,0,255),(150,750),100)
                        rect=True
                        board[6]="X"
                    win(board)

                if 300<cords[0]<600 and 600<cords[1]<900:
                    if rect==True and board[7]==" ":
                        pygame.draw.rect(screen,(255,0,0),(350,650,200,200))
                        rect=False
                        board[7]="O"
                    elif rect==False and board[7]==" ":
                        pygame.draw.circle(screen,(0,0,255),(450,750),100)
                        rect=True
                        board[7]="X"
                    win(board)

                if 600<cords[0]<900 and 600<cords[1]<900:
                    if rect==True and board[8]==" ":
                        pygame.draw.rect(screen,(255,0,0),(650,650,200,200))
                        rect=False
                        board[8]="O"
                    elif rect==False and board[8]==" ":
                        pygame.draw.circle(screen,(0,0,255),(750,750),100)
                        rect=True
                        board[8]="X"
                    win(board)      