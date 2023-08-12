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

class circle:
    def __init__(self):
        self.x=randint(50,850)
        self.y=800
        self.colors=color()
        self.radius=50
        self.speed=randint(1,5)
        self.character=randint(97,122)
        self.show=True
        self.makenew=False
        self.removelife=False
    def draw(self,keypress):
        if self.character==keypress and self.show==True:
            self.show=False
            self.makenew=True
            self.removelife=False
        if self.show==True:
            pygame.draw.circle(screen,self.colors,(self.x,self.y),self.radius)
            show_text(chr(self.character),self.x,self.y,(0,0,0),30)
    def move(self):
        self.y-=self.speed
pygame.init()
screenwidth=900
screenheight=900
name="HI"
key=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
circles=[]
gone=[]
lives=3
score=0
for a in range(0,3):
    circles.append(circle())
gameover=False
while True:
    lives1="LIVES: "+str(lives)
    screen.fill((0,0,0))
    if gameover==False:
        show_text(str(score),450,50,(255,255,255),30)
        show_text(lives1,600,50,(255,255,255),30)
        for b in circles:
            b.draw(key)
            b.move()
            if b.makenew==True:
                circles.append(circle())
                b.makenew=False
                if b.removelife==True:
                    pass
                else:
                    score+=1
            if b.y<=0:
                b.removelife=True
            if b.removelife==True:
                lives-=1
                b.makenew=True
                b.removelife=False
            key = 0
        if lives==0:
            gameover=True
        pygame.display.update()
    else:
        show_text("GAME OVER",350,350,(255,255,255),50)
        pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            key=event.key