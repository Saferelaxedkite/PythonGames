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
step=10
left=False
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
images=[]
pos=0
for n in range(0,10):
    walk=pygame.image.load(f"Sprite Animations/animations/Run__00{n}.png")
    images.append(pygame.transform.scale(walk,(100,120)))
while True:
    clock.tick(40)
    screen.fill((0,0,0))
    screen.blit(images[pos],(x,450))
    pygame.display.update()
    pos+=1
    if pos==9:
        pos=0
    x+=step
    if x>=800 or x<=0:
        step=-step
        for z in range(0,len(images)):
            images[z]=pygame.transform.flip(images[z],True,False)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()