# My First Code
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

def show_text(msg, x, y, color, size):
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))


pygame.init()
screenwidth=1430
screenheight=800
name="HI"
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
x=0
y=0
step=10
enemy_x=500
enemy_y=500
gameover=False
pygame.display.set_caption(name)
while True:
    enemy=pygame.draw.rect(screen,(255,0,0),(enemy_x,enemy_y,100,100))
    player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
    game_over=enemy.colliderect(player)
    key_input=pygame.key.get_pressed()
    pygame.display.update()
    screen.fill((0,255,0))
    if game_over==False:
        if key_input[pygame.K_LEFT] and x!=0:
            while x !=0:
                screen.fill((0,255,0))
                x -= step
                player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
                pygame.display.update()
        if key_input[pygame.K_UP] and y!=0:
            while y !=0:
                screen.fill((0,255,0))
                y -= step
                player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
                pygame.display.update()
        if key_input[pygame.K_RIGHT] and x!=screenwidth-100:
            while x !=screenwidth-100:
                x += step
                screen.fill((0,255,0))
                player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
                pygame.display.update()
        if key_input[pygame.K_DOWN] and y!=screenheight-100:
            while y !=screenheight-100:
                y += step
                screen.fill((0,255,0))
                player=pygame.draw.rect(screen,(0,0,2,55),(x,y,100,100))
                pygame.display.update()



        if key_input[pygame.K_a] and enemy_x!=0:
            enemy_x -= step
        if key_input[pygame.K_w] and enemy_y!=0:
            enemy_y -= step
        if key_input[pygame.K_d] and enemy_x!=screenwidth-100:
            enemy_x += step
        if key_input[pygame.K_s] and enemy_y!=screenheight-100:
            enemy_y += step
    else: 
        show_text(f"GAME OVER.",50,450,(0,0,0),50)
        if key_input[pygame.K_SPACE]:
            gameover=False
            enemy_x=500
            enemy_y=500
            x=0
            y=0
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()