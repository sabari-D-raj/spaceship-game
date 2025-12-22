import pygame
import sys
import random

pygame.init()
fps=pygame.time.Clock()
width,height=800,800
screen=pygame.display.set_mode((width,height))
background= pygame.image.load("images/Parallax60.png").convert()
background=pygame.transform.scale(background,(width,height))
player= pygame.image.load("images/rockect.png").convert_alpha()
player=pygame.transform.scale(player,(100,100))
player_x,player_y=350,690
bg_visible,bg_above,bg_speed =0,-height,3

running=True
while running:
    fps.tick(60)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    bg_visible+=bg_speed
    bg_above+=bg_speed
    if bg_visible>=height:
        bg_visible= -height
    if bg_above >=height:
        bg_above= -height
    key=pygame.key.get_pressed()
    if key[pygame.K_d]:
        player_x+=5
    if key[pygame.K_a]:
        player_x-=5
    if player_x>=800 or player_x<=0:
        print("out")     
    screen.blit(background,(0,bg_visible))
    screen.blit(background,(0,bg_above))
    screen.blit(player,(player_x,player_y))
    pygame.display.update()
pygame.quit()
sys.exit()