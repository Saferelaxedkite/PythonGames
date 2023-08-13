import pygame
from random import randint
from pygame.locals import *
import time
# color generator
class character():
    def __init__(self,x,y,color,height,width,speed,bullets,fired):
        self.x=x
        self.y=y
        self.color=color
        self.height=height
        self.width=width
        self.speed=speed
        self.bullets=bullets
        self.fired=fired
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

class alien(character):
    def movealien(self):
        self.x+=self.speed
        if self.x>=900 or self.x<=0:
            self.speed=-self.speed
            self.y+=30
    def draw(self):
        if self.bullets==3:
            self.color=((255,0,0))
        elif self.bullets==2:
            self.color=((255,200,0))
        elif self.bullets==1:
            self.color=((100,250,0))
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.height))

class player(character):
    def moveplayer(self,key):
        if key[K_LEFT]:
            self.x-=self.speed
        elif key[K_RIGHT]:
            self.x+=self.speed
        if self.x>=800:
            self.x=800
        elif self.x<=0: 
            self.x=0

class bullet(character):
    def fire(self,bulletlist,alienlist):
        for b in bulletlist:
            for c in alienlist:
                if pygame.Rect.colliderect(pygame.Rect(b.x,b.y,b.width,b.height),
                pygame.Rect(c.x,c.y,c.width,c.height)) and b in bulletlist:
                    c.bullets-=1
                    bulletlist.remove(b)
                if c.bullets<=0 and c in alienlist:
                    alienlist.remove(c)
        self.y-=self.speed

class alienbullet(bullet):
    def __init__(self,x,y,color,height,width,speed,bullets,fired,list):
        self.x=x
        self.y=y
        self.color=color
        self.height=height
        self.width=width
        self.speed=3
        self.bullets=bullets
        self.fired=fired
        self.delay=randint(500,1000)
        self.list=list
    def fire(self,alienbulletlist,spaceship):
        for b in alienbulletlist:
            if pygame.Rect.colliderect(pygame.Rect(b.x,b.y,b.width,b.height),
            pygame.Rect(spaceship.x,spaceship.y,spaceship.width,spaceship.height)):
                self.bullets="HIT"
        self.y+=self.speed

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
screenheight=750
name="Space Invaders"
bg=pygame.image.load("Sprite Animations/free_plane_sprite/png/BG.png")
cooldown=False
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
aliens=[]
fired=False
speed=5
spaceship=player(400,700,(0,0,255),30,100,5,0,True)
bullets=[]
bulletsleft=100
gameover=False
alienbullets=[alienbullet(0,0,(0,0,0),1,1,0,0,True,[])]
for y in range(1,3):
    for x in range(1,11):
        aliens.append(alien(x*50,y*50,(255,0,0),30,30,5,1,True))
allnums=[]
screen.blit(bg,(0,0))
gamestart=False
while True:
    key=pygame.key.get_pressed()
    if gamestart==True:
        if gameover==False:
            clock.tick(60)
            screen.blit(bg,(0,0))
            bulletsleft1="BULLETS: "+str(bulletsleft)
            show_text(bulletsleft1,650,50,(255,255,255),30)
            spaceship.draw()
            spaceship.moveplayer(key)
            for b in bullets: 
                b.draw()
                b.fire(bullets,aliens)
            for a in aliens:
                a.draw() 
                a.movealien()
                if a.y>=670:
                    show_text("GAME OVER",300,300,(0,0,0),50)
                    gameover=True
            for c in alienbullets:
                c.list.append(0)
                if c. bullets=="HIT":
                    show_text("GAME OVER",300,300,(255,255,255),50)
                    gameover=True
                if c.y>=900:
                    alienbullets.remove(c) 
                c.fire(alienbullets,spaceship)
                print(alienbullets)
                c.draw()
                if len(c.list)>=c.delay:
                    alienbullets.append(alienbullet(a.x,a.y,(25,0,0),10,10,1,0,True,[]))
            if key[K_SPACE] and cooldown==False and bulletsleft>0:
                bullets.append(bullet(spaceship.x+50,700,(250,0,0),10,10,10,0,True))
                cooldown=True
                bulletsleft=100-len(bullets)
            if aliens==[]:
                cooldown=False
                fired=False
                spaceship=player(400,700,(0,0,255),30,100,3,0,False)
                bullets=[]
                for y in range(1,4):
                    for x in range(1,11):
                        aliens.append(alien(x*50,y*50,(255,0,0),30,30,5,3,True))
        else:
            show_text("Press R to restart.",300,500,(0,0,0),50)
            if key[K_r]:
                cooldown=False
                aliens=[]
                fired=False
                speed=5
                spaceship=player(400,700,(0,0,255),30,100,5,0,True)
                bullets=[]
                bulletsleft=100
                gameover=False
                alienbullets=[alienbullet(0,0,(0,0,0),1,1,0,0,True,[])]
                for y in range(1,3):
                    for x in range(1,11):
                        aliens.append(alien(x*50,y*50,(255,0,0),30,30,5,1,True))
                allnums=[]
                gamestart=False
                screen.blit(bg,(0,0))
    else:
        show_text("Press SPACE to start.",300,300,(255,255,255),50)
        if key[K_SPACE]:
            gamestart=True
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYUP and event.key==pygame.K_SPACE:
            cooldown=False
