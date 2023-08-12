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


pygame.init()
screenwidth=900
screenheight=900
name="Walk"
x=450
y=450
step=0
left=False
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
right=[]
left=[]
rightidle=[]
leftidle=[]
pos=0
pos1=0
lst=right
idlelst=right
jumpright=[]
jumpleft=[]
jumplst=jumpright
change=0
for n in range(0,10):
    walk=pygame.image.load(f"Sprite Animations/animations/Run__00{n}.png")
    right.append(pygame.transform.scale(walk,(100,120)))
for n in range(0,10):
    walk1=pygame.image.load(f"Sprite Animations/animations/Run__00{n}.png")
    walk1=pygame.transform.flip(walk1,True,False)
    left.append(pygame.transform.scale(walk1,(100,120)))
for n in range(0,10):
    idle=pygame.image.load(f"Sprite Animations/animations/Idle__00{n}.png")
    rightidle.append(pygame.transform.scale(idle,(60,110)))
for n in range(0,10):
    idle1=pygame.image.load(f"Sprite Animations/animations/Idle__00{n}.png")
    idle1=pygame.transform.flip(idle1,True,False)
    leftidle.append(pygame.transform.scale(idle1,(60,110)))
for n in range(0,10):
    jump=pygame.image.load(f"Sprite Animations/animations/Jump__00{n}.png")
    jumpright.append(pygame.transform.scale(jump,(100,120)))
for n in range(0,10):
    jump1=pygame.image.load(f"Sprite Animations/animations/Jump__00{n}.png")
    jump1=pygame.transform.flip(jump1,True,False)
    jumpleft.append(pygame.transform.scale(jump1,(100,120)))
while True:
    key=pygame.key.get_pressed()
    clock.tick(30)
    pygame.display.update()
    screen.fill((0,0,0))
    if key[pygame.K_RIGHT] and x<=800:
        x+=10
        pos+=1
        if pos==9:
            pos=0
        lst=right
        idlelst=rightidle
        jumplst=jumpright
        screen.blit(lst[pos],(x,y))
    elif key[pygame.K_LEFT] and x>=0:
        x-=10
        pos+=1
        if pos==9:
            pos=0
        lst=left
        idlelst=leftidle
        jumplst=jumpleft
        screen.blit(lst[pos],(x,y))
    elif key[pygame.K_UP]:
        for z in range(0,5):
            change+=z
            if change%50==0:
                pos+=1
                if pos==9:
                    pos=0
            y-=50
            clock.tick(30)
            pygame.display.update()
            screen.fill((0,0,0))
            screen.blit(jumplst[pos],(x,y))
        for a in range(0,5):
            change+=a
            if change%25==0:
                pos+=1
                if pos==9:
                    pos=0
            y+=50
            clock.tick(30)
            pygame.display.update()
            screen.fill((0,0,0))
            screen.blit(jumplst[pos],(x,y))
    else:
        screen.blit(idlelst[pos1],(x,y))
        pos1+=1
        if pos1==9:
            pos1=0
        
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()