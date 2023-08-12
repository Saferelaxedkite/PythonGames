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
screenwidth=700
screenheight=700
name="Snake"
score=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
foodx=(randint(0,700)//20)*20
foody=(randint(0,700)//20)*20
snakex=(randint(0,700)//20)*20
snakey=(randint(0,700)//20)*20
snakepos=[(snakex,snakey)]
direction=""
gameover=False
while True:
    key=pygame.key.get_pressed()
    if gameover==False:
        screen.fill((0,255,0))
        for a in range(0,45):
            for b in range(0,45):
                pygame.draw.rect(screen,(255,255,255),(a*20,b*20,20,20),1)
        clock.tick(15)
        show_text(str(score),400,10,(0,0,0),30)
        snakepos.pop()
        snakepos.insert(0,(snakex,snakey))
        for x in snakepos:
            snake=pygame.draw.rect(screen,(0,0,255),x+(20,20))
        if direction=="right":
            snakex+=20
        elif direction=="left":
            snakex-=20
        elif direction=="up":
            snakey-=20
        elif direction=="down":
            snakey+=20
        if key[K_RIGHT] and direction != "left":
            direction="right"
        elif key[K_LEFT] and direction != "right":
            direction="left"
        elif key[K_UP] and direction != "down":
            direction="up"
        elif key[K_DOWN] and direction != "up":
            direction="down"
        food=pygame.draw.rect(screen,(255,0,0),(foodx,foody,20,20))
        if snakex==foodx and snakey==foody:
            foodx=(randint(0,700)//20)*20
            foody=(randint(0,700)//20)*20
            score+=1
            snakepos.append((snakex,snakey))
        if snakepos[0] in snakepos[1:]:
            show_text("GAME OVER.",150,350,(0,0,0),50)
            gameover=True
        if snakex in (-20,700) or snakey in (-20,700):
            show_text("GAME OVER.",150,350,(0,0,0),50)
            gameover=True
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()