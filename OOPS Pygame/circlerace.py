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
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.colors=(255,255,255)
        self.radius=50
        self.speed=0
        self.laps=0
        self.changefinished=True
        self.changecolor=True
    def move(self,spacepressed,finishers):
        if self.laps==10:
            self.changefinished=False
            if finishers==1 and self.changecolor==True:
                self.colors=(0,255,0)
                self.changecolor=False
            if finishers==2 and self.changecolor==True:
                self.colors=(0,0,255)
                self.changecolor=False
            if finishers==3 and self.changecolor==True:
                self.colors=(255,0,0)
                self.changecolor=False
        else:
            self.x+=self.speed
            if spacepressed==True:
                self.speed=randint(1,30)
            if self.x<=0:
                self.speed=randint(1,30)
                self.laps+=1
            if self.x>=900:
                self.speed=randint(-30,-1)
                self.laps+=1
        pygame.draw.circle(screen,self.colors,(self.x,self.y),self.radius)
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
space=False
finished=0
for z in range(0,8):
    for a in range(0,1):
        circles.append(circle(a*75+51,100*z+51))
while True:
    key=pygame.key.get_pressed()
    if key[K_SPACE]:
        space=True
    screen.fill((0,0,0))
    for b in circles:
        b.move(space,finished)
        if b.laps==10 and b.changefinished==True:
            finished+=1
    pygame.display.update()
    space=False
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()