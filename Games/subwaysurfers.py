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
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))

class character():
    def __init__(self,x,y,width,hieght,speed,color,screen):
        self.x=x
        self.y=y
        self.width=width
        self.hieght=hieght
        self.speed=speed
        self.color=color
        self.screen=screen
    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.hieght))

class train(character):
    def movetrain(self):
        self.y+=self.speed

pygame.init()
screenwidth=900
screenheight=900
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
newtrain=True
trains=[]
lanes=[0,400,800]
playerlane=1
left=True
right=True
while True:
    key=pygame.key.get_pressed()
    screen.fill((255,0,0))
    player=pygame.draw.rect(screen,(0,0,0),(lanes[playerlane],700,100,100))
    if newtrain==True:
        trains.append(train(lanes[randint(0,2)],-200,100,200,20,(0,0,0),screen))
        newtrain=False
    for x in trains:
        x.draw()
        x.movetrain()
        if x.y>=900:
            trains.remove(x)
            newtrain=True
    if key[K_LEFT] and playerlane!=0 and left==True:
        playerlane-=1
        left=False
    if key[K_RIGHT] and playerlane!=2 and right==True:
        playerlane+=1
        right=False
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYUP and event.key==K_LEFT:
                left=True
        if event.type==KEYUP and event.key==K_RIGHT:
            right=True