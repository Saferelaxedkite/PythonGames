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
    def __init__(self,x,y,gone):
        self.x=x
        self.y=y
        self.colors=color()
        self.radius=randint(25,100)
        self.speed=randint(1,10)
        self.character=randint(97,122)
        self.show=True
    def draw(self,keypress):
        if self.character==keypress:
            self.show=not self.show
        if self.show==True:
            pygame.draw.circle(screen,self.colors,(self.x,self.y),self.radius)
            show_text(chr(self.character),self.x,self.y,(0,0,0),30)
    def move(self):
        self.x+=self.speed
        if self.x>=900:
            self.speed=-self.speed
            self.x-100
        if self.x<=0:
            self.speed=-self.speed  
            self.x+100
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
for z in range(0,9):
    for a in range(0,10):
        circles.append(circle(a*75,100*z,gone))
while True:
    screen.fill((0,0,0))
    for b in circles:
        b.draw(key)
        b.move()
    key = 0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            key=event.key