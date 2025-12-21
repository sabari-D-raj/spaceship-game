import pygame
import sys
import random

pygame.init()
fps=pygame.time.Clock()
width,height=800,800
screen=pygame.display.set_mode((width,height))
background= pygame.image.load("images/Parallax60.png").convert()
background=pygame.transform.scale(background,(width,height))
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
    screen.blit(background,(0,bg_visible))
    screen.blit(background,(0,bg_above))
    pygame.display.update()
pygame.quit()
sys.exit()