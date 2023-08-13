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


def collide(player,tilelevel):
    hitlist=[]
    for k in tilelevel:
        if pygame.Rect.colliderect(player,k):
            hitlist.append(k)
    return hitlist


def reaction(move,player,tilelevel):
    collides={"up":False,"left":False,"right":False,"down":False}
    player.x+=move[0]
    hitlist=collide(player,tilelevel)
    for k in hitlist:
        if move[0]>0:
            player.right=k.left
            collides["right"]=True
        if move[0]<0:
            player.left=k.right
            collides["left"]=True
    player.y+=move[1]
    hitlist=collide(player,tilelevel)
    for k in hitlist:
        if move[1]>0:
            player.bottom=k.top
            collides["down"]=True
        if move[1]<0:
            player.top=k.bottom
            collides["top"]=True
    return collides, player

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
level=[[[1,1,1,1,0,0,1,1,1],[0,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,1,0],[0,0,1,0,1,0,1,0,1]]
,[[1,1,0,1,0,1,1,1,1],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1]],
[[1,0,0,0,0,0,1,1,1],[0,0,0,1,0,0,0,1,1],[0,1,0,0,1,0,0,1,0],[0,0,1,0,1,0,1,0,1],[0,0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1]],
[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[1,0,0,1,0,0,1,0,1]]
,[[1,1,1,1,1,1,1,1,1]]
]
change=0
gravity=5
jump=False
tilelevel=[]
hitlist=[]
move={"up":False,"left":False,"right":False,"down":False}
tile=pygame.image.load("Sprite Animations/platformer(desert)/png/Tile/2.png")
tile=pygame.transform.scale(tile,(100,100))
idle=pygame.image.load(f"Sprite Animations/ninja animations/Idle__001.png")
idle=pygame.transform.scale(idle,(1,1))
idle1=pygame.transform.flip(idle,True,False)
player=pygame.Rect(0,500,60,120)
bg=pygame.image.load("Sprite Animations/platformer(desert)/png/BG.png")
y1=900
z1=-100
counter=0
orient=[idle,idle1]
pos=0
while True:
    y1=800
    z1=-100
    screen.blit(bg,(0,0))
    hitlist=[]
    tilelevel=[]
    for z in range(0,len(level[counter])):
        z1=-100
        y1-=100
        for y in level[counter][z]:
            z1+=100
            if y==1:
                tile1=screen.blit(tile,(z1,y1))
                tilelevel.append(tile1)
    move={"up":False,"left":False,"right":False,"down":False}
    movement=[0,0]
    key=pygame.key.get_pressed()
    clock.tick(100)
    player=screen.blit(orient[pos],(player.x,player.y))
    if key[pygame.K_RIGHT] and player.x<=840:
        move["right"]=True
        movement[0]=5
        pos=0
    if key[pygame.K_LEFT] and player.x>=0:
        move["left"]=True
        movement[0]=-5
        pos=1
    if key[pygame.K_UP] and collides["down"]==True:
        if jump==False:
            gravity=-30
            movement[1]=20
            jump=True
    if move["right"]==True:
        player.x+=5
    if move["left"]==True:
        player.x-=5
    movement[1]+=gravity
    gravity+=1
    collides,player=reaction(movement,player,tilelevel)
    if collides["down"]==True:
        jump=False
        gravity=0
    if collides["up"]==True:
        jump=True
        gravity=10
    if player.y>=900:
        player.x=10
        player.y=10
        gravity=0
    if player.x>=840:
        if counter!=len(level)-1:
            counter+=1
        player.x=10
        player.y=10
        movement[0]=10
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()