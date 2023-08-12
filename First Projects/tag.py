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


pygame.init()
screenwidth=800
screenheight=800
length=100
height=100
infinite=0
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
x=0
y=0
x1=600
y1=600
step=10
tagger = Rect(100, 100, 100) 
runner = Rect(100, 100, 100)
collide=False
while True:
    collide=pygame.Rect.colliderect(tagger,runner)
    print(collide)
    pygame.display.update()
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,255,0),tagger)
    pygame.draw.rect(screen,(255,0,0),runner)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    #player 1
    key_input = pygame.key.get_pressed()   
    if key_input[pygame.K_LEFT] and x!=0:
        x -= step
    if key_input[pygame.K_UP] and y!=0:
        y -= step
    if key_input[pygame.K_RIGHT] and x!=screenwidth-length:
        x += step
    if key_input[pygame.K_DOWN] and y!=screenheight-height:
        y += step
    #player2
    key_input1 = pygame.key.get_pressed()   
    if key_input1[pygame.K_a] and x1!=0:
        x1 -= 5
    if key_input1[pygame.K_w] and y1!=0:
        y1 -= 5
    if key_input1[pygame.K_d] and x1!=screenwidth-200:
        x1 += 5
    if key_input1[pygame.K_s] and y1!=screenheight-200:
        y1 += 5
    if collide==False:
        screen.fill((0,255,255))