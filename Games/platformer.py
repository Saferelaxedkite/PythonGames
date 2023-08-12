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
x=0
y=500
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
level=[1,1,1,1,0,0,1,1,1]
change=0
gravity=5
jump=False
tilelevel=[]
hitlist=[]
move={"up":False,"left":False,"right":False,"down":False}
collide={"up":False,"left":False,"right":False,"down":True}
tile=pygame.image.load("Sprite Animations/platformer(desert)/png/Tile/2.png")
tile=pygame.transform.scale(tile,(100,100))
idle=pygame.image.load(f"Sprite Animations/ninja animations/Idle__001.png")
idle=pygame.transform.scale(idle,(60,120))
player=pygame.Rect(0,500,60,120)


while True:
    screen.fill((0,0,0))
    hitlist=[]
    tilelevel=[]
    for z in range(0,9):
        if level[z]==1:
            tile1=screen.blit(tile,(100*z,700))
            tilelevel.append(tile1)
    move={"up":False,"left":False,"right":False,"down":False}
    key=pygame.key.get_pressed()
    clock.tick(100)
    player=screen.blit(idle,(player.x,player.y))
    if key[pygame.K_RIGHT] and player.x<=840:
        move["right"]=True
    if key[pygame.K_LEFT] and player.x>=0:
        move["left"]=True
    if key[pygame.K_UP]:
        if jump==False:
            gravity=-13
            jump=True
    if move["right"]==True:
        player.x+=10
    if move["left"]==True:
        player.x-=10
    player.y+=gravity
    gravity+=0.5
    for k in tilelevel:
        if pygame.Rect.colliderect(player,k):
            hitlist.append(k)
    collide={"up":False,"left":False,"right":False,"down":False}
    for k in hitlist:
        player.bottom=k.top
        collide["down"]=True
    if collide["down"]==True:
        jump=False
        gravity=0
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()