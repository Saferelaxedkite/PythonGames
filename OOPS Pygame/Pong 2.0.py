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

class Ball():
    def __init__(self):
        self.x=400
        self.y=400
        self.speed=15
        self.angle=0
        self.size=25
        self.color=(255,255,255)
    def draw(self,p1y,p2y):
        if self.x==730 and self.y in range(p1y,p1y+200) or self.x==70 and self.y in range(p2y,p2y+200):
            self.speed=-self.speed
            self.angle=randint(-10,10)
        self.x+=self.speed
        self.y+=self.angle
        if self.y>=800 or self.y<=0:
            self.angle=-self.angle
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.size,1)
class Paddle():
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.height=200
        self.width=20
        self.up=False
        self.down=False
        self.score=0
        self.speed=20
    def draw(self,key):
        if key[K_UP] and self.y>=0:
            self.y-=self.speed
        if key[K_DOWN] and self.y<=600:
            self.y+=self.speed
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.width,self.height))
    def draw1(self,key):
        if key[K_w] and self.y>=0:
            self.y-=self.speed
        if key[K_s] and self.y<=600:
            self.y+=self.speed
        pygame.draw.rect(screen,(255,255,255),(self.x,self.y,self.width,self.height))
pygame.init()
screenwidth=800
screenheight=800
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
ball=Ball()
p1=Paddle(750,300)
p2=Paddle(50,300)
gameover=False
while True:
    if gameover==False:
        screen.fill(color())
        pygame.draw.line(screen,(0,0,0),(400,800),(400,0),10)
        show_text(str(p1.score),600,50,(0,0,0),30)
        show_text(str(p2.score),200,50,(0,0,0),30)
        key=pygame.key.get_pressed()
        p1.draw(key)
        p2.draw1(key)
        ball.draw(p1.y,p2.y)
        if ball.x>800: 
            ball=Ball()
            p1.y=300
            p2.y=300
            p2.score+=1
            pygame.time.delay(1000)
        if ball.x<0:
            ball=Ball()
            p1.y=300
            p2.y=300
            p1.score+=1
            pygame.time.delay(1000)
        if p1.score==11 or p2.score==11:
            show_text("__GAME OVER__",150,350,(0,0,0),50)
            gameover=True
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()