# import pygame
# from random import randint
# from pygame.locals import *
# import time
# # color generator
# def color():
#     colors=[]
#     for x in range(0,3):
#         colors.append(randint(0,255))
#     return tuple(colors)
# # text
# def show_text(msg, x, y, color, size):
#     fontobj= pygame.font.SysFont('rockwell', size)
#     msgobj = fontobj.render(msg,False,color)
#     screen.blit(msgobj,(x, y))

# class circle:
#     radius=10
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y
#         self.radius=10
#     def draw():
#         pygame.draw.circle(screen,(255,255,255),(self.x,self.y),self.radius)
# pygame.init()
# screenwidth=900
# screenheight=900
# name="HI"
# key=0
# screen=pygame.display.set_mode((screenwidth,screenheight))
# clock=pygame.time.Clock()
# pygame.display.set_caption(name)
# circles=[]
# gone=[]
# space=False
# finished=0
# for z in range(0,8):
#     for a in range(0,1):
#         circles.append(circle(450,450))
# while True:
#     key=pygame.key.get_pressed()
#     if key[K_SPACE]:
#         space=True
#     screen.fill((0,0,0))
#     for b in circles:
#         b.draw()
#     pygame.display.update()
#     space=False
#     for event in pygame.event.get():
#         if event.type==QUIT:
#             pygame.quit()
#             exit()