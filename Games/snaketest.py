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
def show_text(msg, x, y, color, size,screen):
    fontobj= pygame.font.SysFont('rockwell', size)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x, y))


pygame.init()
size=10
screenwidth=700
screenheight=700
name="Snake"
score=0
screen=pygame.display.set_mode((screenwidth,screenheight))
clock=pygame.time.Clock()
pygame.display.set_caption(name)
foodx=(randint(0,700)//size)*size
foody=(randint(0,700)//size)*size
snakex=(randint(0,700)//size)*size
snakey=(randint(0,700)//size)*size
snakepos=[(snakex,snakey)]
direction=""
gameover=False
while True:
    key=pygame.key.get_pressed()
    if gameover==False:
        screen.fill((0,255,0))
        for a in range(0,700//size):
            for b in range(0,700//size):
                pygame.draw.rect(screen,(255,255,255),(a*size,b*size,size,size),1)
        clock.tick(15)
        show_text(str(score),400,10,(0,0,0),30,screen)
        snakepos.pop()
        snakepos.insert(0,(snakex,snakey))
        for x in snakepos:
            snake=pygame.draw.rect(screen,(0,0,255),x+(size,size))
        if direction=="right":
            snakex+=size
        elif direction=="left":
            snakex-=size
        elif direction=="up":
            snakey-=size
        elif direction=="down":
            snakey+=size
        if key[K_RIGHT] and direction != "left":
            direction="right"
        elif key[K_LEFT] and direction != "right":
            direction="left"
        elif key[K_UP] and direction != "down":
            direction="up"
        elif key[K_DOWN] and direction != "up":
            direction="down"
        food=pygame.draw.rect(screen,(255,0,0),(foodx,foody,size,size))
        if snakex==foodx and snakey==foody:
            foodx=(randint(0,700)//size)*size
            foody=(randint(0,700)//size)*size
            score+=1
            snakepos.append((snakex,snakey))
        if snakepos[0] in snakepos[1:]:
            show_text("GAME OVER.",150,350,(0,0,0),50,screen)
            show_text("Press R to restart.",50,450,(0,0,0),30,screen)
            show_text("Press B to go back to Home.",50,500,(0,0,0),30,screen)
            gameover=True
        if snakex in (-size,700) or snakey in (-size,700):
            show_text("GAME OVER.",150,350,(0,0,0),50,screen)
            show_text("Press R to restart.",50,450,(0,0,0),30,screen)
            show_text("Press B to go back to Home.",50,500,(0,0,0),30,screen)
            gameover=True
        pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
    if key[pygame.K_r]:
        gameover=False
        foodx=(randint(0,700)//size)*size
        foody=(randint(0,700)//size)*size
        snakex=(randint(0,700)//size)*size
        snakey=(randint(0,700)//size)*size
        snakepos=[(snakex,snakey)]
        direction=""
        score=0